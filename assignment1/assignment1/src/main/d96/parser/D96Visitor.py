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


    # Visit a parse tree produced by D96Parser#attr_no_value.
    def visitAttr_no_value(self, ctx:D96Parser.Attr_no_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_with_value.
    def visitAttr_with_value(self, ctx:D96Parser.Attr_with_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_pair.
    def visitAttr_pair(self, ctx:D96Parser.Attr_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array.
    def visitAttr_array(self, ctx:D96Parser.Attr_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_pair_arr.
    def visitAttr_pair_arr(self, ctx:D96Parser.Attr_pair_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_decl_tail.
    def visitAttr_array_decl_tail(self, ctx:D96Parser.Attr_array_decl_tailContext):
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


    # Visit a parse tree produced by D96Parser#var_decl_no_value.
    def visitVar_decl_no_value(self, ctx:D96Parser.Var_decl_no_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_decl_with_value.
    def visitVar_decl_with_value(self, ctx:D96Parser.Var_decl_with_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair.
    def visitPair(self, ctx:D96Parser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_arr.
    def visitVar_arr(self, ctx:D96Parser.Var_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair_arr.
    def visitPair_arr(self, ctx:D96Parser.Pair_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_decl_tail.
    def visitArray_decl_tail(self, ctx:D96Parser.Array_decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_decl.
    def visitObject_decl(self, ctx:D96Parser.Object_declContext):
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


    # Visit a parse tree produced by D96Parser#int_expr.
    def visitInt_expr(self, ctx:D96Parser.Int_exprContext):
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


    # Visit a parse tree produced by D96Parser#class_name.
    def visitClass_name(self, ctx:D96Parser.Class_nameContext):
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


    # Visit a parse tree produced by D96Parser#instance_member_access.
    def visitInstance_member_access(self, ctx:D96Parser.Instance_member_accessContext):
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


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)



del D96Parser