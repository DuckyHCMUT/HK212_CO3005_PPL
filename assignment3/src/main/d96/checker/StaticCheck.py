# Student ID: 1953097

"""
 * @author nhphung
"""

from AST import * 
from Visitor import *
#from Utils import Utils
from StaticError import *

class Utils:
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    # def __str__(self):
    #     return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + ')'

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return 'Symbol(' + str(self.name) + ',' + str(self.mtype) + ',' + str(self.value) +')'

class Checker(BaseVisitor,Utils):
    utils = Utils()

    @staticmethod
    def checkNoEntry(memlist):
        # Step 1: Check if Program does not have Program class --> raise, checked below
        # Step 2 (This function): In Program class, check if main method is Static, if not --> raise
        # Step 2.1: If the main function is Static but return something (Did not check in assignment 2 - AST) --> raise
        for i in memlist:
            if type(i) is MethodDecl:
                if i.name.name == 'main' and i.kind == Static():
                    return 
        raise NoEntryPoint()

    @staticmethod
    def checkRedeclared(sym, kind, c):
        if Checker.utils.lookup(sym.name, c, lambda x: x.name):
            raise Redeclared(kind, sym.name.name)
        return sym

    @staticmethod
    def overrideInEnv(inner, outer):
        # inner: overriding (local)
        # outer: being overrided (global)
        resultEnv = outer

        for i in inner:
            x = Checker.utils.lookup(i.name, outer, lambda x: x.name)
            if x in resultEnv:
                resultEnv.remove(x)
            resultEnv.append(i)

        return resultEnv


class StaticChecker(BaseVisitor,Utils):
    global_envi = []
    classMap = {}

    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

