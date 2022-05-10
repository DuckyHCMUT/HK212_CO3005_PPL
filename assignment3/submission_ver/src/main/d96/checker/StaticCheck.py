# Student ID: 1953097

"""
 * @author nhphung
"""

from AST import * 
from Visitor import *
from StaticError import *

class Utils:
    def lookup(self, name, lst, func, flag):
        # FLAG: 0 for Attribute/VarDecl/ConstDecl and 1 for Method
        for x in lst:
            if name == func(x):
                if (flag == 0 and type(x.mtype) != MType) or (flag == 1 and type(x.mtype) == MType):
                    return x
        return None

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + ')'

class Symbol:
    def __init__(self, name, mtype, declType, value = None):
        self.name = name # Id()
        self.mtype = mtype # Type() for attribute/var/const or MType() for method
        self.declType = declType # VarDecl or ConstDecl
        self.value = value # None or any for attr/var/const

    def __str__(self):
        return 'Symbol(' + str(self.name) + ',' + str(self.mtype) + ',' + str(self.declType) + ',' + str(self.value) + ')'

class Checker(BaseVisitor,Utils):
    utils = Utils()

    @staticmethod
    def checkNoEntry(memlist):
        # Step 1: In Program class, check if main method is Static, if not --> raise
        # Step 2.1: If the main function is Static but return something (Did not check in assignment 2 - AST) --> raise
        for i in memlist:
            if type(i) is MethodDecl:
                if str(i.name.name) == 'main' and str(i.kind) == 'Static':
                    return 
        raise NoEntryPoint()

    @staticmethod
    def checkParam(left, right, ast):
        # Left: x.mtype.partype (accept side)
        # Right: param (to be passed side)
        # AST: ast to be raised if error occurs
        if len(left) != len(right):
            raise TypeMismatchInStatement(ast) if type(ast) == CallStmt else TypeMismatchInExpression(ast)
        
        for i, j in zip(left, right):
            if str(i) != str(j):
                if (type(i) == ClassType and type(j) == NullLiteral)\
                or (type(i) == FloatType and type(j) == IntType):
                    continue
                else:   
                    raise TypeMismatchInStatement(ast) if type(ast) == CallStmt else TypeMismatchInExpression(ast)
        return
    
