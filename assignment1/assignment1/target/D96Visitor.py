# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_attr.
    def visitClass_attr(self, ctx:D96Parser.Class_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_method.
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


    # Visit a parse tree produced by D96Parser#params_list.
    def visitParams_list(self, ctx:D96Parser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_type.
    def visitData_type(self, ctx:D96Parser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_types.
    def visitClass_types(self, ctx:D96Parser.Class_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_decl.
    def visitVar_decl(self, ctx:D96Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#decl_tail.
    def visitDecl_tail(self, ctx:D96Parser.Decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_decl_tail.
    def visitArray_decl_tail(self, ctx:D96Parser.Array_decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_decl.
    def visitObject_decl(self, ctx:D96Parser.Object_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_tail.
    def visitExpr_tail(self, ctx:D96Parser.Expr_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type_tail.
    def visitArray_type_tail(self, ctx:D96Parser.Array_type_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:D96Parser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_body.
    def visitIf_body(self, ctx:D96Parser.If_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_if_body.
    def visitElse_if_body(self, ctx:D96Parser.Else_if_bodyContext):
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


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invoc.
    def visitMethod_invoc(self, ctx:D96Parser.Method_invocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal_idx_array.
    def visitLiteral_idx_array(self, ctx:D96Parser.Literal_idx_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal_mtd_array.
    def visitLiteral_mtd_array(self, ctx:D96Parser.Literal_mtd_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_element.
    def visitArray_element(self, ctx:D96Parser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arithmetic_ops.
    def visitArithmetic_ops(self, ctx:D96Parser.Arithmetic_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolean_ops.
    def visitBoolean_ops(self, ctx:D96Parser.Boolean_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_ops.
    def visitString_ops(self, ctx:D96Parser.String_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_ops.
    def visitRelational_ops(self, ctx:D96Parser.Relational_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_expr.
    def visitElement_expr(self, ctx:D96Parser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_ops.
    def visitIndex_ops(self, ctx:D96Parser.Index_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_attr.
    def visitInstance_attr(self, ctx:D96Parser.Instance_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_attr.
    def visitStatic_attr(self, ctx:D96Parser.Static_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_method.
    def visitInstance_method(self, ctx:D96Parser.Instance_methodContext):
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



del D96Parser