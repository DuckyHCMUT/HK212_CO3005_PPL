# Student ID: 1953097

"""
 * @author nhphung
"""

from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    """
    Type of method declaration:
    partype: list(Type) - parameters type
    rettype: Type       - return type
    """
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + ')'

class Symbol:
    def __init__(self, name, mtype, value = None, parent = None, inclass = None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.parent = parent
        self.inclass = inclass

    def toStatic(self, classname):
        self.inclass = classname
        return self

    def __str__(self):
        return 'Symbol(' + str(self.name) + ',' + str(self.mtype) + ',' + str(self.value) + ',' + str(self.parent) + ',' + str(self.inclass) +')'

class Checker(BaseVisitor,Utils):
    utils = Utils()

    @staticmethod
    def checkNoEntry(memlist):
        # Step 1: Check if Program does not have Program class --> raise, checked below
        # Step 2 (This function): In Program class, check if main method is Static, if not --> raise
        # Step 2.1: If the main function is Static but return something (Did not check in assignment 2 - AST) --> raise
        for i in memlist:
            if type(i) is MethodDecl:
                if i.name.name == 'main' and i.kind == 'Static':
                    # Need to check no return or return nothing here
                    return
        raise NoEntryPoint

    @staticmethod
    def typeCheckConst(ast):
        if type(ast.constType) is FloatType and type(ast.value) is FloatLiteral:
            return
        if type(ast.constType) is IntType and type(ast.value) is IntLiteral:
            return
        if type(ast.constType) is BoolType and type(ast.value) is BooleanLiteral:
            return
        if type(ast.constType) is StringType and type(ast.value) is StringLiteral:
            return
        raise TypeMismatchInStatement(ast)

    @staticmethod
    def typeCheckVar(ast):
        if type(ast.varType) is FloatType and type(ast.varInit) is FloatLiteral:
            return
        if type(ast.varType) is IntType and type(ast.varInit) is IntLiteral:
            return
        if type(ast.varType) is BoolType and type(ast.varInit) is BooleanLiteral:
            return
        if type(ast.varType) is StringType and type(ast.varInit) is StringLiteral:
            return
        raise TypeMismatchInStatement(ast)

    @staticmethod
    def checkRedeclared(sym, kind, c):
        if Checker.utils.lookup(sym.name, c, lambda x: x.name):
            raise Redeclared(kind, sym.name.name)
        return sym


class StaticChecker(BaseVisitor,Utils):
    # global_envi = [
    #     Symbol("getInt",MType([],IntType())),
    #     Symbol("putIntLn",MType([IntType()],VoidType()))
    # ]

    global_envi = []

    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

# Visit the Program section
    # class Program(AST):
    # decl: List[ClassDecl]
    def visitProgram(self, ast:Program, c):
        symbols = []

        # Check redeclared class
        # for x in ast.decl:
        #     print("x.name = ", x.classname)
        #     name, sym = self.visit(x, symbols)

        #     if name.name in symbols:
        #         raise Redeclared(Class(), name.name)
        #     symbols[name.name] = sym
        #     self.global_envi.append(sym)

        for x in ast.decl:
            symbol = Symbol(x.classname, MType([], ClassType(x.classname)), None, x.parentname, None)
            self.global_envi.append(Checker.checkRedeclared(symbol, Class(), symbols))
            symbols.append(Checker.checkRedeclared(symbol, Class(), symbols))
            self.visit(x, symbols)

        # Check no entry
        if not self.lookup('Program', self.global_envi, lambda x: x.name.name):
            raise NoEntryPoint()

        return []

    # class ClassDecl(Decl):
    # classname: Id
    # memlist: List[MemDecl]
    # parentname: Id = None  # None if there is no parent
    def visitClassDecl(self, ast, c):
        # Check no entry point
        if ast.classname.name == 'Program':
            Checker.checkNoEntry(ast.memlist)

        mem = []

        for x in ast.memlist:
            name, sym = self.visit(x, mem)
            if self.lookup(name, mem, lambda x: x.name):
                raise Redeclared(Attribute(), name.name)
            mem.append(sym)
            if x.kind == 'Static':
                s = sym.toStatic(ast.classname)
                self.global_envi.append(s)
        return
        # return class_name, Symbol(class_name, MType([], ClassType(class_name)), None, parent, None)

    # class AttributeDecl(MemDecl):
    # kind: SIKind 
    # decl: StoreDecl 
    def visitAttributeDecl(self, ast, c):
        name, mtype, value = self.visit(ast.decl, c)
        sym = Symbol(name, mtype, value, None, None)
        return name, sym

    def visitConstDecl(self, ast, c):
        name = ast.constant
        constType = ast.constType
        value = ast.value

        # Raise error because constant variable can't be null
        if not value:
            raise IllegalConstantExpression(None)

        # Raise error because type mismatch
        Checker.typeCheckConst(ast)

        return name, MType([], constType), value

    def visitVarDecl(self, ast, c):
        name = ast.variable
        varType = ast.varType
        value = ast.varInit

        if value:
            Checker.typeCheckVar(ast)

        return name, MType([], varType), value

    # class MethodDecl(MemDecl):
    # kind: SIKind
    # name: Id
    # param: List[VarDecl]
    # body: Block
    def visitMethodDecl(self, ast, c):
        name = ast.name
        param = ast.param
        self.visit(ast.body, c)
        return name, Symbol(name, MType([], None), None, None, None)

    # class Block(Stmt):
    # inst: List[Inst]
    def visitBlock(self, ast, c):
        # print("c = ", [i.__str__() for i in c])

        # variable from c (ref envi) can be redeclared, but scope can't
        scope = [] + c
        for x in ast.inst:
            self.visit(x, scope)
        pass

    # class CallStmt(Stmt):
    # obj: Expr
    # method: Id
    # param: List[Expr]
    def visitCallStmt(self, ast, c):
        local_env = list(set(c + self.global_envi))

        print([i.__str__() for i in local_env])

        obj = ast.obj

        print(self.lookup(obj.name, local_env, lambda x: x.name))

        method = ast.method
        param = [i for i in ast.param]
        
        #print(obj, method, param)

    # class Return(Stmt):
    # expr: Expr = None
    def visitReturn(self, ast, c):
        pass

    def visitIntType(self, ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBoolType(self, ast, c):
        return BoolType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitArrayType(self, ast, c):
        return ArrayType()

    def visitClassType(self, ast, c):
        return ClassType()

    def visitVoidType(self, ast, c):
        return VoidType()
    