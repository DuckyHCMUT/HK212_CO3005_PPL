from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

from functools import reduce

class ASTGeneration(MPVisitor):
    # program: mptype EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.mptype())
    
    # mptype: primtype | arraytype;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return self.visitChildren(ctx)
    
    # arraytype: primtype dimens;
    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        return ArrayType(self.visit(ctx.dimens()), self.visit(ctx.primtype()))

    # primtype: INTTYPE | FLOATTYPE; 
    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        if ctx.INTTYPE(): return IntType()
        return FloatType()

    # dimens: dimen+;
    def visitDimens(self,ctx:MPParser.DimensContext):
        return reduce(lambda a, b: UnionType(a, b), [self.visitDimen(x) for x in ctx.dimen()])

    # dimen: '[' num '..' num ']';
    def visitDimen(self,ctx:MPParser.DimenContext):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))
    
    # num: '-'? INTLIT;
    def visitNum(self,ctx:MPParser.DimenContext):
        if ctx.getChildCount() == 1:
            return int(ctx.INTLIT().getText()) 
        return -int(ctx.INTLIT().getText()) 

        

