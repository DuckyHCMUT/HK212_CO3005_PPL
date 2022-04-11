# Student ID: 1953097

"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

from main.d96.utils.AST import ArrayCell, ArrayLiteral, Assign, AttributeDecl, BinaryOp, Block, BoolType, BooleanLiteral, Break, CallExpr, ClassDecl, ClassType, ConstDecl, Continue, FieldAccess, For, If, MethodDecl, NewExpr, NullLiteral, Return, FloatLiteral, StringLiteral, IntLiteral, SelfLiteral, StringType, UnaryOp, FloatType, Id, Instance, IntType, Program, Static, VarDecl, ArrayType, CallStmt, VoidType

class MType:
    """
    Type of function declaration:
    partype: list(Type) - parameters type
    rettype: Type       - return type
    """
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + ')'

class Symbol:
    # Default declare type is 
    def __init__(self, name, mtype = None, value = None, kind = None, isGlobal = None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.isGlobal = isGlobal

    def __str__(self):
        return 'Symbol(' + str(self.name) + ',' + str(self.mtype) + ',' + str(self.kind) + ')'

    def getKind(self):
        return self.kind if type(self.mtype) is MType else Identifier()

    def toGlobal(self):
        self.isGlobal = True # For static variable
        return self 

    def toVar(self):
        self.kind = Variable()
        return self

    def toParam(self):
        self.kind = Parameter()
        return self

    def toConst(self):
        self.kind = Constant()
        return self

    def toClass(self):
        self.kind = Class()
        self.toGlobal() # Once it's a Class type, the scope is global
        return self


    @staticmethod
    def fromClassDecl(decl):
        return Symbol(decl.classname).toClass()

class Scope:
    @staticmethod
    def start(scope_name):
        print("================" + scope_name + "================")
        pass

    @staticmethod
    def end():
        print("==============================================")

class Checker:
    utils = Utils()

    @staticmethod
    def checkNoEntry(symbols):
        # Step 1: If no class named Program --> Raise
        # Step 2: If no main() method in class Program --> Raise
        # Step 3: If main() method has any parameter (main(x: Float)) or return anything inside --> Raise
        # Step 4: If main() method has no parameter, no return --> OK

        # Have no Program class
        if 'Program' not in [i.name.name for i in symbols]:
            raise NoEntryPoint()

        print('symbols = ', [str(i) for i in symbols])
        # Have no main method
        # if 'main' not in 

class StaticChecker(BaseVisitor,Utils):
    global_envi = [
        Symbol("getInt",MType([],IntType())),
        Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
        
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    # class Program(AST):
    # decl: List[ClassDecl]
    def visitProgram(self, ast:Program, c):
        Scope.start("Program")
        symbols = [Symbol.fromClassDecl(x) for x in ast.decl]
        # Check redeclared

        # Check for no entry point
        Checker.checkNoEntry(symbols)
    
        Scope.end()
        return []

    # class ClassDecl(Decl):
    # classname: Id
    # memlist: List[MemDecl]
    # parentname: Id = None  # None if there is no parent
    def visitClass_decl(self, ast, c):
        class_name = ast.classname
        parent = ast.parentname
        body = [self.visitClass_body(x, c) for x in ast.memlist]


    # 
    def visitClass_body(self, ast, c):
        pass


    # Visit a parse tree produced by D96Parser#class_attr.
    def visitClass_attr(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_no_value.
    def visitAttr_no_value(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_with_value.
    def visitAttr_with_value(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_pair.
    def visitAttr_pair(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_no_value.
    def visitAttr_array_no_value(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_with_value.
    def visitAttr_array_with_value(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_pair.
    def visitAttr_array_pair(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_array_decl_tail.
    def visitAttr_array_decl_tail(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#any_id.
    def visitAny_id(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_method.
    def visitClass_method(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normal_method.
    def visitNormal_method(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_decl.
    def visitVar_decl(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_no_value.
    def visitVar_no_value(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_with_value.
    def visitVar_with_value(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_pair.
    def visitVar_pair(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_array_no_value.
    def visitVar_array_no_value(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_array_with_value.
    def visitVar_array_with_value(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_array_pair.
    def visitVar_array_pair(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_array_decl_tail.
    def visitVar_array_decl_tail(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_rhs.
    def visitArray_rhs(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs.
    def visitAssign_lhs(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params_list.
    def visitParams_list(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_type.
    def visitData_type(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#prim_type.
    def visitPrim_type(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_if_body.
    def visitElse_if_body(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_body.
    def visitElse_body(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_stmt.
    def visitFor_in_stmt(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_body.
    def visitFor_in_body(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_expr.
    def visitFor_in_expr(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_variable.
    def visitScalar_variable(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invoc.
    def visitMethod_invoc(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method_invoc.
    def visitStatic_method_invoc(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt_stmt.
    def visitBlock_stmt_stmt(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invoc_literal.
    def visitMethod_invoc_literal(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcall.
    def visitFuncall(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#all_expr.
    def visitAll_expr(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op.
    def visitOp(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op1.
    def visitOp1(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op2.
    def visitOp2(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op3.
    def visitOp3(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op4.
    def visitOp4(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op5.
    def visitOp5(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op6.
    def visitOp6(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op7.
    def visitOp7(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#postfix_array_exp.
    def visitPostfix_array_exp(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op8.
    def visitOp8(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op9.
    def visitOp9(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op10.
    def visitOp10(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_expr.
    def visitElement_expr(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_ops.
    def visitIndex_ops(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_member_access.
    def visitStatic_member_access(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method.
    def visitStatic_method(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_create.
    def visitObject_create(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_expr.
    def visitList_of_expr(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal_array.
    def visitLiteral_array(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal_idx_array.
    def visitLiteral_idx_array(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal_mtd_array.
    def visitLiteral_mtd_array(self, ast, c):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_element.
    def visitArray_element(self, ast, c):
        return self.visitChildren(ctx)
    

