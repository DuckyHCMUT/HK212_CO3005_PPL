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