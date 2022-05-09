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
            if ast.parentname.name not in self.classMap:
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
            if self.blockDepth == 0: # For Attribute at bottom of stack
                raise Redeclared(Attribute(), ast.constant.name)
            else:
                raise Redeclared(Constant(), ast.constant.name)
            
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
        valueType = self.visit(ast.value, c)

        if self.willRaiseError:
            raise IllegalConstantExpression(ast.value)

        # Raise error because type mismatch, except type coerce
        if str(valueType) != str(constType):
            if not (type(valueType) == IntType and type(constType) == FloatType):
                raise TypeMismatchInConstant(ast)
        self.isConstDecl = False

        return Symbol(name, constType, 'Const', value)


    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable, c[self.blockDepth], lambda x: x.name, 0):
            if self.blockDepth == 0: # For Attribute at bottom of stack
                raise Redeclared(Attribute(), ast.variable.name)
            else:
                raise Redeclared(Variable(), ast.variable.name)

        name = ast.variable

        if type(ast.varType) == ClassType:
            if ast.varType.classname.name not in self.classMap:
                raise Undeclared(Class(), ast.varType.classname.name)

        value = ast.varInit
        varType = ast.varType
        valueType = self.visit(ast.varInit, c) if ast.varInit else None

        # Raise error because type mismatch and if only there is value
        if valueType:
            if type(valueType) == NullLiteral:
                return Symbol(name, varType, 'Var', value) 
            if str(valueType) != str(varType):
                if not (type(valueType) == IntType and type(varType) == FloatType):
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

        # Create a new symbol and immediately pass into the body block
        sym = Symbol(ast.name, MType(typeList, []), 'Const', None)
        c[0].append(sym)

        if (str(ast.name.name) == 'main' and str(ast.kind) == 'Static') or str(ast.name.name) == 'Constructor':
            self.isInMain = True
        if str(ast.name.name) == 'Destructor':
            self.isInDestructor = True
        
        # Get the return type of that method
        returnType = self.visit(ast.body, c)
        
        # Toggle flag
        if self.isInMain: self.isInMain = False
        if self.isInDestructor: self.isInDestructor = False

        sym.mtype.rettype = returnType

        return sym
    

    def visitParam(self, ast, c):
        if self.lookup(ast.variable, c[1], lambda x: x.name, 0):
            raise Redeclared(Parameter(), ast.variable.name)

        varType = ast.varType
        if type(varType) == ClassType:
            if varType.classname.name not in self.classMap:
                raise Undeclared(Class(), varType.classname.name)

        return Symbol(ast.variable, varType, 'Var', None)


    def visitBlock(self, ast, c):
        retType = None

        self.blockDepth += 1
        
        for i in ast.inst:
            if isinstance(i, StoreDecl):
                c[self.blockDepth].append(self.visit(i, c))
            elif type(i) == Block:
                c.append([])
                retType = self.visit(i, c)
            elif type(i) == CallStmt:
                if type(self.visit(i, c)) != VoidType:
                    raise TypeMismatchInStatement(i)
            elif type(i) == Assign:
                self.visit(i, c) # Nothing should be returned
            elif type(i) in [Return, For, If]:
                currRetType = self.visit(i, c)

                if self.willRaiseError:
                    raise TypeMismatchInStatement(i)

                if not retType:
                    retType = currRetType
                else:
                    if str(retType) != str(currRetType):
                        raise TypeMismatchInStatement(i)
            else:  # Continue, Break
                self.visit(i, c)
        
        c.pop()
        self.blockDepth -= 1

        if self.blockDepth == 0:
            return retType if retType else VoidType()
        else:
            return retType

                                
    def visitCallStmt(self, ast, c):
        method = ast.method
        param = [self.visit(i, c) for i in ast.param]

        # Static access
        if '$' in str(method.name):
            self.checkClass = True
            if ast.obj.name in self.classMap:
                x = self.lookup(method, self.classMap[ast.obj.name], lambda x: x.name, 1)
                if not x:
                    raise Undeclared(Method(), method.name)
                else:
                    Checker.checkParam(x.mtype.partype, param, ast)
                    if self.isConstDecl:
                        self.willRaiseError = True
                    self.checkClass = False
                    return x.mtype.rettype
            else:
                x = self.visit(ast.obj, c)
                if x:
                    if type(x) == ClassType:
                        raise IllegalMemberAccess(ast)
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    raise Undeclared(Class(), ast.obj.name)
        # Instance access
        else:
            self.checkClass = True
            obj = self.visit(ast.obj, c)
            if obj:
                if type(obj) == ClassType:
                    x = self.lookup(method, self.classMap[obj.classname.name], lambda x: x.name, 1)
                    if not x:
                        raise Undeclared(Method(), method.name)
                    else:
                        if self.isInLHS:
                            if str(x.declType) == 'Const':
                                self.willRaiseError = True
                                return x.mtype.rettype
                            else:
                                Checker.checkParam(x.mtype.partype, param, ast)
                                self.checkClass = False
                                return x.mtype.rettype
                        else:
                            if self.isConstDecl:
                                if str(x.declType) == 'Var':
                                    self.willRaiseError = True
                                    return x.mtype
                            else:
                                Checker.checkParam(x.mtype.partype, param, ast)

                                self.checkClass = False
                                return x.mtype.rettype
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                if ast.obj.name in self.classMap:
                    raise IllegalMemberAccess(ast)
                else:
                    raise Undeclared(Identifier(), ast.obj.name)


    def visitReturn(self, ast, c):
        if self.isInDestructor or (self.isInMain and ast.expr):
            raise TypeMismatchInStatement(ast)
        return self.visit(ast.expr, c) if ast.expr else None


    def visitContinue(self, ast, c):
        if self.loopDepth <= 0: raise MustInLoop(ast) 


    def visitBreak(self, ast, c):
        if self.loopDepth <= 0: raise MustInLoop(ast)


    def visitFor(self, ast, c):
        self.isInLHS = True # Toggle LHS flag for Id
        scalar = self.visit(ast.id, c)
        self.isInLHS = False

        if self.willRaiseError:
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))

        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        expr3 = self.visit(ast.expr3, c)


        if not all(isinstance(x, IntType) for x in [scalar, expr1, expr2, expr3]):
            raise TypeMismatchInStatement(ast)

        # Check loop block
        c.append([])
        self.loopDepth += 1
        ret = self.visit(ast.loop, c)
        self.loopDepth -= 1

        return ret if ret else None


    def visitIf(self, ast, c):
        evaType = self.visit(ast.expr, c)
        if type(evaType) != BoolType:
            self.willRaiseError = True
            return None
        
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


    def visitAssign(self, ast, c):
        # rhs first because rhs will be checked before lhs
        # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158007
        rhsType = self.visit(ast.exp, c)
        
        self.isInLHS = True
        lhsType = self.visit(ast.lhs, c)
        
        if self.willRaiseError:
            raise CannotAssignToConstant(ast)
        self.isInLHS = False

        # Type-cast a stmt: FloatType = IntType 
        if type(lhsType) == FloatType and type(rhsType) == IntType:
            return

        if str(lhsType) != str(rhsType):
            raise TypeMismatchInStatement(ast)


    def visitBinaryOp(self, ast, c):
        lType = self.visit(ast.left, c)
        rType = self.visit(ast.right, c)
        op = ast.op

        # Operands can either be Float or Int, but not other
        if op in ['+', '-', '*', '/']:
            if (type(lType) == FloatType and type(rType) == FloatType)\
            or (type(lType) == FloatType and type(rType) == IntType)\
            or (type(lType) == IntType and type(rType) == FloatType):
                return FloatType()
            elif type(lType) == IntType and type(rType) == IntType:
                return IntType()
        # Operands must be both Int
        elif op == '%':
            if type(lType) == IntType and type(rType) == IntType:
                return IntType()
        # Operands must be both Boolean
        elif op in ['&&', '||']:
            if type(lType) == BoolType and type(rType) == BoolType:   
                return BoolType()
        # Operands must be both String
        elif op == '+.':
            if type(lType) == StringType and type(rType) == StringType:   
                return StringType()       
        # Operands must be both String
        elif op == '==.':
            if type(lType) == StringType and type(rType) == StringType:   
                return BoolType()     
        # Operands must be Int-Float or Boolean only
        elif op in ['==', '!=']:
            if type(lType) in [IntType, BoolType] and type(lType) == type(rType):
                return BoolType()
        # Operands can either be Float or Int, but not other
        elif op in ['<', '<=', '>', '>=']:
            if type(lType) in [IntType, FloatType] and type(rType) in [IntType, FloatType]:
                return BoolType()
        # If none of above is valid, raise type mismatch in this expression
        raise TypeMismatchInExpression(ast)


    def visitUnaryOp(self, ast, c):
        unTyp = self.visit(ast.body, c)
        op = ast.op

        if op == '-':
            if type(unTyp) == IntType: return IntType()
            elif type(unTyp) == FloatType: return FloatType()
        elif op == '!':
            if type(unTyp) == BoolType: return BoolType()
        raise TypeMismatchInExpression(ast)


    def visitCallExpr(self, ast, c):
        method = ast.method
        param = [self.visit(i, c) for i in ast.param]

        # Static access
        if '$' in str(method.name):
            self.checkClass = True
            if ast.obj.name in self.classMap:
                x = self.lookup(method, self.classMap[ast.obj.name], lambda x: x.name, 1)
                if not x:
                    raise Undeclared(Method(), method.name)
                else:
                    Checker.checkParam(x.mtype.partype, param, ast)
                    
                    if self.isConstDecl:
                        self.willRaiseError = True
                    self.checkClass = False
                    return x.mtype.rettype
            else:
                x = self.visit(ast.obj, c)
                if x:
                    if type(x) == ClassType:
                        raise IllegalMemberAccess(ast)
                    else:
                        raise TypeMismatchInExpression(ast)
                else:
                    raise Undeclared(Class(), ast.obj.name)
        # Instance access
        else:
            self.checkClass = True
            obj = self.visit(ast.obj, c)
            if obj:
                if type(obj) == ClassType:
                    x = self.lookup(method, self.classMap[obj.classname.name], lambda x: x.name, 1)
                    if not x:
                        raise Undeclared(Method(), method.name)
                    if self.isConstDecl:
                        if str(x.declType) == 'Var':
                            self.willRaiseError = True
                        Checker.checkParam(x.mtype.partype, param, ast)
                        return x.mtype.rettype
                    else:
                        Checker.checkParam(x.mtype.partype, param, ast)

                        self.checkClass = False
                        return x.mtype.rettype
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                if ast.obj.name in self.classMap:
                    raise IllegalMemberAccess(ast)
                else:
                    raise Undeclared(Identifier(), ast.obj.name)


    def visitNewExpr(self, ast, c):
        # Check undeclared class
        if ast.classname.name not in self.classMap:
            raise Undeclared(Class(), ast.classname.name)
        # Declared
        else:
            paramList = [self.visit(i, c) for i in ast.param]
            constructor = self.lookup(Id('Constructor'), self.classMap[ast.classname.name], lambda x: x.name, 1)

            # Provide that class a default Constructor
            if not constructor:
                # Provide something to a default Constructor, which has no param
                if paramList:
                    raise TypeMismatchInExpression(ast)
            else:
                if paramList != constructor.mtype.partype:
                    raise TypeMismatchInExpression(ast) 
            return ClassType(ast.classname)


    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr, c)
        idx = [self.visit(i, c) for i in ast.idx]

        # Subscripting the incorrect type (Not IntType)
        if type(arr) != ArrayType or not all(isinstance(i, IntType) for i in idx):
            raise TypeMismatchInExpression(ast)
        return self.processArrayCell(arr, c, len(idx) - 1)


    def processArrayCell(self, ast, c, depth):
        if depth > 0:
            if type(ast.eleType) == ArrayType:
                return self.processArrayCell(ast.eleType, c, depth - 1)
            else:
                return ast.eleType
        else:
            return ast.eleType


    def visitFieldAccess(self, ast, c):
        fieldname = ast.fieldname

        if '$' in str(fieldname.name):
            self.checkClass = True
            if ast.obj.name in self.classMap:
                x = self.lookup(fieldname, self.classMap[ast.obj.name], lambda x: x.name, 0)
                if not x:
                    raise Undeclared(Attribute(), fieldname.name)
                # The only case where it would work
                else:
                    if self.isInLHS:
                        if str(x.declType) == 'Const':
                            self.willRaiseError = True
                            return x.mtype
                        else:
                            return x.mtype
                    else:
                        if self.isConstDecl:
                            if str(x.declType) == 'Var':
                                self.willRaiseError = True
                    self.checkClass = False
                    return x.mtype
            else:
                x = self.visit(ast.obj, c)
                if x:
                    if type(x) == ClassType:
                        raise IllegalMemberAccess(ast)
                    else:
                        raise TypeMismatchInExpression(ast)
                else:
                    raise Undeclared(Class(), ast.obj.name)
        else:
            self.checkClass = True
            obj = self.visit(ast.obj, c)
            if obj:
                if type(obj) == ClassType:
                    x = self.lookup(fieldname, self.classMap[obj.classname.name], lambda x: x.name, 0)
                    if not x:
                        raise Undeclared(Attribute(), fieldname.name)
                    else:
                        if self.isInLHS:
                            if str(x.declType) == 'Const':
                                self.willRaiseError = True
                                return x.mtype
                            else: # The only possible case
                                self.checkClass = False
                                return x.mtype
                        else:
                            if self.isConstDecl:
                                if str(x.declType) == 'Var':
                                    self.willRaiseError = True
                                    return x.mtype
                                else:
                                    self.checkClass = False
                                    return x.mtype
                            else:
                                self.checkClass = False
                                return x.mtype
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                if ast.obj.name in self.classMap:
                    raise IllegalMemberAccess(ast)
                else:
                    raise Undeclared(Identifier(), ast.obj.name)


    def visitId(self, ast, c):
        # Exclude the first element (Class members) and traverse the stack from the top
        for i in reversed(c[1:]):
            x = self.lookup(ast, i, lambda x: x.name, 0)
            if x: 
                if self.isInLHS:
                    if str(x.declType) == 'Const':
                        self.willRaiseError = True
                    return x.mtype
                else:
                    if self.isConstDecl and str(x.declType) == 'Var':
                        self.willRaiseError = True     
                    return x.mtype
        if self.checkClass:
            return None
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
        # Check if all element in the list is the same type as first one
        typList = [str(self.visit(i, c)) for i in ast.value]

        if len(set(typList)) == 1:
            return ArrayType(len(ast.value), typList[0])
        else:
            raise IllegalArrayLiteral(ast)


    def visitSelfLiteral(self, ast, c):
        return ClassType(Id(list(self.classMap)[-1]))


    def visitNullLiteral(self, ast, c):
        return NullLiteral()
    