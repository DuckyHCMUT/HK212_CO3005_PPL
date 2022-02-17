# Generate Abstract Syntax Tree from a parse tree generated from ANTLR

from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

### Remember to uncomment this mess before submit to BKEL ###
from main.d96.utils.AST import ArrayLiteral, AttributeDecl, BinaryOp, BoolType, BooleanLiteral, Break, ClassDecl, ConstDecl, Continue, MethodDecl, NewExpr, NullLiteral, Return
from main.d96.utils.AST import FloatLiteral, StringLiteral, IntLiteral, SelfLiteral, StringType, UnaryOp
from main.d96.utils.AST import FloatType, Id, Instance, IntType, Program, Static, VarDecl, ArrayType, CallStmt

class ASTGeneration(D96Visitor):
    # Visit a parse tree produced by D96Parser#program.
    # program: class_decl+ EOF;
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        declList = []
        for x in ctx.class_decl():
            decl = self.visitClass_decl(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return Program(declList)


    # Visit a parse tree produced by D96Parser#class_decl.
    # class_decl: ('Class' ID (COLON ID)? LP class_body* RP );
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        memberList = []
        name = Id(ctx.ID(0).getText())
        parent = Id(ctx.ID(1).getText()) if ctx.ID(1) else None

        for x in ctx.class_body():
            member = self.visitClass_body(x)
            if isinstance(member, list):
                memberList.extend(member if member else [])
            else:
                memberList.append(member)
        return ClassDecl(name, memberList, parent) 


    # Visit a parse tree produced by D96Parser#class_body.
    # class_body: class_attr | class_method;
    # --> Just need to visit either of class member
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_attr.
    # class_attr: attr_no_value | attr_with_value | attr_array_no_value | attr_array_with_value;
    # --> Just need to visit either any attribute
    def visitClass_attr(self, ctx:D96Parser.Class_attrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by D96Parser#attr_no_value.
    # attr_no_value: (VAR | VAL) any_id (COMMA any_id)* COLON data_type SEMI;
    # However, attr_no_value can only be VAR
    def visitAttr_no_value(self, ctx:D96Parser.Attr_no_valueContext):
        attrList = []
        
        for name in ctx.any_id():
            if '$' in name.getText(): attrList.append(AttributeDecl(Static().__str__(), VarDecl(Id(name.getText()), self.visit(ctx.data_type()))))
            else: attrList.append(AttributeDecl(Instance().__str__(), VarDecl(Id(name.getText()), self.visit(ctx.data_type()))))

        return attrList


    # Visit a parse tree produced by D96Parser#attr_with_value.
    # attr_with_value: (VAR | VAL) any_id attr_pair all_expr SEMI; 
    def visitAttr_with_value(self, ctx:D96Parser.Attr_with_valueContext):
        name = Id(ctx.any_id().getText()) # First variable
        expr = self.visit(ctx.all_expr()) # Last value
        
        a = [name] + [expr] + self.visit(ctx.attr_pair())

        nameList = []
        exprList = []
        dataType = None
        counter = -1
        length = len(a)
        for i in a:
            # even: 0, 2, 4...
            counter += 1
            if (counter % 2 == 0):
                if counter < length - 1:
                    nameList.append(i)
                else:
                    dataType = i
            else:
                exprList.append(i)
        
        returnList = []
        if ctx.VAR(): # VAR()
            for i in range(len(nameList)):
                if '$' in nameList[i].__str__():
                    returnList.append(AttributeDecl(Static().__str__(), VarDecl(nameList[i], dataType, exprList[len(exprList) - i - 1])))
                else:
                    returnList.append(AttributeDecl(Instance().__str__(), VarDecl(nameList[i], dataType, exprList[len(exprList) - i - 1])))
        if ctx.VAL(): # VAL()
            for i in range(len(nameList)):
                if '$' in nameList[i].__str__():
                    returnList.append(AttributeDecl(Static().__str__(), ConstDecl(nameList[i], dataType, exprList[len(exprList) - i - 1])))
                else:
                    returnList.append(AttributeDecl(Instance().__str__(), ConstDecl(nameList[i], dataType, exprList[len(exprList) - i - 1])))
        return returnList

        
    # Visit a parse tree produced by D96Parser#attr_pair.
    # attr_pair: COMMA any_id attr_pair all_expr COMMA | COLON data_type ASSIGN; 
    def visitAttr_pair(self, ctx:D96Parser.Attr_pairContext):
        # COLON data_type ASSIGN
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.data_type())] # Data type, some sort of like Int should be returned here
            
        # COMMA any_id attr_pair all_expr COMMA
        name = Id(self.visit(ctx.any_id()))
        expr = self.visit(ctx.all_expr())
        return [name, expr] + ctx.attr_pair().accept(self)


    # Visit a parse tree produced by D96Parser#attr_array_no_value.
    # attr_array_no_value: (VAR | VAL) any_id (COMMA any_id)* COLON attr_array_decl_tail SEMI;
    # Var arr: Array[Float, 3];
    def visitAttr_array_no_value(self, ctx:D96Parser.Attr_array_no_valueContext):
        attrList = []
        for name in ctx.any_id():
            lst = self.visit(ctx.attr_array_decl_tail())
            data_type = lst[0]
            if '$' in name.getText():
                attrList.append(AttributeDecl(Static().__str__(), VarDecl(Id(name.getText()), self.nested_array(lst, data_type))))
            else:
                attrList.append(AttributeDecl(Instance().__str__(), VarDecl(Id(name.getText()), self.nested_array(lst, data_type))))
        return attrList

    # Helper Function    
    def nested_array(self, lst, data_type):
        lst.pop(0)
        return ArrayType(lst[0], self.nested_array(lst, data_type)) if len(lst) > 0 else data_type


    # Visit a parse tree produced by D96Parser#attr_array_with_value.
    # attr_array_with_value: (VAR | VAL) any_id attr_array_pair array_rhs SEMI; 
    def visitAttr_array_with_value(self, ctx:D96Parser.Attr_array_with_valueContext):
        first_id = Id(ctx.any_id().getText())
        body = self.visit(ctx.attr_array_pair())
        # print(first_id)
        # print(body)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_pair.
    # attr_array_pair: COMMA any_id attr_array_pair array_rhs COMMA | COLON attr_array_decl_tail ASSIGN; 
    def visitAttr_array_pair(self, ctx:D96Parser.Attr_array_pairContext):
        if (ctx.getChildren() == 3):
            self.visit(ctx.attr_array_decl_tail())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_decl_tail.
    # attr_array_decl_tail: ARRAY LS (data_type | attr_array_decl_tail) COMMA (LITERAL_INT) RS;
    def visitAttr_array_decl_tail(self, ctx:D96Parser.Attr_array_decl_tailContext):
        size = IntLiteral(ctx.LITERAL_INT().getText())
        # ARRAY LS data_type COMMA LITERAL_INT RS
        if ctx.data_type(): 
            data_type = self.visit(ctx.data_type())
            return [data_type] + [size]
        # ARRAY LS attr_array_decl_tail COMMA LITERAL_INT RS
        elif ctx.attr_array_decl_tail():
            return ctx.attr_array_decl_tail().accept(self) + [size]


    # Visit a parse tree produced by D96Parser#any_id.
    # any_id: ID | DOLLAR_ID;
    # --> Just need to visit either any ID or DOLLAR_ID, and return ID by getText() cause they are literals
    def visitAny_id(self, ctx:D96Parser.Any_idContext):
        return ctx.getText()


    # Visit a parse tree produced by D96Parser#class_method.
    # class_method: normal_method | constructor | destructor;
    # --> Just need to visit either any method
    def visitClass_method(self, ctx:D96Parser.Class_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normal_method.
    # normal_method: any_id LB params_list? RB LP block_stmt? RP; 
    # Not yet done
    def visitNormal_method(self, ctx:D96Parser.Normal_methodContext):
        id = Id(self.visit(ctx.any_id()))
        kind = Static().__str__() if '$' in id.__str__() else Instance().__str__()
        param = self.visit(ctx.params_list()) if ctx.params_list() else []
        block_stmt = self.visit(ctx.block_stmt()) if ctx.block_stmt() else []
        # print("block_stmt = ", block_stmt)
        # return MethodDecl(kind, id, param, block_stmt)


    # Visit a parse tree produced by D96Parser#constructor.
    # constructor: CONSTRUCTOR LB params_list? RB LP block_stmt? RP; 
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        id = Id('"' + ctx.CONSTRUCTOR().getText() + '"') # Id("Constructor")
        kind = Instance().__str__() # Constructor is always Instance
        param = self.visit(ctx.params_list()) if ctx.params_list() else []
        block_stmt = self.visit(ctx.block_stmt()) if ctx.block_stmt() else []
        # return MethodDecl(kind, id, param, block_stmt)


    # Visit a parse tree produced by D96Parser#destructor.
    # destructor: DESTRUCTOR LB RB LP block_stmt? RP;
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        id = Id('"' + ctx.DESTRUCTOR().getText() + '"') # Id("Destructor")
        kind = Instance().__str__() # Destructor is always Instance
        block_stmt = self.visit(ctx.block_stmt()) if ctx.block_stmt() else []
        #return MethodDecl(kind, id, None, block_stmt)


    # Visit a parse tree produced by D96Parser#stmt.
    # stmt: var_decl | assign_stmt | if_stmt | for_in_stmt | break_stmt | continue_stmt | return_stmt
	# | method_invoc_literal DOT funcall SEMI
	# | (SELF | ID) DOUBLE_COLON static_method SEMI
	# | LP block_stmt? RP 
    def visitStmt(self, ctx:D96Parser.StmtContext):
        # stmt: var_decl | assign_stmt | if_stmt | for_in_stmt | break_stmt | continue_stmt | return_stmt
        print(ctx.getText())
        if ctx.getChildren() == 1:
            if ctx.var_decl(): return self.visit(ctx.var_decl()) # var_decl
            if ctx.assign_stmt(): return self.visit(ctx.assign_stmt()) # assign_stmt
            if ctx.if_stmt(): return self.visit(ctx.if_stmt()) # if_stmt
            if ctx.for_in_stmt(): return self.visit(ctx.for_in_stmt()) # for_in_stmt
            if ctx.break_stmt(): return self.visit(ctx.break_stmt()) # break_stmt
            if ctx.continue_stmt(): return self.visit(ctx.continue_stmt()) # continue_stmt
            return self.visit(ctx.return_stmt()) # return_stmt
        # LP block_stmt? RP 
        if ctx.LP():
            return ctx.visit(ctx.block_stmt())

        # method_invoc_literal DOT funcall SEMI
        # (SELF | ID) DOUBLE_COLON static_method SEMI    
        if ctx.getChildren() == 4:
            pass # Do later


    # Visit a parse tree produced by D96Parser#var_decl.
    # var_decl: var_no_value | var_with_value | var_array_no_value| var_array_with_value;
    def visitVar_decl(self, ctx:D96Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_no_value.
    # var_no_value: (VAR | VAL) ID (COMMA ID)* COLON data_type SEMI;
    def visitVar_no_value(self, ctx:D96Parser.Var_no_valueContext):
        print([Id(x.getText()) for x in ctx.ID()])
        print("a")


    # Visit a parse tree produced by D96Parser#var_with_value.
    # var_with_value: (VAR | VAL) ID var_pair all_expr SEMI; 
    def visitVar_with_value(self, ctx:D96Parser.Var_with_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_pair.
    def visitVar_pair(self, ctx:D96Parser.Var_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_array_no_value.
    def visitVar_array_no_value(self, ctx:D96Parser.Var_array_no_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_array_with_value.
    def visitVar_array_with_value(self, ctx:D96Parser.Var_array_with_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_array_pair.
    def visitVar_array_pair(self, ctx:D96Parser.Var_array_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_array_decl_tail.
    # 
    def visitVar_array_decl_tail(self, ctx:D96Parser.Var_array_decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_rhs.
    # array_rhs: literal_array | object_create all_expr?;
    def visitArray_rhs(self, ctx:D96Parser.Array_rhsContext):
        if ctx.literal_array():
            return self.visit(ctx.literal_array())
        if ctx.object_create():
            if ctx.all_expr():
                expr = self.visit(ctx.all_expr())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    # assign_stmt: assign_lhs ASSIGN all_expr SEMI;
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs.
    # assign_lhs: scalar_variable element_expr?;
    def visitAssign_lhs(self, ctx:D96Parser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params_list.
    # params_list: params (SEMI params)*;
    def visitParams_list(self, ctx:D96Parser.Params_listContext):
        return [self.visitParams(x) for x in ctx.params()]


    # Visit a parse tree produced by D96Parser#params.
    # params : ID ((COMMA ID)* COLON (data_type | var_array_decl_tail)); 
    # a, b: Int | a, b: Array[Int, 5]
    def visitParams(self, ctx:D96Parser.ParamsContext):
        for i in range(len(ctx.ID())):
            #print(ctx.ID(i), ctx.data_type().getText() if ctx.data_type() else self.visit(ctx.var_array_decl_tail()))
            pass
        #return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_type.
    # data_type : INT | FLOAT | BOOLEAN | STRING | ID | SELF;
    def visitData_type(self, ctx:D96Parser.Data_typeContext):
        if ctx.INT(): return IntType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOLEAN(): return BoolType()
        if ctx.STRING(): return StringType()
        if ctx.SELF(): return SelfLiteral()


    # Visit a parse tree produced by D96Parser#if_stmt.
    # if_stmt: IF LB all_expr RB LP block_stmt? RP (else_if_body)? else_body?;
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_if_body.
    # else_if_body: ELSEIF LB all_expr RB LP block_stmt? RP else_if_body?;
    def visitElse_if_body(self, ctx:D96Parser.Else_if_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_body.
    # else_body: ELSE LP block_stmt? RP;
    def visitElse_body(self, ctx:D96Parser.Else_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_stmt.
    # for_in_stmt: FOREACH LB for_in_body RB LP block_stmt? RP;
    def visitFor_in_stmt(self, ctx:D96Parser.For_in_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_body.
    # for_in_body: scalar_variable IN for_in_expr DOTDOT for_in_expr (BY for_in_expr)? ; 
    def visitFor_in_body(self, ctx:D96Parser.For_in_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_expr.
    # for_in_expr: all_expr;
    def visitFor_in_expr(self, ctx:D96Parser.For_in_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_variable.
    # scalar_variable: scalar_variable DOT (ID | funcall)
    # | static_member_access
    # | SELF 
    # | ID 
    # ;
    def visitScalar_variable(self, ctx:D96Parser.Scalar_variableContext):
        # static_member_access | SELF | ID
        if ctx.getChildren() == 1: 
            if ctx.static_member_access():
                return ctx.visit(ctx.static_member_access())
            if ctx.SELF(): return SelfLiteral()
            if ctx.ID(): return Id(ctx.ID().getText())
        
        # scalar_variable DOT (ID | funcall)
        if ctx.getChildren() == 3:
            if ctx.ID(): id = Id(ctx.ID())
            if ctx.funcall(): func = self.visit(ctx.funcall())
            left = self.visit(ctx.scalar_variable())
            return 


    # Visit a parse tree produced by D96Parser#break_stmt.
    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by D96Parser#continue_stmt.
    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by D96Parser#return_stmt.
    # return_stmt: RETURN all_expr* SEMI;
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        expr_list = []
        for x in ctx.all_expr():
            expr = self.visitAll_expr(x)
            if isinstance(expr, list):
                expr_list.extend(expr if expr else [])
            else:
                expr_list.append(expr)
        return Return(expr_list) if len(expr_list) > 0 else Return()


    # Visit a parse tree produced by D96Parser#method_invoc_literal.
    # method_invoc_literal: 
    # method_invoc_literal DOT (ID | funcall) 
    # | NEW funcall // New X().New
    # | method_invoc_literal element_expr
    # | static_member_access
    # | SELF
    # | ID
    # ;
    def visitMethod_invoc_literal(self, ctx:D96Parser.Method_invoc_literalContext):
        # SELF | ID | static_member_access
        if ctx.getChildren() == 1:
            if ctx.SELF(): return SelfLiteral()
            if ctx.ID(): return Id(ctx.ID().getText())
            if ctx.static_member_access(): return self.visit(ctx.static_member_access())

        # method_invoc_literal element_expr | NEW funcall 
        if ctx.getChildren() == 2:
            pass
        
        # method_invoc_literal DOT (ID | funcall) 
        if ctx.getChildren() == 3:
            if ctx.ID():
                id = Id(ctx.ID().getText())
            

    # Visit a parse tree produced by D96Parser#expr_list.
    # expr_list: (all_expr COMMA)* all_expr;
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return [self.visitAll_expr(x) for x in ctx.all_expr()]


    # Visit a parse tree produced by D96Parser#funcall.
    # funcall: ID LB list_of_expr? RB;
    def visitFuncall(self, ctx:D96Parser.FuncallContext):
        # id = Id(ctx.ID().getText())
        # expr_list = self.visit(ctx.list_of_expr())
        # return CallStmt(self, id, expr_list)

        # do later
        pass 


    # Visit a parse tree produced by D96Parser#block_stmt.
    # block_stmt: stmt+;
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        stmtList = []
        for x in ctx.stmt():
            stmt = self.visitStmt(x)
            if isinstance(stmt, list):
                stmtList.extend(stmt if stmt else [])
            else:
                stmtList.append(stmt)
        return stmtList


    # Visit a parse tree produced by D96Parser#all_expr.
    # all_expr: (op | object_create); --> Hợp lý
    def visitAll_expr(self, ctx:D96Parser.All_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op.
    # op: op1 (STRING_CONCAT | EQUAL_STRING) op1 | op1; // +., ==., - Binary - Infix - None
    def visitOp(self, ctx:D96Parser.OpContext):
        if ctx.getChildCount() == 1: # op1
            return self.visit(ctx.op1(0))
        left = self.visit(ctx.op1(0))
        right = self.visit(ctx.op1(1))
        op = '+.' if ctx.STRING_CONCAT() else '==.'

        return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#op1.
    # op1: op2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LEQ | GEQ) op2 | op2; // ==, !=, <, >, <, =< >= - Binary - Infix - None
    def visitOp1(self, ctx:D96Parser.Op1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op2(0))
        left = self.visit(ctx.op2(0))
        right = self.visit(ctx.op2(1))
        op = op = ctx.getChild(1).getText()

        return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#op2.
    # op2: op2 (AND | OR) op3 | op3; // &&, || - Binary - Infix - Left-assoc
    def visitOp2(self, ctx:D96Parser.Op2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op3())
        left = self.visit(ctx.op2())
        right = self.visit(ctx.op3())
        op = '&&' if ctx.AND() else '||'

        return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#op3.
    # op3: op3 (ADD | SUBTRACT) op4 | op4; // +, - - Binary - Infix - Left-assoc
    def visitOp3(self, ctx:D96Parser.Op3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op4())
        left = self.visit(ctx.op3())
        right = self.visit(ctx.op4())
        op = '+' if ctx.ADD() else '-'

        return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#op4.
    # op4: op4 (MULTIPLY | DIVIDE | MODULO) op5 | op5 ; // *, /, % - Binary - Infix - Left-assoc
    def visitOp4(self, ctx:D96Parser.Op4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op5())
        left = self.visit(ctx.op4())
        right = self.visit(ctx.op5())
        op = ctx.getChild(1).getText()

        return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#op5.
    # op5: (NOT op5) | op6; // ! -  Unary - Prefix - Right-assoc
    def visitOp5(self, ctx:D96Parser.Op5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op6())
        op = '!'
        body = self.visit(ctx.op5())
        return UnaryOp(op, body)


    # Visit a parse tree produced by D96Parser#op6.
    # op6: (SUBTRACT op6) | op7; // (-) - Unary - Prefix - Right-assoc
    def visitOp6(self, ctx:D96Parser.Op6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op7())
        op = '-'
        body = self.visit(ctx.op6())
        return UnaryOp(op, body)


    # Visit a parse tree produced by D96Parser#op7.
    # op7: op7 LS op7 RS | op8 ; // [] - Unary - Postfix - Left-assoc
    def visitOp7(self, ctx:D96Parser.Op7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op8())
        left = self.visit(ctx.op7(0))
        index = self.visit(ctx.op7(1))

        return
        pass # ArrayCell


    # Visit a parse tree produced by D96Parser#op8.
    # op8: op8 DOT (ID | funcall) | op9; // . - Binary - Infix - Left-assoc
    def visitOp8(self, ctx:D96Parser.Op8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op9())
        left = self.visit(ctx.op8())

        if ctx.ID(): return ctx.ID().getText()
        elif ctx.funcall(): func = self.visit(ctx.funcall())

        return


    # Visit a parse tree produced by D96Parser#op9.
    # op9: (SELF | ID) DOUBLE_COLON (static_method | DOLLAR_ID) | op10; 
    def visitOp9(self, ctx:D96Parser.Op9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op10()) 

        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op10.
    # op10: (NEW operands LB list_of_expr? RB) | operands; // New - Unary - Prefix - Right-assoc
    def visitOp10(self, ctx:D96Parser.Op10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands()) 

        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    # operands: literal | SELF | ID | LB op RB | NULL | literal_array; // Because member access can also return a value
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        # literal | SELF | ID | NULL | literal_array;
        if ctx.getChildCount() == 1:
            if ctx.SELF(): return SelfLiteral()
            if ctx.ID(): return Id(ctx.ID().getText())
            if ctx.NULL(): return NullLiteral()
            if ctx.literal(): return self.visit(ctx.literal())
            if ctx.literal_array(): return self.visit(ctx.literal_array())
        # LB op RB 
        if ctx.LB():
            return self.visit(ctx.op())


    # Visit a parse tree produced by D96Parser#element_expr.
    def visitElement_expr(self, ctx:D96Parser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_ops.
    def visitIndex_ops(self, ctx:D96Parser.Index_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_member_access.
    # static_member_access: (SELF | ID) DOUBLE_COLON (DOLLAR_ID | static_method);
    # Self::$a or Self::$a() or Self::$a(b) or Self::$a(b, c)
    # x::$a or x::$a() or x::$a(b) or x::$a(b, c)
    def visitStatic_member_access(self, ctx:D96Parser.Static_member_accessContext):
        id = SelfLiteral() if ctx.SELF() else Id(ctx.ID().getText())
        right = Id(ctx.DOLLAR_ID().getText()) if ctx.DOLLAR_ID() else self.visit(ctx.static_method())
        return Call
        # return "Call(" + str(self.obj) + "," + str(self.method) + ",[" + ','.join(str(i) for i in self.param) + "])"

    # Visit a parse tree produced by D96Parser#static_method.
    # static_method: DOLLAR_ID LB list_of_expr? RB; --> $a() / $a(b) / $a(b, c)
    def visitStatic_method(self, ctx:D96Parser.Static_methodContext):
        return [ctx.DOLLAR_ID.getText(), ctx.list_of_expr() if ctx.list_of_expr() else [] ]


    # Visit a parse tree produced by D96Parser#object_create.
    # object_create: NEW ID LB list_of_expr? RB;
    def visitObject_create(self, ctx:D96Parser.Object_createContext):
        id = Id(ctx.ID().getText())
        param = self.visit(ctx.list_of_expr()) if ctx.list_of_expr() else []
        return NewExpr(id, param)


    # Visit a parse tree produced by D96Parser#list_of_expr.
    # list_of_expr: op (COMMA op)*;
    def visitList_of_expr(self, ctx:D96Parser.List_of_exprContext):
        return [self.visitOp(x) for x in ctx.op()]


    # Visit a parse tree produced by D96Parser#literal.
    # literal: LITERAL_INT | LITERAL_FLOAT | LITERAL_STRING | LITERAL_BOOLEAN | LITERAL_ZERO;
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        if ctx.LITERAL_INT():
            return IntLiteral(ctx.LITERAL_INT().getText())
        if ctx.LITERAL_FLOAT():
            return FloatLiteral(ctx.LITERAL_FLOAT().getText())
        if ctx.LITERAL_STRING():
            return StringLiteral(ctx.LITERAL_STRING().getText())
        if ctx.LITERAL_BOOLEAN():
            return BooleanLiteral(ctx.LITERAL_BOOLEAN().getText())
        if ctx.LITERAL_ZERO():
            return IntLiteral(ctx.LITERAL_ZERO().getText())

    # Visit a parse tree produced by D96Parser#literal_array.
    # literal_array: literal_idx_array | literal_mtd_array;
    # --> Let the visitor choose the path
    def visitLiteral_array(self, ctx:D96Parser.Literal_arrayContext):
        return self.visitChildren(ctx) 
    # Children: visitLiteral_idx_array
    # Children: visitLiteral_mtd_array

    # class ArrayLiteral(Literal):
    #     value: List[Literal]

    #     def __str__(self):
    #         return '[' + ','.join(str(i) for i in self.value) + ']'

    # Visit a parse tree produced by D96Parser#literal_idx_array.
    # literal_idx_array: ARRAY LB array_element? RB;
    def visitLiteral_idx_array(self, ctx:D96Parser.Literal_idx_arrayContext):
        array_element = ctx.array_element() if ctx.array_element() else []
        return ArrayLiteral(array_element)


    # Visit a parse tree produced by D96Parser#literal_mtd_array.
    # literal_mtd_array: ARRAY LB literal_idx_array (COMMA literal_idx_array)* RB;
    def visitLiteral_mtd_array(self, ctx:D96Parser.Literal_mtd_arrayContext):
        return [self.literal_idx_array(x) for x in ctx.literal_idx_array()]


    # Visit a parse tree produced by D96Parser#array_element.
    # array_element: all_expr (COMMA all_expr)*;
    def visitArray_element(self, ctx:D96Parser.Array_elementContext):
        return [self.visitAll_expr(x) for x in ctx.all_expr()]