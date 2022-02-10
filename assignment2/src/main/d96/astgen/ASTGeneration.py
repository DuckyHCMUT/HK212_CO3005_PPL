# Generate Abstract Syntax Tree from a parse tree generated from ANTLR

from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    # program: class_decl+ EOF;
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        declList = []
        for x in ctx.class_decl():
            decl = x.accept(self)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return Program(declList)


    def visitClassdecls(self, ctx: D96Parser.Class_declContext):
        pass

    # def visitMptype(self, ctx: D96Parser.MptypeContext):
    #     if ctx.INTTYPE():
    #         return IntType()
    #     else:
    #         return VoidType()

    # def visitBody(self, ctx: D96Parser.BodyContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self, ctx: D96Parser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self, ctx: D96Parser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))
