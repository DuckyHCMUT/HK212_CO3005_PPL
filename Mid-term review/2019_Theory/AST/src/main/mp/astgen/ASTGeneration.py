from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce
 
# Question A
# class ASTGeneration(MPVisitor):
#     def visitProgram(self, ctx:MPParser.ProgramContext):
#         return 1 + self.visit(ctx.struct())

#     def visitStruct(self, ctx:MPParser.StructContext):
#         return 1 + sum([self.visitMem(x) for x in ctx.mem()])

#     def visitMem(self, ctx:MPParser.MemContext):
#         return 1 + self.visit(ctx.data_type()) + len(ctx.ID())

#     def visitData_type(self, ctx:MPParser.Data_typeContext):
#         return 1 + self.visit(ctx.struct()) if ctx.struct() else 1

# Question B
class ASTGeneration(MPVisitor):
    # program: struct EOF;
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visit(ctx.struct())

    # struct: STRUCT LB mem+ RB;
    def visitStruct(self, ctx:MPParser.StructContext):
        return Struct(reduce(lambda a, b: a + b, [self.visitMem(x) for x in ctx.mem()]))

    # mem: data_type ID (COMMA ID)* SEMI;
    def visitMem(self, ctx:MPParser.MemContext):
        return [MemDecl(self.visit(ctx.data_type()), var.getText()) for var in ctx.ID()]

    # data_type: INTTYPE | FLOATTYPE | struct;
    def visitData_type(self, ctx:MPParser.Data_typeContext):
        if ctx.struct(): return self.visit(ctx.struct())
        if ctx.INTTYPE(): return IntType()
        return FloatType()