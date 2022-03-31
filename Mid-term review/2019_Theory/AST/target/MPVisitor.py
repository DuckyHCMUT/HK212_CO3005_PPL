# Generated from main/mp/parser/MP.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#struct.
    def visitStruct(self, ctx:MPParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#mem.
    def visitMem(self, ctx:MPParser.MemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#data_type.
    def visitData_type(self, ctx:MPParser.Data_typeContext):
        return self.visitChildren(ctx)



del MPParser