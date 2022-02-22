from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    # program: mptype EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.mptype())
    
    # mptype: primtype | arraytype;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return self.visitChildren(ctx)
        
    # primtype: INTTYPE | FLOATTYPE; 
    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        if ctx.INTTYPE():
            return IntType()
        return FloatType()
        
    # arraytype: primtype dimen | arraytype dimen;
    # arraytype: primtype dimen dimen;
    # array: real [-3 .. 0][-10 .. -1]
    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        if ctx.primtype():
            return ArrayType(self.visit(ctx.dimen()), self.visit(ctx.primtype()))
        arr = self.visit(ctx.arraytype())
        return ArrayType(UnionType(arr.indexType, self.visit(ctx.dimen())), arr.eleType)
            

    # dimen: '[' num '..' num ']';
    def visitDimen(self,ctx:MPParser.DimenContext):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))
    
    # num: '-'? INTLIT;
    def visitNum(self,ctx:MPParser.DimenContext):
        if ctx.getChildCount() == 1:
            return int(ctx.INTLIT().getText()) 
        return -int(ctx.INTLIT().getText()) 



        

