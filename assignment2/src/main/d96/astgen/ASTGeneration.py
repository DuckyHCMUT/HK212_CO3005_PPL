# Generate Abstract Syntax Tree from a parse tree generated from ANTLR

from numbers import Real
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

### Remember to uncomment this mess before submit to BKEL ###
from main.d96.utils.AST import AttributeDecl, ArrayType, BoolType, ClassDecl, IntLiteral, StringType, UnaryOp
from main.d96.utils.AST import FloatType, Id, Instance, IntType, Program, Static, VarDecl

class ASTGeneration(D96Visitor):
    def checkDatatype(self, param, expr = None):
        # Helper function to return corresponding data type and value
        if not expr:
            if 'Int' in param:
                return IntType().__str__()
            elif 'Float' in param:
                return FloatType().__str__()
            elif 'Bool' in param:
                return BoolType().__str__()
            elif 'String' in param:
                return StringType().__str__()
            elif 'Array' in param:
                return ArrayType().__str__()

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
    # class_attr: (VAR | VAL) 
	#             (attr_no_value 
	# 		      | attr_with_value 
	# 		      | attr_array_no_value 
	# 		      | attr_array_with_value) 
	# 		      SEMI;
    # --> Just need to visit either any attribute
    def visitClass_attr(self, ctx:D96Parser.Class_attrContext):
        if ctx.attr_no_value():
            return self.visitAttr_no_value(ctx.attr_no_value())

        elif ctx.attr_with_value():
            return self.visitAttr_with_value(ctx)

        elif ctx.attr_array_no_value():
            return self.visitAttr_array_no_value(ctx.attr_array_no_value())

        elif ctx.attr_array_with_value():
            return self.visitAttr_array_with_value(ctx.attr_array_with_value())


    # Visit a parse tree produced by D96Parser#attr_no_value.
    def visitAttr_no_value(self, ctx:D96Parser.Attr_no_valueContext):
        type = ctx.data_type().getText()
        name = ctx.any_id(0).getText()
        attrList = []
        
        for name in ctx.any_id():
            # Dollar id --> static
            if '$' in name.getText():
                attrList.append(AttributeDecl(Static().__str__(), VarDecl(Id(name.getText()), self.checkDatatype(type))))
            # Normal id --> instance
            else:
                attrList.append(AttributeDecl(Instance().__str__(), VarDecl(Id(name.getText()), self.checkDatatype(type))))
        return attrList


    # Visit a parse tree produced by D96Parser#attr_with_value.
    # attr_with_value: any_id attr_pair all_expr; 
    # attr_pair: COMMA any_id attr_pair all_expr COMMA | COLON data_type ASSIGN; 
    def visitAttr_with_value(self, ctx:D96Parser.Attr_with_valueContext):
        # print(ctx.getText())
        name = Id(ctx.attr_with_value().any_id().getText()) # First variable
        expr = IntLiteral(ctx.attr_with_value().all_expr().getText()) # Last value
        #type = ctx.attr_with_value().attr_pair().data_type().getText()
        muttability = ctx.VAL() if ctx.VAL() else ctx.VAR()
        
        a = [name] + [expr] + self.visitAttr_pair(ctx.attr_with_value().attr_pair())
        print(type(a), a)
        
    # Visit a parse tree produced by D96Parser#attr_pair.
    def visitAttr_pair(self, ctx:D96Parser.Attr_pairContext):
        # COLON data_type ASSIGN
        if ctx.getChildCount() == 3:
            # print("ctx.getChildCount() == 3: ", ctx.getText())
            # print(ctx.data_type().getText())
            return [self.checkDatatype(ctx.data_type().getText())] # Data type, some sort of like Int should be returned here
            
        # COMMA any_id attr_pair all_expr COMMA
        elif ctx.getChildCount() == 5:
            #print("ctx.getChildCount() == 5: ", ctx.getText())
            name = Id(ctx.any_id().getText())
            expr = IntLiteral(ctx.all_expr().getText())
            # print(name, expr)
            return [name, expr] + ctx.attr_pair().accept(self)


    # Visit a parse tree produced by D96Parser#attr_array_no_value.
    def visitAttr_array_no_value(self, ctx:D96Parser.Attr_array_no_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_with_value.
    def visitAttr_array_with_value(self, ctx:D96Parser.Attr_array_with_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_pair.
    def visitAttr_array_pair(self, ctx:D96Parser.Attr_array_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_decl_tail.
    def visitAttr_array_decl_tail(self, ctx:D96Parser.Attr_array_decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#any_id.
    # any_id: ID | DOLLAR_ID;
    # --> Just need to visit either any ID or DOLLAR_ID
    def visitAny_id(self, ctx:D96Parser.Any_idContext):
        return ctx.getText()


    # Visit a parse tree produced by D96Parser#class_method.
    # class_method: normal_method | constructor | destructor;
    # --> Just need to visit either any method
    def visitClass_method(self, ctx:D96Parser.Class_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normal_method.
    def visitNormal_method(self, ctx:D96Parser.Normal_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_decl.
    def visitVar_decl(self, ctx:D96Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_no_value.
    def visitVar_no_value(self, ctx:D96Parser.Var_no_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_with_value.
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
    def visitVar_array_decl_tail(self, ctx:D96Parser.Var_array_decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_rhs.
    def visitArray_rhs(self, ctx:D96Parser.Array_rhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:D96Parser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params_list.
    def visitParams_list(self, ctx:D96Parser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_type.
    def visitData_type(self, ctx:D96Parser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_if_body.
    def visitElse_if_body(self, ctx:D96Parser.Else_if_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_body.
    def visitElse_body(self, ctx:D96Parser.Else_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_stmt.
    def visitFor_in_stmt(self, ctx:D96Parser.For_in_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_body.
    def visitFor_in_body(self, ctx:D96Parser.For_in_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_expr.
    def visitFor_in_expr(self, ctx:D96Parser.For_in_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_variable.
    def visitScalar_variable(self, ctx:D96Parser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invoc_literal.
    def visitMethod_invoc_literal(self, ctx:D96Parser.Method_invoc_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcall.
    def visitFuncall(self, ctx:D96Parser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#all_expr.
    def visitAll_expr(self, ctx:D96Parser.All_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op.
    def visitOp(self, ctx:D96Parser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op1.
    def visitOp1(self, ctx:D96Parser.Op1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op2.
    def visitOp2(self, ctx:D96Parser.Op2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op3.
    def visitOp3(self, ctx:D96Parser.Op3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op4.
    def visitOp4(self, ctx:D96Parser.Op4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op5.
    def visitOp5(self, ctx:D96Parser.Op5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op6.
    def visitOp6(self, ctx:D96Parser.Op6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op7.
    def visitOp7(self, ctx:D96Parser.Op7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op8.
    def visitOp8(self, ctx:D96Parser.Op8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op9.
    def visitOp9(self, ctx:D96Parser.Op9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op10.
    def visitOp10(self, ctx:D96Parser.Op10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_expr.
    def visitElement_expr(self, ctx:D96Parser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_ops.
    def visitIndex_ops(self, ctx:D96Parser.Index_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_member_access.
    def visitStatic_member_access(self, ctx:D96Parser.Static_member_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method.
    def visitStatic_method(self, ctx:D96Parser.Static_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_create.
    def visitObject_create(self, ctx:D96Parser.Object_createContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_expr.
    def visitList_of_expr(self, ctx:D96Parser.List_of_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)

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
    def visitLiteral_idx_array(self, ctx:D96Parser.Literal_idx_arrayContext):
        array_element = ctx.array_element()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by D96Parser#literal_mtd_array.
    def visitLiteral_mtd_array(self, ctx:D96Parser.Literal_mtd_arrayContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by D96Parser#array_element.
    def visitArray_element(self, ctx:D96Parser.Array_elementContext):
        return [self.visitAll_expr(x) for x in ctx.all_expr()]

    # def visitBody(self, ctx: D96Parser.BodyContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self, ctx: D96Parser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self, ctx: D96Parser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))
