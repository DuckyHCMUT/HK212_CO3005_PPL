from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

from functools import reduce

class ASTGeneration(MPVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(reduce(lambda a, b: a + b, [self.visitVardecl(x) for x in ctx.vardecl()]))
    
    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        type = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        return [VarDecl(id, type) for id in ids]
    
    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE(): return IntType()
        return FloatType()
    
    # ids: ID (',' ID)*; 
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(i.getText()) for i in ctx.ID()]

        

