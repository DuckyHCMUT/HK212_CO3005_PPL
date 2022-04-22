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
    def __init__(self, name, mtype, value = None, parent = None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.parent = parent

    def __str__(self):
        return 'Symbol(' + str(self.name) + ',' + str(self.mtype) + ',' + str(self.value) + ',' + str(self.parent) +')'

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
    # global_envi = [
    #     Symbol("getInt",MType([],IntType())),
    #     Symbol("putIntLn",MType([IntType()],VoidType()))
    # ]

    global_envi = []
    classList = []
    classMap = {}

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
        for x in ast.decl:
            symbol = Symbol(x.classname, MType([], ClassType(x.classname)), None, x.parentname)
            self.classList.append(Checker.checkRedeclared(symbol, Class(), symbols))
            symbols.append(Checker.checkRedeclared(symbol, Class(), symbols))
            self.visit(x, symbols)

        # Check no entry
        if not self.lookup('Program', self.classList, lambda x: x.name.name):
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

        # If a Class name inherits the same Superclass name, Undeclared Class will be raised
        if ast.classname == ast.parentname:
            raise Undeclared(Class(), ast.parentname.name)

        # Raise error if this class inherits undeclared class
        if ast.parentname:
            if not self.lookup(ast.parentname, c, lambda x: x.name):
                raise Undeclared(Class(), ast.parentname.name)

        mem = []

        for x in ast.memlist:
            name, sym = self.visit(x, mem)
            if self.lookup(name, mem, lambda x: x.name):
                raise Redeclared(Attribute(), name.name)
            #mem.append(sym)
            if x.kind == 'Static':
                self.global_envi.append(sym)
        
        for i in mem:
            print("mem = ", i.__str__())
        
        return

    # class AttributeDecl(MemDecl):
    # kind: SIKind 
    # decl: StoreDecl 
    def visitAttributeDecl(self, ast, c):
        name, mtype, value = self.visit(ast.decl, c)
        sym = Symbol(name, mtype, value, None)
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
        
        param_list = []
        type_list = []
        
        # All param are VarDecl
        for p in ast.param:
            # Check redeclared right in parameter part
            if self.lookup(p.variable, param_list, lambda x: x.name):
                raise Redeclared(Parameter(), p.variable.name)
            param_list.append(Symbol(p.variable, MType([], p.varType), None, None))
            type_list.append(p.varType)

        # Helper function to override outer variable by parameters (if variable with same name was declared)
        # method_env = Checker.overrideInEnv(param_list, c)
        
        # return the type of a method decl
        return name, Symbol(name, MType([], self.visit(ast.body, [c, param_list])), None, None)

    # class Block(Stmt):
    # inst: List[Inst]
    def visitBlock(self, ast, c):
        # print(f"========== {ast} ==========")
        outer, inner = [] + c[0], [] + c[1]

        # variable from c (ref envi) can be redeclared, but scope can't
        ref_envi = Checker.overrideInEnv(inner, outer)
        
        for x in ast.inst:
            if type(x) is VarDecl:
                if self.lookup(x.variable, inner, lambda x: x.name):
                    raise Redeclared(Variable(), x.variable.name)
                else:
                    name, mtype, value = self.visit(x, ref_envi)
                    #inner.append(Symbol(name, mtype, value, None))
            elif type(x) is ConstDecl:
                if self.lookup(x.constant, inner, lambda x: x.name):
                    raise Redeclared(Constant(), x.constant.name)
                else:
                    name, mtype, value = self.visit(x, ref_envi)
                    #inner.append(Symbol(name, mtype, value, None))
            elif type(x) is Return:
                return self.visit(x, [outer, inner]) # Skip every other things after
            elif type(x) is Block:
                self.visit(x, [ref_envi, []])
            else:
                self.visit(x, c)


    # class CallStmt(Stmt):
    # obj: Expr
    # method: Id
    # param: List[Expr]
    def visitCallStmt(self, ast, c):
        # print("ast = ", ast)
        pass

    # class Return(Stmt):
    # expr: Expr = None
    def visitReturn(self, ast, c):
        outer, inner = c[0], c[1]
        if ast.expr:
            if type(ast.expr) is Id:
                ret = self.lookup(ast.expr, inner, lambda x: x.name)
                if ret:
                    return ret.mtype.rettype
                else: raise Undeclared(Identifier(), ast.expr.name)
            elif type(ast.expr) in [IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral, NullLiteral, SelfLiteral, ArrayLiteral]:
                print(Checker.getTypeInReturn(type(ast.expr)))
            for i in c[0]:
                print("outer = ", i.__str__())
            for i in c[1]:
                print("inner = ", i.__str__())
            return type(ast.expr)

    # Continue stmt
    def visitContinue(self, ast, c):
        return 

    # Break stmt
    def visitBreak(self, ast, c):
        return

    # Gonna be very long
    def visitFor(self, ast, c):
        return

    def visitIf(self, ast, c):
        return

    def visitAssign(self, ast, c):
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
    