# Visit the Program section
    # class Program(AST):
    # decl: List[ClassDecl]
    def visitProgram(self, ast:Program, c):
        for x in ast.decl:
            # Check redeclared class
            if x.classname.name in self.classMap:
                raise Redeclared(Class(), x.classname.name)
            else:
                self.classMap[x.classname.name] = self.visit(x, self.classMap)

        # Check no entry
        if 'Program' not in self.classMap:
            raise NoEntryPoint()

        # for i, j in self.classMap.items():
        #     print(f"Class {i}: {[x.__str__() for x in j]}")

        # Somehow if I don't clear this, the later on testcase will still inherits the previous class
        self.classMap.clear()
        return []

    # class ClassDecl(Decl):
    # classname: Id
    # memlist: List[MemDecl]
    # parentname: Id = None  # None if there is no parent
    def visitClassDecl(self, ast, c):
        # Check no entry point
        if ast.classname == Id(Program):
            Checker.checkNoEntry(ast.memlist)

        # If a Class name inherits the same Superclass name, Undeclared Class will be raised
        if ast.parentname:
            if ast.classname == ast.parentname:
                raise Undeclared(Class(), ast.parentname.name)

        # Raise error if this class inherits undeclared class
        if ast.parentname:
            if not self.lookup(ast.parentname, c, lambda x: x.name):
                raise Undeclared(Class(), ast.parentname.name)

        mem = []

        for x in ast.memlist:
            ret, isStatic = self.visit(x, mem)
            mem.append(ret)
                
        return mem

    # class AttributeDecl(MemDecl):
    # kind: SIKind 
    # decl: StoreDecl 
    def visitAttributeDecl(self, ast, c):
        ret = self.visit(ast.decl, c)
        return (ret, True)

    def visitConstDecl(self, ast, c):
        name = ast.constant
        constType = ast.constType
        value = ast.value
        valueType = self.visit(ast.value, c)

        # Raise redeclared for Constant 
        if self.lookup(name, c, lambda x: x.name):
            raise Redeclared(Constant(), name.name)

        # Raise error because constant variable can't be null
        if not valueType:
            raise IllegalConstantExpression(None)

        # Raise error because type mismatch
        if type(valueType) != type(constType):
            raise TypeMismatchInConstant(ast)

        return Symbol(name, constType, value)

    def visitVarDecl(self, ast, c):
        name = ast.variable
        varType = ast.varType
        value = ast.varInit
        valueType = self.visit(ast.varInit, c) if ast.varInit else None

        # Raise redeclared for Variable
        if self.lookup(name, c, lambda x: x.name):
            raise Redeclared(Attribute(), name.name)

        # Raise error because type mismatch and if only there is value
        if valueType:
            if type(valueType) != type(varType):
                raise TypeMismatchInStatement(ast)

        return Symbol(name, varType, value)

    # class MethodDecl(MemDecl):
    # kind: SIKind
    # name: Id
    # param: List[VarDecl]
    # body: Block
    def visitMethodDecl(self, ast, c):
        # Check and raise redeclared method
        if self.lookup(ast.name, c, lambda x: x.name):
            raise Redeclared(Method(), ast.name.name)

        # Check for parameter
        paramList = []
        typeList = []
        for i in ast.param:
            if self.lookup(i.variable, paramList, lambda x: x.name):
                raise Redeclared(Parameter(), i.variable.name)
            paramList.append(self.visit(i, paramList))
            typeList.append(i.varType)

        # Create a new symbol and immediately pass into the body block
        sym = Symbol(ast.name, MType(typeList, []), None)
        # Get the return type of that method
        returnType = self.visit(ast.body, [paramList, [sym] + c])
        sym.mtype.rettype = returnType

        return sym, True

    # class Block(Stmt):
    # inst: List[Inst]
    def visitBlock(self, ast, c):
        print(f"===================== {ast} ======================")
        inner = [] + c[0]
        outer = [] + c[1]

        for i in ast.inst:
            # Variable and Constant Declaration Statement
            if type(i) is VarDecl or type(i) is ConstDecl:
                self.visit(i, inner)
            elif type(i) is Assign:
                self.visit(i, [inner, outer])
            elif type(i) is Return:
                return self.visit(i, [inner, outer])
            else:
                self.visit(i, [inner, outer])

        ##print(f"inner = {[i.__str__() for i in inner]}")
        ##print(f"outer = {[i.__str__() for i in outer]}")

        return VoidType()

    # class CallStmt(Stmt):
    # obj: Expr
    # method: Id
    # param: List[Expr]                                      
    def visitCallStmt(self, ast, c):
        pass

    # class Return(Stmt):
    # expr: Expr = None
    def visitReturn(self, ast, c):
        # If expr is None
        if not ast.expr: return VoidType()

        ret = Checker.overrideInEnv(c[0], c[1])

        if type(ast.expr) is Id:
            retType = self.lookup(ast.expr, ret, lambda x: x.name)
            if not retType:
                raise Undeclared(Identifier(), ast.expr.name)
            else:
                return retType.mtype
        else:
            return self.visit(ast.expr, ret)

    # Continue stmt
    def visitContinue(self, ast, c):
        return 

    # Break stmt
    def visitBreak(self, ast, c):
        return

    # Gonna be very long
    def visitFor(self, ast, c):
        return

    # class If(Stmt):
    # expr: Expr
    # thenStmt: Stmt
    # elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast, c):
        evaType = self.visit(ast.expr, c)
        if type(evaType) is not BoolType:
            raise TypeMismatchInExpression(ast.expr)

        thenReturnType = self.visit(ast.thenStmt, c)
        elseReturnType = self.visit(ast.elseStmt, c)
        
        # Both then and else have return stmt
        if type(thenReturnType) and type(elseReturnType):
            if type(thenReturnType) != type(elseReturnType):
                raise TypeMismatchInStatement(ast)
            else:
                return thenReturnType
        else:
            pass
    
    # class Assign(Stmt):
    # lhs: Expr
    # exp: Expr
    def visitAssign(self, ast, c):
        if not self.lookup(ast.lhs, c, lambda x: x.name):
            raise Undeclared(Identifier(), ast.lhs.name)
        return

    # class BinaryOp(Expr):
    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast, c):
        lType = self.visit(ast.left, c)
        rType = self.visit(ast.right, c)
        op = ast.op

        if op in ['+', '-', '*', '/']:
            if type(lType) is FloatType or type(rType) is FloatType:
                return FloatType()
            if type(lType) is IntType or type(rType) is IntType:
                return IntType()
        elif op == '%':
            if type(lType) is IntType and type(rType) is IntType:
                return IntType()
        elif op in ['&&', '||']:
            if type(lType) is BoolType and type(rType) is BoolType:   
                return BoolType()
        elif op == '+.':
            if type(lType) is StringType and type(rType) is StringType:   
                return StringType()       
        elif op == '==.':
            if type(lType) is StringType and type(rType) is StringType:   
                return BoolType()     
        elif op in ['==', '!=']:
            ifType = [IntType, FloatType]
            if (type(lType) in ifType and type(rType) in ifType) \
            or (type(lType) is BoolType and type(rType) is BoolType): 
                return BoolType()
        elif op in ['<', '<=', '>', '>=']:
            validType = [IntType, FloatType]
            if type(lType) in validType and type(rType) in validType:
                return BoolType()

        raise TypeMismatchInExpression(ast)

    # class UnaryOp(Expr):
    # op: str - [] !
    # body: Expr
    def visitUnaryOp(self, ast, c):
        unTyp = self.visit(ast.body, c)
        op = ast.op

        if op == '-':
            if type(unTyp) is IntType: return IntType()
            elif type(unTyp) is FloatType: return FloatType()
        elif op == '!':
            if type(unTyp) is BoolType: return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        return

    def visitNewExpr(self, ast, c):
        return

    def visitArrayCell(self, ast, c):
        return

    def visitFieldAccess(self, ast, c):
        return

    # <--- Type visitor --->
    # class Id(LHS):
    # name: str
    def visitId(self, ast, c):
        # for i in c[0]:
        #     print(f"c[0] lookup = {str(i)}")
        # for i in c[1]:
        #     print(f"c[1] lookup = {str(i)}")

        # refEnv = Checker.overrideInEnv(c[0], c[1])
        x = self.lookup(ast, c, lambda x: x.name)
        if not x:
            raise Undeclared(Identifier(), ast.name)
        return x.mtype

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitArrayLiteral(self, ast, c):
        return ArrayType()

    def visitSelfLiteral(self, ast, c):
        return ClassType()

    def visitNullLiteral(self, ast, c):
        return VoidType()
    