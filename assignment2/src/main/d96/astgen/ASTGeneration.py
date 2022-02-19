# Generate Abstract Syntax Tree from a parse tree generated from ANTLR

from dataclasses import Field
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

### Remember to uncomment this mess before submit to BKEL ###
from main.d96.utils.AST import ArrayCell, ArrayLiteral, Assign, AttributeDecl, BinaryOp, Block, BoolType, BooleanLiteral, Break, CallExpr, ClassDecl, ClassType, ConstDecl, Continue, FieldAccess, For, If, MethodDecl, NewExpr, NullLiteral, Return
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
            if ctx.ID(0).getText() == 'Program':
                member = self.visitClass_body(x, 1)
            if ctx.ID(0).getText() != 'Program':
                member = self.visitClass_body(x)
            if isinstance(member, list):
                memberList.extend(member if member else [])
            else:
                memberList.append(member)
        return ClassDecl(name, memberList, parent) 


    # Visit a parse tree produced by D96Parser#class_body.
    # class_body: class_attr | class_method;
    # --> Just need to visit either of class member
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext, idx = None):
        # Not program
        if not idx: 
            return self.visitChildren(ctx)
        # Program
        else:
            if ctx.class_attr():
                return self.visit(ctx.class_attr())
            # Program and main
            if ctx.class_method():
                if ctx.class_method().normal_method():
                    return self.visitNormal_method(ctx.class_method().normal_method(), 1)
                if ctx.class_method().constructor():
                    return self.visitConstructor(ctx.class_method().constructor())
                if ctx.class_method().destructor():
                    return self.visitDestructor(ctx.class_method().destructor())
                


    # Visit a parse tree produced by D96Parser#class_attr.
    # class_attr: attr_no_value | attr_with_value | attr_array_no_value | attr_array_with_value;
    # --> Just need to visit either any attribute
    def visitClass_attr(self, ctx:D96Parser.Class_attrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by D96Parser#attr_no_value.
    # attr_no_value: (VAR | VAL) any_id (COMMA any_id)* COLON data_type SEMI;
    def visitAttr_no_value(self, ctx:D96Parser.Attr_no_valueContext):
        attrList = []
        for name in ctx.any_id():
            if ctx.VAR():
                if '$' in name.getText(): 
                    attrList.append(AttributeDecl(Static().__str__(), VarDecl(Id(name.getText()), self.visit(ctx.data_type()))))
                else: attrList.append(AttributeDecl(Instance().__str__(), VarDecl(Id(name.getText()), self.visit(ctx.data_type()))))
            if ctx.VAL():
                if '$' in name.getText(): 
                    attrList.append(AttributeDecl(Static().__str__(), ConstDecl(Id(name.getText()), self.visit(ctx.data_type()))))
                else: attrList.append(AttributeDecl(Instance().__str__(), ConstDecl(Id(name.getText()), self.visit(ctx.data_type()))))
        return attrList


    # Visit a parse tree produced by D96Parser#attr_with_value.
    # attr_with_value: (VAR | VAL) any_id attr_pair all_expr SEMI;
    def visitAttr_with_value(self, ctx:D96Parser.Attr_with_valueContext):
        nameList = [Id(self.visit(ctx.any_id()))] # First variable --> nameList = [first_var]
        exprList = []
        
        body = self.visit(ctx.attr_pair())
        size = len(body)

        for i in range(size):
            if i is not size - 1:
                if i % 2 == 0:
                    nameList.append(body[i])
                else:
                    exprList.append(body[size - i - 1])
            else: 
                data_type = body[i]
        exprList.append(self.visit(ctx.all_expr()))

        returnList = []
        if ctx.VAR(): # VAR()
            for i in range(len(nameList)):
                if '$' in nameList[i].__str__():
                    returnList.append(AttributeDecl(Static().__str__(), VarDecl(nameList[i], data_type, exprList[i])))
                else:
                    returnList.append(AttributeDecl(Instance().__str__(), VarDecl(nameList[i], data_type, exprList[i])))
        if ctx.VAL(): # VAL()
            for i in range(len(nameList)):
                if '$' in nameList[i].__str__():
                    returnList.append(AttributeDecl(Static().__str__(), ConstDecl(nameList[i], data_type, exprList[i])))
                else:
                    returnList.append(AttributeDecl(Instance().__str__(), ConstDecl(nameList[i], data_type, exprList[i])))
        return returnList

        
    # Visit a parse tree produced by D96Parser#attr_pair.
    # attr_pair: COMMA any_id attr_pair all_expr COMMA | COLON data_type ASSIGN; 
    def visitAttr_pair(self, ctx:D96Parser.Attr_pairContext):
        # COLON data_type ASSIGN
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.data_type())] 
            # Data type, some sort of like Int should be returned here, and will be appended to the end of the list
            
        # COMMA any_id attr_pair all_expr COMMA
        name = Id(self.visit(ctx.any_id()))
        expr = self.visit(ctx.all_expr())
        return [name, expr] + self.visit(ctx.attr_pair())


    # Visit a parse tree produced by D96Parser#attr_array_no_value.
    # attr_array_no_value: (VAR | VAL) any_id (COMMA any_id)* COLON attr_array_decl_tail SEMI;
    def visitAttr_array_no_value(self, ctx:D96Parser.Attr_array_no_valueContext):
        attrList = []
        if ctx.VAR():
            for name in ctx.any_id():
                if '$' in name.getText():
                    attrList.append(AttributeDecl(Static().__str__(), VarDecl(Id(name.getText()), self.visit(ctx.attr_array_decl_tail()))))
                else:
                    attrList.append(AttributeDecl(Instance().__str__(), VarDecl(Id(name.getText()), self.visit(ctx.attr_array_decl_tail()))))
        if ctx.VAL():
            for name in ctx.any_id():
                if '$' in name.getText():
                    attrList.append(AttributeDecl(Static().__str__(), ConstDecl(Id(name.getText()), self.visit(ctx.attr_array_decl_tail()))))
                else:
                    attrList.append(AttributeDecl(Instance().__str__(), ConstDecl(Id(name.getText()), self.visit(ctx.attr_array_decl_tail()))))
        return attrList


    # Visit a parse tree produced by D96Parser#attr_array_with_value.
    # attr_array_with_value: (VAR | VAL) any_id attr_array_pair array_rhs SEMI; 
    def visitAttr_array_with_value(self, ctx:D96Parser.Attr_array_with_valueContext):
        nameList = [Id(self.visit(ctx.any_id()))] # First variable --> nameList = [first_var]
        exprList = []
        
        body = self.visit(ctx.attr_array_pair())
        size = len(body)

        for i in range(size):
            if i is not size - 1:
                if i % 2 == 0:
                    nameList.append(body[i])
                else:
                    exprList.append(body[size - i - 1])
            else: 
                data_type = body[i]
        exprList.append(self.visit(ctx.array_rhs()))

        returnList = []
        if ctx.VAR(): # VAR()
            for i in range(len(nameList)):
                if '$' in nameList[i].__str__():
                    returnList.append(AttributeDecl(Static().__str__(), VarDecl(nameList[i], data_type, exprList[i])))
                else:
                    returnList.append(AttributeDecl(Instance().__str__(), VarDecl(nameList[i], data_type, exprList[i])))
        if ctx.VAL(): # VAL()
            for i in range(len(nameList)):
                if '$' in nameList[i].__str__():
                    returnList.append(AttributeDecl(Static().__str__(), ConstDecl(nameList[i], data_type, exprList[i])))
                else:
                    returnList.append(AttributeDecl(Instance().__str__(), ConstDecl(nameList[i], data_type, exprList[i])))
        return returnList


    # Visit a parse tree produced by D96Parser#attr_array_pair.
    # attr_array_pair: COMMA any_id attr_array_pair array_rhs COMMA | COLON attr_array_decl_tail ASSIGN; 
    def visitAttr_array_pair(self, ctx:D96Parser.Attr_array_pairContext):
        # COLON attr_array_decl_tail ASSIGN
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.attr_array_decl_tail())] 
            # Array declaration data type, some sort of like Int should be returned here, and will be appended to the end of the list
            
        # COMMA any_id attr_array_pair array_rhs COMMA
        name = Id(self.visit(ctx.any_id()))
        rhs = self.visit(ctx.array_rhs())
        return [name, rhs] + self.visit(ctx.attr_array_pair())


    # Visit a parse tree produced by D96Parser#attr_array_decl_tail.
    # attr_array_decl_tail: ARRAY LS (data_type | attr_array_decl_tail) COMMA LITERAL_INT RS;
    def visitAttr_array_decl_tail(self, ctx:D96Parser.Attr_array_decl_tailContext):
        if ctx.data_type():
            return ArrayType(self.checkBase(ctx.LITERAL_INT().getText()), self.visit(ctx.data_type()))

        # var_array_decl_tail: ARRAY LS var_array_decl_tail COMMA LITERAL_INT RS;
        if ctx.attr_array_decl_tail():
            return ArrayType(self.checkBase(ctx.LITERAL_INT().getText()), self.visit(ctx.attr_array_decl_tail()))


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
    def visitNormal_method(self, ctx:D96Parser.Normal_methodContext, idx = None):
        id = self.visit(ctx.any_id())
        kind = Instance().__str__()
        param = self.visit(ctx.params_list()) if ctx.params_list() else []

        # Program
        if idx:
            if (id.__str__() == "main" and param == []) or '$' in id.__str__():
                kind = Static().__str__() 
        # Not program
        else: 
            if '$' in id.__str__():
                kind = Static().__str__()

        block_stmt = self.visit(ctx.block_stmt()) if ctx.block_stmt() else []
        return MethodDecl(kind, Id(id), param, Block(block_stmt))


    # Visit a parse tree produced by D96Parser#constructor.
    # constructor: CONSTRUCTOR LB params_list? RB LP block_stmt? RP; 
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        id = Id('"' + ctx.CONSTRUCTOR().getText() + '"') # Id("Constructor")
        kind = Instance().__str__() # Constructor is always Instance
        param = self.visit(ctx.params_list()) if ctx.params_list() else []
        block_stmt = self.visit(ctx.block_stmt()) if ctx.block_stmt() else []
        return MethodDecl(kind, id, param, Block(block_stmt))


    # Visit a parse tree produced by D96Parser#destructor.
    # destructor: DESTRUCTOR LB RB LP block_stmt? RP;
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        id = Id('"' + ctx.DESTRUCTOR().getText() + '"') # Id("Destructor")
        kind = Instance().__str__() # Destructor is always Instance
        block_stmt = self.visit(ctx.block_stmt()) if ctx.block_stmt() else []
        return MethodDecl(kind, id, [], Block(block_stmt))


    # Visit a parse tree produced by D96Parser#stmt.
    # stmt: var_decl | assign_stmt | if_stmt | for_in_stmt 
    # | break_stmt | continue_stmt | return_stmt | method_invoc | static_method_invoc | block_stmt_stmt
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_decl.
    # var_decl: var_no_value | var_with_value | var_array_no_value | var_array_with_value;
    def visitVar_decl(self, ctx:D96Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_no_value.
    # var_no_value: (VAR | VAL) ID (COMMA ID)* COLON data_type SEMI;
    def visitVar_no_value(self, ctx:D96Parser.Var_no_valueContext):
        attrList = []
        for name in ctx.ID():
            if ctx.VAR():
                attrList.append(VarDecl(Id(name.getText()), self.visit(ctx.data_type())))
            elif ctx.VAL():
                attrList.append(ConstDecl(Id(name.getText()), self.visit(ctx.data_type())))
        return attrList


    # Visit a parse tree produced by D96Parser#var_with_value.
    # var_with_value: (VAR | VAL) ID var_pair all_expr SEMI; 
    def visitVar_with_value(self, ctx:D96Parser.Var_with_valueContext):
        nameList = [Id(ctx.ID().getText())] # First variable --> nameList = [first_var]
        exprList = []
        
        body = self.visit(ctx.var_pair())
        size = len(body)

        for i in range(size):
            if i is not size - 1:
                if i % 2 == 0:
                    nameList.append(body[i])
                else:
                    exprList.append(body[size - i - 1])
            else: 
                data_type = body[i]
        exprList.append(self.visit(ctx.all_expr()))

        returnList = []
        if ctx.VAR(): # VAR()
            for i in range(len(nameList)):
                if '$' in nameList[i].__str__():
                    returnList.append(VarDecl(nameList[i], data_type, exprList[i]))
                else:
                    returnList.append(VarDecl(nameList[i], data_type, exprList[i]))
        if ctx.VAL(): # VAL()
            for i in range(len(nameList)):
                if '$' in nameList[i].__str__():
                    returnList.append(ConstDecl(nameList[i], data_type, exprList[i]))
                else:
                    returnList.append(ConstDecl(nameList[i], data_type, exprList[i]))
        return returnList


    # Visit a parse tree produced by D96Parser#var_pair.
    # var_pair: COMMA ID var_pair all_expr COMMA | COLON data_type ASSIGN; 
    def visitVar_pair(self, ctx:D96Parser.Var_pairContext):
        # COLON data_type ASSIGN
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.data_type())] 
            # Data type, some sort of like Int should be returned here, and will be appended to the end of the list
            
        # COMMA any_id attr_pair all_expr COMMA
        name = Id(ctx.ID().getText())
        expr = self.visit(ctx.all_expr())
        return [name, expr] + self.visit(ctx.var_pair())


    # Visit a parse tree produced by D96Parser#var_array_no_value.
    # var_array_no_value: (VAR | VAL) ID (COMMA ID)* COLON var_array_decl_tail SEMI;
    def visitVar_array_no_value(self, ctx:D96Parser.Var_array_no_valueContext):
        attrList = []
        for name in ctx.ID():
            if ctx.VAR():
                attrList.append(VarDecl(Id(name.getText()), self.visit(ctx.var_array_decl_tail())))
            if ctx.VAL():
                attrList.append(ConstDecl(Id(name.getText()), self.visit(ctx.var_array_decl_tail())))
        return attrList


    # Visit a parse tree produced by D96Parser#var_array_with_value.
    # var_array_with_value: (VAR | VAL) ID var_array_pair array_rhs SEMI; 
    def visitVar_array_with_value(self, ctx:D96Parser.Var_array_with_valueContext):
        nameList = [Id(ctx.ID().getText())] # First variable --> nameList = [first_var]
        exprList = []
        
        body = self.visit(ctx.var_array_pair())
        size = len(body)

        for i in range(size):
            if i is not size - 1:
                if i % 2 == 0:
                    nameList.append(body[i])
                else:
                    exprList.append(body[size - i - 1])
            else: 
                data_type = body[i]
        exprList.append(self.visit(ctx.array_rhs()))

        returnList = []
        for i in range(len(nameList)):
            if ctx.VAR(): # VAR()
                returnList.append(VarDecl(nameList[i], data_type, exprList[i]))
            if ctx.VAL(): # VAL()
                returnList.append(ConstDecl(nameList[i], data_type, exprList[i]))
        return returnList


    # Visit a parse tree produced by D96Parser#var_array_pair.
    # var_array_pair: COMMA ID var_array_pair array_rhs COMMA | COLON var_array_decl_tail ASSIGN; 
    def visitVar_array_pair(self, ctx:D96Parser.Var_array_pairContext):
        # COLON var_array_decl_tail ASSIGN
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.var_array_decl_tail())] 
            # Array declaration data type, some sort of like Int should be returned here, and will be appended to the end of the list
            
        # COMMA ID var_array_pair array_rhs COMMA
        name = Id(ctx.ID().getText())
        rhs = self.visit(ctx.array_rhs())
        return [name, rhs] + self.visit(ctx.var_array_pair())


    # Visit a parse tree produced by D96Parser#var_array_decl_tail.
    # var_array_decl_tail: ARRAY LS (data_type | var_array_decl_tail) COMMA LITERAL_INT RS;
    def visitVar_array_decl_tail(self, ctx:D96Parser.Var_array_decl_tailContext):
        # var_array_decl_tail: ARRAY LS data_type COMMA LITERAL_INT RS;
        if ctx.data_type():
            return ArrayType(self.checkBase(ctx.LITERAL_INT().getText()), self.visit(ctx.data_type()))

        # var_array_decl_tail: ARRAY LS var_array_decl_tail COMMA LITERAL_INT RS;
        if ctx.var_array_decl_tail():
            return ArrayType(self.checkBase(ctx.LITERAL_INT().getText()), self.visit(ctx.var_array_decl_tail()))


    # Visit a parse tree produced by D96Parser#array_rhs.
    # array_rhs: literal_array | object_create;
    def visitArray_rhs(self, ctx:D96Parser.Array_rhsContext):
        return self.visitChildren(ctx)
    

    # Visit a parse tree produced by D96Parser#assign_stmt.
    # assign_stmt: assign_lhs ASSIGN all_expr SEMI;
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        lhs = self.visit(ctx.assign_lhs())
        expr = self.visit(ctx.all_expr())
        return Assign(lhs, expr)


    # Visit a parse tree produced by D96Parser#assign_lhs.
    # assign_lhs: scalar_variable
    # assign_lhs: scalar_variable element_expr
    def visitAssign_lhs(self, ctx:D96Parser.Assign_lhsContext):
        scalar = self.visit(ctx.scalar_variable())
        if ctx.element_expr():
            ele_expr = self.visit(ctx.element_expr())
            return ArrayCell(scalar, ele_expr)
        return scalar # else return scalar_variable only


    # Visit a parse tree produced by D96Parser#params_list.
    # params_list: params (SEMI params)*;
    def visitParams_list(self, ctx:D96Parser.Params_listContext):
        paramsList = []
        for x in ctx.params():
            paramsList = paramsList + self.visitParams(x)
        return paramsList

    # Visit a parse tree produced by D96Parser#params.
    # params : ID (COMMA ID)* COLON (data_type | var_array_decl_tail); 
    def visitParams(self, ctx:D96Parser.ParamsContext):
        paramsList = []
        for i in ctx.ID():
            if ctx.data_type():
                paramsList.append(VarDecl(Id(i.getText()), self.visit(ctx.data_type())))
            if ctx.var_array_decl_tail():
                paramsList.append(VarDecl(Id(i.getText()), self.visit(ctx.var_array_decl_tail())))
        return paramsList


    # Visit a parse tree produced by D96Parser#data_type.
    # data_type : INT | FLOAT | BOOLEAN | STRING | ID | SELF;
    def visitData_type(self, ctx:D96Parser.Data_typeContext):
        if ctx.INT(): return IntType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOLEAN(): return BoolType()
        if ctx.STRING(): return StringType()
        if ctx.ID(): return ClassType(Id(ctx.ID().getText()))
        if ctx.SELF(): return SelfLiteral()


    # Visit a parse tree produced by D96Parser#if_stmt.
    # if_stmt: IF LB all_expr RB LP block_stmt? RP (else_if_body | else_body)?
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        expr = self.visit(ctx.all_expr())
        block_stmt = Block(self.visit(ctx.block_stmt())) if ctx.block_stmt() else Block([])

        # IF LB all_expr RB LP block_stmt? RP else_if_body
        if ctx.else_if_body():
            else_if_body = self.visit(ctx.else_if_body())
            return If(expr, block_stmt, else_if_body)
        # IF LB all_expr RB LP block_stmt? RP else_body
        if ctx.else_body():
            else_body = self.visit(ctx.else_body())
            return If(expr, block_stmt, else_body)
        # IF LB all_expr RB LP block_stmt? RP
        return If(expr, block_stmt)

    # Visit a parse tree produced by D96Parser#else_if_body.
    # else_if_body: ELSEIF LB all_expr RB LP block_stmt? RP (else_if_body | else_body)?
    def visitElse_if_body(self, ctx:D96Parser.Else_if_bodyContext):
        expr = self.visit(ctx.all_expr())
        block_stmt = Block(self.visit(ctx.block_stmt())) if ctx.block_stmt() else Block([])

        # ELSEIF LB all_expr RB LP block_stmt? RP else_if_body
        if ctx.else_if_body():
            else_if_body = self.visit(ctx.else_if_body())
            return If(expr, block_stmt, else_if_body)
        if ctx.else_body():
            else_body = self.visit(ctx.else_body())
            return If(expr, block_stmt, else_body)
        
        # ELSEIF LB all_expr RB LP block_stmt? RP
        return If(expr, block_stmt)


    # Visit a parse tree produced by D96Parser#else_body.
    # else_body: ELSE LP block_stmt? RP;
    def visitElse_body(self, ctx:D96Parser.Else_bodyContext):
        return Block(self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by D96Parser#for_in_stmt.
    # for_in_stmt: FOREACH LB for_in_body RB LP block_stmt? RP;
    def visitFor_in_stmt(self, ctx:D96Parser.For_in_stmtContext):
        id, expr1, expr2, expr3 = self.visit(ctx.for_in_body())
        stmt = Block(self.visit(ctx.block_stmt())) if ctx.block_stmt() else Block([])
        return For(id, expr1, expr2, stmt, expr3)


    # Visit a parse tree produced by D96Parser#for_in_body.
    # for_in_body: scalar_variable IN for_in_expr DOTDOT for_in_expr (BY for_in_expr)? ; 
    def visitFor_in_body(self, ctx:D96Parser.For_in_bodyContext):
        id = self.visit(ctx.scalar_variable()) # Limited to id for assignment 2
        expr1 = self.visit(ctx.for_in_expr(0)) # Start
        expr2 = self.visit(ctx.for_in_expr(1)) # End
        expr3 = self.visit(ctx.for_in_expr(2)) if ctx.for_in_expr(2) else IntLiteral(int(1)) # Range (1 if not specified)
        return id, expr1, expr2, expr3


    # Visit a parse tree produced by D96Parser#for_in_expr.
    # for_in_expr: all_expr;
    def visitFor_in_expr(self, ctx:D96Parser.For_in_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_variable.
    # scalar_variable: scalar_variable DOT (ID | funcall)
    # | static_member_access | SELF | ID 
    def visitScalar_variable(self, ctx:D96Parser.Scalar_variableContext):
        # static_member_access | SELF | ID
        if ctx.getChildCount() == 1: 
            if ctx.static_member_access():
                return self.visit(ctx.static_member_access())
            if ctx.SELF(): return SelfLiteral()
            if ctx.ID(): return Id(ctx.ID().getText())
        
        # scalar_variable DOT (ID | funcall)
        if ctx.getChildCount() == 3:
            obj = self.visit(ctx.scalar_variable())
            if ctx.ID(): 
                id = Id(ctx.ID().getText())
                return FieldAccess(obj, id)
            if ctx.funcall(): # return id, exprList
                id, exprList = self.visit(ctx.funcall())
                return CallExpr(obj, id, exprList)


    # Visit a parse tree produced by D96Parser#break_stmt.
    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by D96Parser#continue_stmt.
    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by D96Parser#return_stmt.
    # return_stmt: RETURN all_expr? SEMI;
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        # RETURN SEMI
        if ctx.getChildCount() == 2:
            return Return()
        # RETURN all_expr SEMI
        expr = self.visit(ctx.all_expr())
        return Return(expr)

    # Visit a parse tree produced by D96Parser#method_invoc.
    # method_invoc: method_invoc_literal DOT funcall SEMI;
    def visitMethod_invoc(self, ctx:D96Parser.Method_invocContext):
        obj = self.visit(ctx.method_invoc_literal())
        id, paramList = self.visit(ctx.funcall())
        return CallStmt(obj, id, paramList)


    # Visit a parse tree produced by D96Parser#static_method_invoc.
    # static_method_invoc: (SELF | ID) DOUBLE_COLON static_method SEMI;
    def visitStatic_method_invoc(self, ctx:D96Parser.Static_method_invocContext):
        obj = SelfLiteral() if ctx.SELF() else Id(ctx.ID().getText())
        id, paramList = self.visit(ctx.static_method())
        return CallStmt(obj, id, paramList)


    # Visit a parse tree produced by D96Parser#block_stmt_stmt.
    # block_stmt_stmt: LP block_stmt? RP;
    def visitBlock_stmt_stmt(self, ctx:D96Parser.Block_stmt_stmtContext):
        return Block(self.visit(ctx.block_stmt())) if ctx.block_stmt() else Block([])


    # Visit a parse tree produced by D96Parser#method_invoc_literal.
    # method_invoc_literal: 
    # method_invoc_literal DOT (ID | funcall) 
    # | NEW funcall | method_invoc_literal element_expr
    # | static_member_access | SELF | ID
    def visitMethod_invoc_literal(self, ctx:D96Parser.Method_invoc_literalContext):
        # SELF | ID | static_member_access
        if ctx.getChildCount() == 1:
            if ctx.SELF(): return SelfLiteral()
            if ctx.ID(): return Id(ctx.ID().getText())
            if ctx.static_member_access(): return self.visit(ctx.static_member_access())

        # method_invoc_literal element_expr | NEW funcall 
        if ctx.getChildCount() == 2:
            # method_invoc_literal element_expr
            if ctx.method_invoc_literal(): 
                arr = self.visit(ctx.method_invoc_literal()) 
                idx = self.visit(ctx.element_expr())
                return ArrayCell(arr, idx)
            # NEW funcall 
            if ctx.funcall(): 
                id, exprList = self.visit(ctx.funcall())
                return NewExpr(id, exprList)
        
        # method_invoc_literal DOT (ID | funcall) 
        # ID.ID or ID.funcall
        if ctx.getChildCount() == 3:
            obj = self.visit(ctx.method_invoc_literal())
            if ctx.ID():
                id = Id(ctx.ID().getText())
                return FieldAccess(obj, id)
            if ctx.funcall():
                id, exprList = self.visit(ctx.funcall())
                return CallExpr(obj, id, exprList)
            

    # Visit a parse tree produced by D96Parser#expr_list.
    # expr_list: (all_expr COMMA)* all_expr;
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return [self.visitAll_expr(x) for x in ctx.all_expr()]


    # Visit a parse tree produced by D96Parser#funcall.
    # funcall: ID LB list_of_expr? RB;
    def visitFuncall(self, ctx:D96Parser.FuncallContext):
        id = Id(ctx.ID().getText())
        exprList = self.visit(ctx.list_of_expr()) if ctx.list_of_expr() else []
        return id, exprList


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
    # all_expr: op | object_create; --> Hợp lý
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
        op = ctx.getChild(1).getText()

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
    # op7: op7 postfix_array_exp+ | op8;
    def visitOp7(self, ctx:D96Parser.Op7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op8())

        # op7 postfix_array_exp+
        left = self.visit(ctx.op7())
        exprList = []
        for x in ctx.postfix_array_exp():
            decl = self.visitPostfix_array_exp(x)
            if isinstance(decl, list):
                exprList.extend(decl if decl else [])
            else:
                exprList.append(decl)
        return ArrayCell(left, exprList)


    # postfix_array_exp: LS all_expr RS
    def visitPostfix_array_exp(self, ctx:D96Parser.Postfix_array_expContext):
        return self.visit(ctx.all_expr())


    # Visit a parse tree produced by D96Parser#op8.
    # op8: op8 DOT (ID | funcall) | op9; // . - Binary - Infix - Left-assoc
    def visitOp8(self, ctx:D96Parser.Op8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op9())
        
        obj = self.visit(ctx.op8())
        if ctx.ID(): 
            return FieldAccess(obj, Id(ctx.ID().getText()))
        elif ctx.funcall(): 
            id, exprList = self.visit(ctx.funcall())
            return CallExpr(obj, id, exprList)


    # Visit a parse tree produced by D96Parser#op9.
    # op9: (SELF | ID) DOUBLE_COLON (static_method | DOLLAR_ID) | op10
    def visitOp9(self, ctx:D96Parser.Op9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.op10()) 

        if ctx.SELF(): obj = SelfLiteral() 
        if ctx.ID(): obj = Id(ctx.ID().getText())

        if ctx.static_method():
            id, exprList = self.visit(ctx.static_method())
            return CallExpr(obj, id, exprList)
        if ctx.DOLLAR_ID():
            return FieldAccess(obj, Id(ctx.DOLLAR_ID().getText()))

    # Visit a parse tree produced by D96Parser#op10.
    # op10: (NEW operands LB list_of_expr? RB) | operands; // New - Unary - Prefix - Right-assoc
    def visitOp10(self, ctx:D96Parser.Op10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands()) 

        id = self.visit(ctx.operands())
        exprList = self.visit(ctx.list_of_expr()) if ctx.list_of_expr() else []
        return NewExpr(id, exprList)


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
    # element_expr: index_ops
    def visitElement_expr(self, ctx:D96Parser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_ops.
    # index_ops: index_ops LS all_expr RS | LS all_expr RS;
    def visitIndex_ops(self, ctx:D96Parser.Index_opsContext):
        # LS all_expr RS
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.all_expr())]

        # index_ops LS all_expr RS
        return self.visit(ctx.index_ops()) + [self.visit(ctx.all_expr())] 


    # Visit a parse tree produced by D96Parser#static_member_access.
    # static_member_access: (SELF | ID) DOUBLE_COLON (DOLLAR_ID | static_method);
    # Self::$a or Self::$a() or Self::$a(b) or Self::$a(b, c)
    # x::$a or x::$a() or x::$a(b) or x::$a(b, c)
    def visitStatic_member_access(self, ctx:D96Parser.Static_member_accessContext):
        # Left: SELF | ID
        if ctx.SELF():
            id = SelfLiteral()
        if ctx.ID():
            id = Id(ctx.ID().getText())
        
        # Right: DOLLAR_ID | static_method
        if ctx.DOLLAR_ID(): 
            return FieldAccess(id, Id(ctx.DOLLAR_ID().getText()))
        if ctx. static_method():
            right, exprList = self.visit(ctx.static_method())
            return CallExpr(id, right, exprList)   


    # Visit a parse tree produced by D96Parser#static_method.
    # static_method: DOLLAR_ID LB list_of_expr? RB; --> $a() / $a(b) / $a(b, c)
    def visitStatic_method(self, ctx:D96Parser.Static_methodContext):
        id = Id(ctx.DOLLAR_ID().getText())
        exprList = self.visit(ctx.list_of_expr()) if ctx.list_of_expr() else []
        return id, exprList


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
            return IntLiteral(self.checkBase(ctx.LITERAL_INT().getText()))
        if ctx.LITERAL_FLOAT():
            # .e3
            if ctx.LITERAL_FLOAT().getText().startswith('.'):
                return FloatLiteral(float('0' + ctx.LITERAL_FLOAT().getText()))
            return FloatLiteral(float(ctx.LITERAL_FLOAT().getText()))
        if ctx.LITERAL_STRING(): return StringLiteral(ctx.LITERAL_STRING().getText())
        if ctx.LITERAL_BOOLEAN(): return BooleanLiteral(ctx.LITERAL_BOOLEAN().getText())
        if ctx.LITERAL_ZERO(): return IntLiteral(int(0))

    def checkBase(self, stringLit):
        if stringLit.startswith('0x') or stringLit.startswith('0X'):
            return int(stringLit, 16)
        elif stringLit.startswith('0b') or stringLit.startswith('0B'):
            return int(stringLit[2:], 2)
        elif stringLit.startswith('0'):
            return int(stringLit[1:], 8)
        return int(stringLit)

    # Visit a parse tree produced by D96Parser#literal_array.
    # literal_array: literal_idx_array | literal_mtd_array;
    # --> Let the visitor choose the path
    def visitLiteral_array(self, ctx:D96Parser.Literal_arrayContext):
        return self.visitChildren(ctx) 


    # Visit a parse tree produced by D96Parser#literal_idx_array.
    # literal_idx_array: ARRAY LB array_element? RB;
    def visitLiteral_idx_array(self, ctx:D96Parser.Literal_idx_arrayContext):
        array_element = self.visit(ctx.array_element()) if ctx.array_element() else []
        return ArrayLiteral(array_element)


    # Visit a parse tree produced by D96Parser#literal_mtd_array.
    # literal_mtd_array: ARRAY LB literal_idx_array (COMMA literal_idx_array)* RB;
    def visitLiteral_mtd_array(self, ctx:D96Parser.Literal_mtd_arrayContext):
        return [self.visitLiteral_idx_array(x) for x in ctx.literal_idx_array()]


    # Visit a parse tree produced by D96Parser#array_element.
    # array_element: all_expr (COMMA all_expr)*;
    def visitArray_element(self, ctx:D96Parser.Array_elementContext):
        return [self.visitAll_expr(x) for x in ctx.all_expr()]