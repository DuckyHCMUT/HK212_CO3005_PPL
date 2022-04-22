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
                if i.name.name == 'main' and i.kind == 'Static':
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
            #print("lookup = ", Checker.utils.lookup(i.name, outer, lambda x: x.name))
            if x in resultEnv:
                resultEnv.remove(x)
            resultEnv.append(i)

        return resultEnv

    @staticmethod
    def getTypeInReturn(expr, className = None, size = None, arrType = None):
        typeMap = {
            IntLiteral: IntType(),
            FloatLiteral: FloatType(),
            BooleanLiteral: BoolType(),
            StringLiteral: StringType(),
            ArrayLiteral: ArrayType(size, arrType),
            NullLiteral: None,
            SelfLiteral: ClassType(className),
        }
        return typeMap[expr]


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

        for i, j in self.classMap.items():
            print(f"Class {i}: {[x.__str__() for x in j]}")
        return []

    # class ClassDecl(Decl):
    # classname: Id
    # memlist: List[MemDecl]
    # parentname: Id = None  # None if there is no parent
    def visitClassDecl(self, ast, c):
        # Check no entry point
        if ast.classname.name == 'Program':
            Checker.checkNoEntry(ast.memlist)

        # If a Class name inherits the same Superclass name, Undeclared Class will be raised
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
        return (ret, True) if ast.kind == 'Static' else (ret, False)

    def visitConstDecl(self, ast, c):
        name = ast.constant
        constType = ast.constType
        value = ast.value

        # Raise redeclared for Constant 
        if self.lookup(name, c, lambda x: x.name):
            raise Redeclared(Constant(), name.name)

        # Raise error because constant variable can't be null
        if not value:
            raise IllegalConstantExpression(None)

        return Symbol(name, constType, value)

    def visitVarDecl(self, ast, c):
        name = ast.variable
        varType = ast.varType
        value = ast.varInit

        # Raise redeclared for Variable
        if self.lookup(name, c, lambda x: x.name):
            raise Redeclared(Variable(), name.name)

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

        return sym, (True if ast.kind == 'Static' else False)

    # class Block(Stmt):
    # inst: List[Inst]
    def visitBlock(self, ast, c):
        print(f"===================== {ast} ======================")
        inner, outer = [] + c[0], [] + c[1]
        #print(f"inner = {[i.__str__() for i in inner]}")
        #print(f"outer = {[i.__str__() for i in outer]}")
        
        # resultEnv = Checker.overrideInEnv(inner, outer)

        for i in ast.inst:
            # Variable and Constant Declaration Statement
            if type(i) is VarDecl or type(i) is ConstDecl:
                inner.append(self.visit(i, inner))
            elif type(i) is Assign:
                self.visit(i, Checker.overrideInEnv(inner, outer))
            elif type(i) is Return:
                return self.visit(i, Checker.overrideInEnv(inner, outer))
            else:
                self.visit(i, Checker.overrideInEnv(inner, outer))
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

        if type(ast.expr) is Id:
            retType = self.lookup(ast.expr, c, lambda x: x.name)
            if not retType:
                raise Undeclared(Identifier(), ast.expr.name)
            else:
                return retType.mtype
        else:
            return self.visit(ast.expr, c)

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
        print("If ast = ", ast.expr, ast.thenStmt, ast.elseStmt)

        evaType = self.visit(ast.expr, c)
        # thenBlock = self.visit(ast.thenStmt, c)
        # elseBlock = self.visit(ast.elseStmt, c)
    
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
        for i in c:
            print("binop c = ", i)
    
        print("binop = ", ast.op, ast.left, ast.right)

    def visitUnaryOp(self, ast, c):
        return

    def visitCallExpr(self, ast, c):
        return

    def visitNewExpr(self, ast, c):
        return

    def visitArrayCell(self, ast, c):
        return

    def visitFieldAccess(self, ast, c):
        return



    

    # <--- Type visitor --->
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
    