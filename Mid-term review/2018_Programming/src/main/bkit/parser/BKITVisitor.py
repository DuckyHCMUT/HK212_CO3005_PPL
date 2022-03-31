# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_type.
    def visitArray_type(self, ctx:BKITParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#data_type.
    def visitData_type(self, ctx:BKITParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#domain_list.
    def visitDomain_list(self, ctx:BKITParser.Domain_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#domain.
    def visitDomain(self, ctx:BKITParser.DomainContext):
        return self.visitChildren(ctx)



del BKITParser