class StaticChecker(BaseVisitor,Utils):
    global_envi = []

    def __init__(self,ast):
        self.classMap = {}

        # Flag list
        self.blockDepth = 0
        self.loopDepth = 0
        self.isInMain = False
        self.isInDestructor = False
        self.isInLHS = False
        self.isConstDecl = False
        self.willRaiseError = False
        self.checkClass = False
        
        self.ast = ast
    

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast:Program, c):
        for x in ast.decl:
            # Check redeclared class
            if x.classname.name in self.classMap:
                raise Redeclared(Class(), x.classname.name)
            else:
                self.classMap[x.classname.name] = []
                self.visit(x, self.classMap)

        # Check no entry
        if 'Program' not in self.classMap:
            raise NoEntryPoint()
        return []


    def visitClassDecl(self, ast, c):
        # Check no entry point
        if ast.classname.name == 'Program':
            Checker.checkNoEntry(ast.memlist)

        # No inheritance but still check if inherited class is declared or not
        if ast.parentname:
            if ast.parentname.name == ast.classname.name or ast.parentname.name not in self.classMap:
                raise Undeclared(Class(), ast.parentname.name)

        # Model: Stack of block [] --> [ [] ] --> [ [], [], ...]
        c = [[]]

        for x in ast.memlist:
            mem = self.visit(x, c)
            self.classMap[ast.classname.name].append(mem)


    def visitAttributeDecl(self, ast, c):
        sym = self.visit(ast.decl, c)
        c[0].append(sym)
        return sym


    def visitConstDecl(self, ast, c):
        if self.lookup(ast.constant, c[self.blockDepth], lambda x: x.name, 0):
            raise Redeclared(Attribute() if self.blockDepth == 0 else Constant(), ast.constant.name)
            
        # Raise error because constant variable can't be null
        if not ast.value:
            raise IllegalConstantExpression(None)  

        if type(ast.constType) == ClassType:
            if ast.constType.classname.name not in self.classMap:
                raise Undeclared(Class(), ast.constType.classname.name)

        self.isConstDecl = True
        name = ast.constant
        constType = ast.constType
        value = ast.value
        valueType, valueKind = self.visit(ast.value, c)

        if self.willRaiseError or valueKind == 'Var':
            raise IllegalConstantExpression(ast.value)

        # Raise error because type mismatch, except type coerce
        if str(valueType) != str(constType) and not (type(valueType) == IntType and type(constType) == FloatType):
                raise TypeMismatchInConstant(ast)

        self.isConstDecl = False
        return Symbol(name, constType, 'Const', value)


    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable, c[self.blockDepth], lambda x: x.name, 0):
            raise Redeclared(Attribute() if self.blockDepth == 0 else Variable(), ast.variable.name)

        name = ast.variable

        if type(ast.varType) == ClassType:
            if ast.varType.classname.name not in self.classMap:
                raise Undeclared(Class(), ast.varType.classname.name)

        value = ast.varInit
        varType = ast.varType
        valueType = self.visit(ast.varInit, c)[0] if ast.varInit else None

        # Raise error because type mismatch and if only there is value
        if valueType:
            if type(valueType) == NullLiteral:
                return Symbol(name, varType, 'Var', value) 
            elif str(valueType) != str(varType) and not (type(valueType) == IntType and type(varType) == FloatType):
                raise TypeMismatchInStatement(ast)

        return Symbol(name, varType, 'Var', value)


    def visitMethodDecl(self, ast, c):
        if self.lookup(ast.name, c[0], lambda x: x.name, 1):
            raise Redeclared(Method(), ast.name.name)

        # Check for parameter
        typeList = []
        c.append([]) # Extend from [[foo]] --> [[foo], [list of foo]]

        for i in ast.param:
            if self.lookup(i.variable, c[1], lambda x: x.name, 0):
                raise Redeclared(Parameter(), i.variable.name)
            c[1].append(self.visitParam(i, c))
            typeList.append(i.varType)

        if (str(ast.name.name) == 'main' and str(ast.kind) == 'Static') or str(ast.name.name) == 'Constructor':
            self.isInMain = True
        if str(ast.name.name) == 'Destructor':
            self.isInDestructor = True
        
        # Get the return type of that method
        returnType, returnKind = self.visit(ast.body, c)
        sym = Symbol(ast.name, MType(typeList, returnType), returnKind, None)
        c[0].append(sym)
        
        # Toggle flag and return
        if self.isInMain: self.isInMain = False
        if self.isInDestructor: self.isInDestructor = False
        return sym
    

    def visitParam(self, ast, c):
        if self.lookup(ast.variable, c[1], lambda x: x.name, 0):
            raise Redeclared(Parameter(), ast.variable.name)

        varType = ast.varType
        if type(varType) == ClassType:
            if varType.classname.name not in self.classMap:
                raise Undeclared(Class(), varType.classname.name)

        return Symbol(ast.variable, varType, 'Var', None)


    def visitBlock(self, ast, c, currReturn = VoidType()):
        retType = currReturn
        retKind = 'Var'

        self.blockDepth += 1
        
        for i in ast.inst:
            if isinstance(i, StoreDecl):
                c[self.blockDepth].append(self.visit(i, c))
            elif type(i) == Block:
                c.append([])
                currRetType, currRetKind = self.visitBlock(i, c, retType)
            elif type(i) == CallStmt:
                if type(self.visit(i, c)) != VoidType:
                    raise TypeMismatchInStatement(i)
            elif type(i) == Assign:
                self.visit(i, c) # Nothing should be returned
            elif type(i) in [For, If, Return]:
                currRetType, currRetKind = self.visit(i, c)
                if self.willRaiseError or (str(retType) != str(currRetType) and type(retType) != VoidType):
                    raise TypeMismatchInStatement(i)
                retType, retKind = currRetType, currRetKind
            else:  # Continue, Break
                self.visit(i, c)
        
        c.pop()
        self.blockDepth -= 1

        return retType, retKind

                                
    def visitCallStmt(self, ast, c):
        method = ast.method
        param = [self.visit(i, c)[0] for i in ast.param]
        self.checkClass = True

        # Static access
        if '$' in str(method.name):
            if ast.obj.name in self.classMap:
                x = self.lookup(method, self.classMap[ast.obj.name], lambda x: x.name, 1)
                if not x:
                    raise Undeclared(Method(), method.name)
                else:
                    Checker.checkParam(x.mtype.partype, param, ast)
                    if self.isConstDecl:
                        self.willRaiseError = True
            else:
                x = self.visit(ast.obj, c)[0]
                if x:
                    if type(x) == ClassType:
                        raise IllegalMemberAccess(ast)
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    raise Undeclared(Class(), ast.obj.name)
        # Instance access
        else:
            obj = self.visit(ast.obj, c)[0]
            if obj:
                if type(obj) == ClassType:
                    x = self.lookup(method, self.classMap[obj.classname.name], lambda x: x.name, 1)
                    if not x:
                        raise Undeclared(Method(), method.name)
                    else:
                        Checker.checkParam(x.mtype.partype, param, ast)
                        if self.isInLHS:
                            if str(x.declType) == 'Const':
                                self.willRaiseError = True
                        else:
                            if self.isConstDecl:
                                if str(x.declType) == 'Var':
                                    self.willRaiseError = True               
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                if ast.obj.name in self.classMap:
                    raise IllegalMemberAccess(ast)
                else:
                    raise Undeclared(Identifier(), ast.obj.name)
        self.checkClass = False
        return x.mtype.rettype

    def visitReturn(self, ast, c):
        if self.isInDestructor or (self.isInMain and ast.expr):
            raise TypeMismatchInStatement(ast)
        
        if ast.expr:
            ret = self.visit(ast.expr, c)
            return ret[0], ret[1]
        return VoidType(), None


    def visitContinue(self, ast, c):
        if self.loopDepth <= 0: raise MustInLoop(ast) 


    def visitBreak(self, ast, c):
        if self.loopDepth <= 0: raise MustInLoop(ast)


    def visitFor(self, ast, c):
        self.isInLHS = True # Toggle LHS flag for Id
        scalar, scalarKind = self.visit(ast.id, c)
        self.isInLHS = False

        if scalarKind == 'Const':
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))

        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        expr3 = self.visit(ast.expr3, c)

        if not all(isinstance(x, IntType) for x in [scalar, expr1[0], expr2[0], expr3[0]]):
            raise TypeMismatchInStatement(ast)

        # Check loop block
        c.append([])
        self.loopDepth += 1
        ret = self.visit(ast.loop, c)
        self.loopDepth -= 1

        return ret if ret else None


    def visitIf(self, ast, c):
        evaType = self.visit(ast.expr, c)[0]
        if type(evaType) != BoolType:
            self.willRaiseError = True
        
        c.append([])
        thenRet = self.visit(ast.thenStmt, c)[0]

        # Only If {}
        if ast.elseStmt:
            c.append([])
            elseRet = self.visit(ast.elseStmt, c)[0]

            if type(thenRet) != type(elseRet):
                raise TypeMismatchInStatement(ast)
            return (elseRet, None)
        else:
            return (thenRet, None)


    def visitAssign(self, ast, c):
        # rhs first because rhs will be checked before lhs
        # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158007
        rhsType = self.visit(ast.exp, c)[0]
        
        self.isInLHS = True
        lhsType = self.visit(ast.lhs, c)[0]
        
        if self.willRaiseError:
            raise CannotAssignToConstant(ast)
        self.isInLHS = False

        # Type-cast a stmt: FloatType = IntType 
        if type(lhsType) == FloatType and type(rhsType) == IntType:
            return

        if str(lhsType) != str(rhsType):
            raise TypeMismatchInStatement(ast)


    def visitBinaryOp(self, ast, c):
        lType, lKind = self.visit(ast.left, c)
        rType, rKind = self.visit(ast.right, c)
        op = ast.op

        retKind = 'Const'
        if lKind == 'Var' or rKind == 'Var':
            retKind = 'Var'

        # Operands can either be Float or Int, but not other
        if op in ['+', '-', '*', '/']:
            if (type(lType) == FloatType and type(rType) == FloatType)\
            or (type(lType) == FloatType and type(rType) == IntType)\
            or (type(lType) == IntType and type(rType) == FloatType):
                return FloatType(), retKind
            elif type(lType) == IntType and type(rType) == IntType:
                return IntType(), retKind
        # Operands must be both Int
        elif op == '%':
            if type(lType) == IntType and type(rType) == IntType:
                return IntType(), retKind
        # Operands must be both Boolean
        elif op in ['&&', '||']:
            if type(lType) == BoolType and type(rType) == BoolType:   
                return BoolType(), retKind
        # Operands must be both String
        elif op == '+.':
            if type(lType) == StringType and type(rType) == StringType:   
                return StringType(), retKind
        # Operands must be both String
        elif op == '==.':
            if type(lType) == StringType and type(rType) == StringType:   
                return BoolType(), retKind
        # Operands must be Int-Float or Boolean only
        elif op in ['==', '!=']:
            if type(lType) in [IntType, BoolType] and type(lType) == type(rType):
                return BoolType(), retKind
        # Operands can either be Float or Int, but not other
        elif op in ['<', '<=', '>', '>=']:
            if type(lType) in [IntType, FloatType] and type(rType) in [IntType, FloatType]:
                return BoolType(), retKind
        # If none of above is valid, raise type mismatch in this expression
        raise TypeMismatchInExpression(ast)


    def visitUnaryOp(self, ast, c):
        unTyp, unKind = self.visit(ast.body, c)
        op = ast.op
        retKind = 'Const'
        if unKind == 'Var': retKind = 'Var'

        if op == '-':
            if type(unTyp) == IntType: return IntType(), retKind
            elif type(unTyp) == FloatType: return FloatType(), retKind
        elif op == '!':
            if type(unTyp) == BoolType: return BoolType(), retKind
        raise TypeMismatchInExpression(ast)


    def visitCallExpr(self, ast, c):
        method = ast.method
        param = [self.visit(i, c)[0] for i in ast.param]
        self.checkClass = True

        # Static access
        if '$' in str(method.name):
            if ast.obj.name in self.classMap:
                x = self.lookup(method, self.classMap[ast.obj.name], lambda x: x.name, 1)
                if not x:
                    raise Undeclared(Method(), method.name)
                else:
                    Checker.checkParam(x.mtype.partype, param, ast)     
            else:
                x = self.visit(ast.obj, c)[0]
                if x:
                    if type(x) == ClassType:
                        raise IllegalMemberAccess(ast)
                    else:
                        raise TypeMismatchInExpression(ast)
                else:
                    raise Undeclared(Class(), ast.obj.name)
        # Instance access
        else:
            obj = self.visit(ast.obj, c)[0]
            if obj:
                if type(obj) == ClassType:
                    x = self.lookup(method, self.classMap[obj.classname.name], lambda x: x.name, 1)
                    if not x:
                        raise Undeclared(Method(), method.name)
                    Checker.checkParam(x.mtype.partype, param, ast)
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                if ast.obj.name in self.classMap:
                    raise IllegalMemberAccess(ast)
                else:
                    raise Undeclared(Identifier(), ast.obj.name)
        
        self.checkClass = False
        return x.mtype.rettype, x.declType


    def visitNewExpr(self, ast, c):
        # Check undeclared class
        if ast.classname.name not in self.classMap:
            raise Undeclared(Class(), ast.classname.name)
        # Declared
        else:
            paramList = [self.visit(i, c)[0] for i in ast.param]
            constructor = self.lookup(Id('Constructor'), self.classMap[ast.classname.name], lambda x: x.name, 1)

            # Provide that class a default Constructor
            if not constructor:
                if paramList:
                    raise TypeMismatchInExpression(ast)
            else:
                Checker.checkParam(constructor.mtype.partype, paramList, ast)
        return ClassType(ast.classname), 'Var'


    def visitArrayCell(self, ast, c):
        arr, arrKind = self.visit(ast.arr, c)
        idx = [self.visit(i, c)[0] for i in ast.idx]

        # Subscripting the incorrect type (Not IntType)
        if type(arr) != ArrayType or not all(isinstance(i, IntType) for i in idx):
            raise TypeMismatchInExpression(ast)
        return self.processArrayCell(arr, c, len(idx) - 1, arrKind)


    def processArrayCell(self, ast, c, depth, kind):
        if depth > 0 and type(ast.eleType) == ArrayType:
            return self.processArrayCell(ast.eleType, c, depth - 1, kind)
        return ast.eleType, kind


    def visitFieldAccess(self, ast, c):
        fieldname = ast.fieldname
        self.checkClass = True

        if '$' in str(fieldname.name):
            if ast.obj.name in self.classMap:
                x = self.lookup(fieldname, self.classMap[ast.obj.name], lambda x: x.name, 0)
                if not x: raise Undeclared(Attribute(), fieldname.name)
                else:
                    if self.isInLHS and str(x.declType) == 'Const': self.willRaiseError = True
                    elif self.isConstDecl and str(x.declType) == 'Var': self.willRaiseError = True
            else:
                x = self.visit(ast.obj, c)[0]
                if x: raise IllegalMemberAccess(ast) if type(x) == ClassType else TypeMismatchInExpression(ast)
                else: raise Undeclared(Class(), ast.obj.name)
        else:
            obj = self.visit(ast.obj, c)[0]
            if obj:
                if type(obj) == ClassType:
                    x = self.lookup(fieldname, self.classMap[obj.classname.name], lambda x: x.name, 0)
                    if not x:
                        raise Undeclared(Attribute(), fieldname.name)
                    else:
                        if self.isInLHS and str(x.declType) == 'Const': self.willRaiseError = True
                        elif self.isConstDecl:
                            if str(x.declType) == 'Var': self.willRaiseError = True        
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise IllegalMemberAccess(ast) if ast.obj.name in self.classMap else Undeclared(Identifier(), ast.obj.name)
        self.checkClass = False
        return x.mtype, x.declType


    def visitId(self, ast, c):
        # Exclude the first element (Class members) and traverse the stack from the top
        for i in reversed(c[1:]):
            x = self.lookup(ast, i, lambda x: x.name, 0)
            if x: 
                if self.isInLHS:
                    if str(x.declType) == 'Const':
                        self.willRaiseError = True
                else:
                    if self.isConstDecl and str(x.declType) == 'Var':
                        if not self.checkClass:
                            self.willRaiseError = True 
                return x.mtype, x.declType
        if self.checkClass:
            return (None, None)
        raise Undeclared(Identifier(), ast.name)

    def visitIntLiteral(self, ast, c):
        return IntType(), 'Const'

    def visitFloatLiteral(self, ast, c):
        return FloatType(), 'Const'

    def visitBooleanLiteral(self, ast, c):
        return BoolType(), 'Const'

    def visitStringLiteral(self, ast, c):
        return StringType(), 'Const'
    
    def visitArrayLiteral(self, ast, c):
        # Check if all element in the list is the same type as first one
        typList = [str(self.visit(i, c)[0]) for i in ast.value]

        if len(set(typList)) == 1:
            return ArrayType(len(ast.value), typList[0]), 'Const'
        else:
            raise IllegalArrayLiteral(ast)

    def visitSelfLiteral(self, ast, c):
        return ClassType(Id(list(self.classMap)[-1])), 'Var'

    def visitNullLiteral(self, ast, c):
        return NullLiteral(), 'Const'