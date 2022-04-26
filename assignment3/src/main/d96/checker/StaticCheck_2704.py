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


class StaticChecker(BaseVisitor,Utils):
    global_envi = []
    classMap = {}
    inFunc = False

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

        # Model: [local vars, members]
        c = []
        return [self.visit(x, [[], c]) for x in ast.memlist]
        

    # class AttributeDecl(MemDecl):
    # kind: SIKind 
    # decl: StoreDecl 
    def visitAttributeDecl(self, ast, c):
        sym = self.visit(ast.decl, c)
        c[1].append(sym)
        return

    def visitConstDecl(self, ast, c):
        if self.lookup(ast.constant, c[1], lambda x: x.name):
            raise Redeclared(Attribute(), ast.constant.name)
            
        # Raise error because constant variable can't be null
        if not ast.value:
            raise IllegalConstantExpression(None)

        name = ast.constant
        constType = ast.constType
        value = ast.value
        valueType = self.visit(ast.value, c[1])

        # Raise error because type mismatch
        if type(valueType) != type(constType):
            raise TypeMismatchInConstant(ast)

        return Symbol(name, constType, value)

    def visitConstDeclVariable(self, ast, c):
        if self.lookup(ast.constant, c[0], lambda x: x.name):
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
            print(type(valueType), type(constType))
            raise TypeMismatchInConstant(ast)

        return Symbol(name, constType, value)

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable, c[1], lambda x: x.name):
            raise Redeclared(Attribute(), ast.variable.name)

        name = ast.variable
        varType = ast.varType
        value = ast.varInit
        valueType = self.visit(ast.varInit, c[1]) if ast.varInit else None

        # Raise error because type mismatch and if only there is value
        if valueType:
            if type(valueType) != type(varType):
                raise TypeMismatchInStatement(ast)

        return Symbol(name, varType, value)

    def visitVarDeclVariable(self, ast, c):
        if self.lookup(ast.variable, c[0], lambda x: x.name):
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
        # Check and raise redeclared method
        # [c[0], c[1]] --> c[0] is local, c[1] is members
        if self.lookup(ast.name, c[1], lambda x: x.name):
            raise Redeclared(Method(), ast.name.name)

        # Check for parameter
        typeList = []
        for i in ast.param:
            if self.lookup(i.variable, c[0], lambda x: x.name):
                raise Redeclared(Parameter(), i.variable.name)
            c[0].append(self.visit(i, c))
            typeList.append(i.varType)

        # Create a new symbol and immediately pass into the body block
        sym = Symbol(ast.name, MType(typeList, []), None)
        c[1].append(sym)

        # Get the return type of that method
        returnType = self.visit(ast.body, c)
        sym.mtype.rettype = returnType

        return sym

    # class Block(Stmt):
    # inst: List[Inst]
    def visitBlock(self, ast, c):
        print(f"===================== {ast} ======================\n")

        methodBlockEnv = []
        retType = VoidType()

        for i in ast.inst:
            if type(i) == ConstDecl:
                print(f"\033[33mat i = {i}, c[0] = {[str(i) for i in c[0]]}, c[1] = {[str(i) for i in c[1]]}\033[0m")
                sym = self.visitConstDeclVariable(i, c)
                c[0].append(sym), methodBlockEnv.append(sym)
            elif type(i) == VarDecl:
                sym = self.visitVarDeclVariable(i, c)
                c[0].append(sym), methodBlockEnv.append(sym)
            elif type(i) == Block:
                r = self.visitInnerBlock(i, c)
                if r:
                    retType = r
            else:
                self.visit(i, c)

        print(f"================== End of {ast} ===================\n")
        return retType

    # Inner block
    # class Block(Stmt):
    # inst: List[Inst]
    def visitInnerBlock(self, ast, c):
        print(f"============Inner block :{ast} ======================\n")
        outerBlockEnv = [] + c[0]
        innerBlockEnv = []

        for i in c[1]:
            print(f"current global = {str(i)}")
        for i in outerBlockEnv:
            print(f"current outerBlockEnv = {str(i)}")

        for i in ast.inst:
            if type(i) == ConstDecl:
                innerBlockEnv.append(self.visitConstDeclVariable(i, [innerBlockEnv, c[0]]))
            elif type(i) == VarDecl:
                innerBlockEnv.append(self.visitVarDeclVariable(i,  [innerBlockEnv, c[0]]))
            elif type(i) == Block:
                mergedList = Checker.overrideInEnv(innerBlockEnv, outerBlockEnv)
                retType = self.visitInnerBlock(i, [mergedList, c[1]])
                # Return statement in a block
                if retType:
                    return retType
            else:
                self.visit(i, c)    

        for i in innerBlockEnv:
            print(f"current innerBlockEnv = {str(i)}")

        print(f"======= End of inner block :{ast} ===================\n")

    # class CallStmt(Stmt):
    # obj: Expr
    # method: Id
    # param: List[Expr]                                      
    def visitCallStmt(self, ast, c):
        pass

    # class Return(Stmt):
    # expr: Expr = None
    def visitReturn(self, ast, c):
        pass

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
        print(f"Assign.ast = {ast}")
        for i in c[0]:
            print("c0 = ", str(i))
        for i in c[1]:
            print("c1 = ", str(i))
        # if not self.lookup(ast.lhs, c, lambda x: x.name):
        #     raise Undeclared(Identifier(), ast.lhs.name)
        if type(ast.lhs) is FieldAccess:
            sym = self.visit(ast.lhs, c)
        elif type(ast.lhs) is Id:
            sym = self.visit(ast.lhs, c[0])
        return

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
            x = self.lookup(ast.fieldname, c, lambda x: x.name)
            if not x:
                raise Undeclared(Attribute(), ast.fieldname.name)
            else:
                return x.mtype


    # <--- Type visitor --->
    # class Id(LHS):
    # name: str
    def visitId(self, ast, c):
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
    