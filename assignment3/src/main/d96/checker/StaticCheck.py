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

    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + ')'

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return 'Symbol(' + str(self.name) + ',' + str(self.mtype) + ',' + str(self.value) + ')'

class Checker(BaseVisitor,Utils):
    utils = Utils()

    @staticmethod
    def checkNoEntry(memlist):
        # Step 1: Check if Program does not have Program class --> raise, checked below
        # Step 2 (This function): In Program class, check if main method is Static, if not --> raise
        # Step 2.1: If the main function is Static but return something (Did not check in assignment 2 - AST) --> raise
        for i in memlist:
            if type(i) is MethodDecl:
                if str(i.name.name) == 'main' and str(i.kind) == 'Static':
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
    
    @staticmethod
    def fprint(c, blockDepth):
        for i in c:
            print("[" + ' --> '.join([str(j) for j in i]) +"]")
        print(f"Current block depth: {blockDepth}")

    @staticmethod
    def cprint(currMap):
        for i, j in currMap.items():
            print(f"{i}: {[str(k) for k in j]}")


class StaticChecker(BaseVisitor,Utils):
    global_envi = []
    classMap = {}
    blockDepth = 0

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

        # Print current self.classMap
        Checker.cprint(self.classMap)

        # Somehow if I don't clear this, the later on testcase will still inherits the previous class
        self.classMap.clear()
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
        if ast.parentname:
            if ast.classname == ast.parentname:
                raise Undeclared(Class(), ast.parentname.name)

        # Raise error if this class inherits undeclared class
        if ast.parentname:
            if not self.lookup(ast.parentname, c, lambda x: x.name):
                raise Undeclared(Class(), ast.parentname.name)

        # Model: Stack of block [] --> [ [] ] --> [ [], [], ...]
        c = [[]]
        return [self.visit(x, c) for x in ast.memlist]
        

    # class AttributeDecl(MemDecl):
    # kind: SIKind 
    # decl: StoreDecl 
    def visitAttributeDecl(self, ast, c):
        sym = self.visit(ast.decl, c)
        c[0].append(sym)
        return sym

    def visitConstDecl(self, ast, c):
        if self.lookup(ast.constant, c[self.blockDepth], lambda x: x.name):
            if self.blockDepth == 0: # For Attribute at bottom of stack
                raise Redeclared(Attribute(), ast.constant.name)
            else:
                raise Redeclared(Constant(), ast.constant.name)
            
        # Raise error because constant variable can't be null
        if not ast.value:
            raise IllegalConstantExpression(None)

        name = ast.constant
        constType = ast.constType
        value = ast.value
        valueType = self.visit(ast.value, c)

        # Raise error because type mismatch
        if type(valueType) != type(constType):
            raise TypeMismatchInConstant(ast)

        return Symbol(name, constType, value)

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable, c[self.blockDepth], lambda x: x.name):
            if self.blockDepth == 0: # For Attribute at bottom of stack
                raise Redeclared(Attribute(), ast.variable.name)
            else:
                raise Redeclared(Variable(), ast.variable.name)

        name = ast.variable
        varType = ast.varType
        value = ast.varInit
        valueType = self.visit(ast.varInit, c) if ast.varInit else None

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
        if self.lookup(ast.name, c[0], lambda x: x.name):
            raise Redeclared(Method(), ast.name.name)

        # Check for parameter
        typeList = []
        c.append([]) # Extend from [[foo]] --> [[foo], [list of foo]]

        for i in ast.param:
            if self.lookup(i.variable, c[1], lambda x: x.name):
                raise Redeclared(Parameter(), i.variable.name)
            c[1].append(self.visitParam(i, c))
            typeList.append(i.varType)

        # Create a new symbol and immediately pass into the body block
        sym = Symbol(ast.name, MType(typeList, []), None)
        c[0].append(sym)

        # Get the return type of that method
        returnType = self.visit(ast.body, c)

        print(f"ast = {ast.body}, ret = {returnType}")

        # Entry function: main()
        if str(ast.name.name) == 'main' and str(ast.kind) == 'Static':
            if not returnType:
                returnType = VoidType()
            else:
                if type(returnType) != VoidType:
                    raise TypeMismatchInStatement(ast)

        sym.mtype.rettype = returnType

        return sym

    def visitParam(self, ast, c):
        if self.lookup(ast.variable, c[1], lambda x: x.name):
            raise Redeclared(Parameter(), ast.variable.name)

        name = ast.variable
        varType = ast.varType
        value = ast.varInit
        valueType = self.visit(ast.varInit, c) if ast.varInit else None

        # Raise error because type mismatch and if only there is value
        if valueType:
            if type(valueType) != type(varType):
                raise TypeMismatchInStatement(ast)

        return Symbol(name, varType, value)

    # class Block(Stmt):
    # inst: List[Inst]
    def visitBlock(self, ast, c):
        print(f"===================== {ast} ======================\n")
        retType = None

        self.blockDepth += 1
        
        for i in ast.inst:
            if isinstance(i, StoreDecl):
                c[self.blockDepth].append(self.visit(i, c))
            elif type(i) == Block:
                c.append([])
                r = self.visit(i, c)
                if r:
                    retType = r
            else:
                r = self.visit(i, c)
                if r:
                    retType = r
        
        # Checker.fprint(c)
        c.pop()
        self.blockDepth -= 1

        print(f"================== End of {ast} ===================\n")
        return retType

    # class CallStmt(Stmt):
    # obj: Expr
    # method: Id
    # param: List[Expr]                                      
    def visitCallStmt(self, ast, c):
        pass

    # class Return(Stmt):
    # expr: Expr = None
    def visitReturn(self, ast, c):
        return self.visit(ast.expr, c) if ast.expr else VoidType()

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
        if type(evaType) != BoolType:
            raise TypeMismatchInExpression(ast.expr)
        
        c.append([])
        thenRet = self.visit(ast.thenStmt, c)

        # Only If {}
        if not ast.elseStmt:
            return thenRet
        else:
            c.append([])
            elseRet = self.visit(ast.elseStmt, c)

            if type(thenRet) != type(elseRet):
                raise TypeMismatchInStatement(ast)

            return elseRet

    # class Assign(Stmt):
    # lhs: Expr
    # exp: Expr
    def visitAssign(self, ast, c):
        # rhs first because rhs will be checked before lhs
        # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158007
        rhsType = self.visit(ast.exp, c)
        lhsType = self.visit(ast.lhs, c)
        
        # Type-cast a stmt: FloatType = IntType 
        if type(lhsType) == FloatType and type(rhsType) == IntType:
            return

        if type(lhsType) != type(rhsType):
            raise TypeMismatchInStatement(ast)

    # class BinaryOp(Expr):
    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast, c):
        lType = self.visit(ast.left, c)
        rType = self.visit(ast.right, c)
        op = ast.op

        # Operands can either be Float or Int, but not other
        if op in ['+', '-', '*', '/']:
            if (type(lType) is FloatType and type(rType) is FloatType)\
            or (type(lType) is FloatType and type(rType) is IntType)\
            or (type(lType) is IntType and type(rType) is FloatType):
                return FloatType()
            elif type(lType) is IntType and type(rType) is IntType:
                return IntType()
        # Operands must be both Int
        elif op == '%':
            if type(lType) is IntType and type(rType) is IntType:
                return IntType()
        # Operands must be both Boolean
        elif op in ['&&', '||']:
            if type(lType) is BoolType and type(rType) is BoolType:   
                return BoolType()
        # Operands must be both String
        elif op == '+.':
            if type(lType) is StringType and type(rType) is StringType:   
                return StringType()       
        # Operands must be both String
        elif op == '==.':
            if type(lType) is StringType and type(rType) is StringType:   
                return BoolType()     
        # Operands must be Int-Float or Boolean only
        elif op in ['==', '!=']:
            validType = [IntType, FloatType]
            if (type(lType) in validType and type(rType) in validType) \
            or (type(lType) is BoolType and type(rType) is BoolType): 
                return BoolType()
        # Operands can either be Float or Int, but not other
        elif op in ['<', '<=', '>', '>=']:
            validType = [IntType, FloatType]
            if type(lType) in validType and type(rType) in validType:
                return BoolType()
        # If none of above is valid, raise type mismatch in this expression
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
        # obj: Expr
        # fieldname: Id

        if type(ast.obj) == SelfLiteral:
            x = self.lookup(ast.fieldname, c[0], lambda x: x.name)
            if not x:
                raise Undeclared(Attribute(), ast.fieldname.name)
            else:
                return x.mtype

    # <--- Type visitor --->
    # class Id(LHS):
    # name: str
    def visitId(self, ast, c):
        # Exclude the first element and traverse the stack from the top
        for i in reversed(c[1:]):
            sym = self.lookup(ast, i, lambda x: x.name)
            if sym: return sym.mtype

        raise Undeclared(Identifier(), ast.name)

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
    