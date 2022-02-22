from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return 1 + self.visit(ctx.vardecls())

    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return 1 + max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail()))

    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.vardecl():
            return 1 + max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail()))
        return 0

    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + max(self.visit(ctx.mptype()), self.visit(ctx.ids()))
    
    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1

    # ids: ID ',' ids | ID; 
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 1:
            return 1
        return 1 + self.visit(ctx.ids())

        

