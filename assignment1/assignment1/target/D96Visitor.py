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


    # Visit a parse tree produced by D96Parser#mptype.
    def visitMptype(self, ctx:D96Parser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#immuttable.
    def visitImmuttable(self, ctx:D96Parser.ImmuttableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#muttable.
    def visitMuttable(self, ctx:D96Parser.MuttableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static.
    def visitStatic(self, ctx:D96Parser.StaticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_type.
    def visitData_type(self, ctx:D96Parser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data.
    def visitData(self, ctx:D96Parser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_types.
    def visitData_types(self, ctx:D96Parser.Data_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_types.
    def visitPrimitive_types(self, ctx:D96Parser.Primitive_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_types.
    def visitArray_types(self, ctx:D96Parser.Array_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_types.
    def visitClass_types(self, ctx:D96Parser.Class_typesContext):
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


    # Visit a parse tree produced by D96Parser#self.
    def visitSelf(self, ctx:D96Parser.SelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body.
    def visitBody(self, ctx:D96Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcall.
    def visitFuncall(self, ctx:D96Parser.FuncallContext):
        return self.visitChildren(ctx)



del D96Parser