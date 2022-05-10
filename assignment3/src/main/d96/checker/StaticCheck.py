# Student ID: 1953097

"""
 * @author nhphung
"""

from AST import * 
from Visitor import *
#from Utils import Utils
from StaticError import *

class Utils:
    def lookup(self, name, lst, func, flag):
        # FLAG: 
        # 0 for Attribute/VarDecl/ConstDecl and 1 for Method
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
    def checkParam(left, right):
        # Left: x.mtype.partype (accept side)
        # Right: param (to be passed side)
        if len(left) != len(right):
            return False
        
        for i, j in zip(left, right):
            if str(i) != str(j):
                if not (type(i) == ClassType and type(j) == NullLiteral)\
                and (type(i) == NullLiteral and type(j) == ClassType)\
                and (type(i) == FloatType and type(j) == IntType):
                    return False
        return True
    
    # @staticmethod
    # def fprint(c, blockDepth):
    #     for i in c:
    #         print("[" + ' --> '.join([str(j) for j in i]) +"]")
    #     print(f"Current block depth: {blockDepth}")

    # @staticmethod
    # def cprint(currMap):
    #     for i, j in currMap.items():
    #         print(f"{i}: {[str(k) for k in j]}")


class StaticChecker(BaseVisitor,Utils):
    global_envi = []

    def __init__(self,ast):
        self.classMap = {}
        self.blockDepth = 0
        self.loopDepth = 0
        self.isInMain = False
        self.isInLHS = False
        self.isConstDecl = False
        self.checkStatic = False
        self.willRaiseError = False
        self.checkClass = False
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
                self.classMap[x.classname.name] = []
                self.visit(x, self.classMap)

        # Check no entry
        if 'Program' not in self.classMap:
            raise NoEntryPoint()

        # Print current self.classMap
        # Checker.cprint(self.classMap)

        return []

    # class ClassDecl(Decl):
    # classname: Id
    # memlist: List[MemDecl]
    # parentname: Id = None  # None if there is no parent
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

    # class AttributeDecl(MemDecl):
    # kind: SIKind 
    # decl: StoreDecl 
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
            # print(f"type(ast.value) = {type(valueType)}")
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

        # Classtype and Undeclared Class
        
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

    # class MethodDecl(MemDecl):
    # kind: SIKind
    # name: Id
    # param: List[VarDecl]
    # body: Block
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
        sym = Symbol(ast.name, MType(typeList, []), None, None)
        c[0].append(sym)

        # Get the return type of that method
        # Entry function: main()
        if str(ast.name.name) == 'main' and str(ast.kind) == 'Static':
            self.isInMain = True
        if str(ast.name.name) == 'Constructor' or str(ast.name.name) == 'Destructor':
            self.isInMain = True

        returnType = self.visit(ast.body, c)
        
        if self.isInMain:
            if not returnType or type(returnType) != VoidType:
                raise TypeMismatchInStatement(ast)
            else:
                self.isInMain = False

        sym.mtype.rettype = returnType

        return sym

    def visitParam(self, ast, c):
        if self.lookup(ast.variable, c[1], lambda x: x.name, 0):
            raise Redeclared(Parameter(), ast.variable.name)

        name = ast.variable
        varType = ast.varType
        value = ast.varInit
        valueType = self.visit(ast.varInit, c) if ast.varInit else None

        # Raise error because type mismatch and if only there is value
        if valueType:
            if type(valueType) != type(varType):
                raise TypeMismatchInStatement(ast)

        return Symbol(name, varType, 'Var', value)

    # class Block(Stmt):
    # inst: List[Inst]
    def visitBlock(self, ast, c):
        #print(f"===================== {ast} ======================\n")
        retType = None

        self.blockDepth += 1
        
        for i in ast.inst:
            if isinstance(i, StoreDecl):
                c[self.blockDepth].append(self.visit(i, c))
            elif type(i) == Block:
                c.append([])
                retType = self.visit(i, c)
            elif type(i) == CallStmt:
                callType = self.visit(i, c)
                if type(callType) != VoidType:
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
            else: 
                retType = self.visit(i, c)
        
        # Checker.fprint(c)
        c.pop()
        self.blockDepth -= 1

        #print(f"================== End of {ast} ===================\n")
        if self.blockDepth == 0:
            return retType if retType else VoidType()
        else:
            return retType

    # class CallStmt(Stmt):
    # obj: Expr
    # method: Id
    # param: List[Expr]                                      
    def visitCallStmt(self, ast, c):
        method = ast.method
        param = [self.visit(i, c) for i in ast.param]

        # Static access
        if '$' in str(method.name):
            self.checkStatic = True
            if ast.obj.name in self.classMap:
                x = self.lookup(method, self.classMap[ast.obj.name], lambda x: x.name, 1)
                if not x:
                    raise Undeclared(Method(), method.name)
                else:
                    if not Checker.checkParam(x.mtype.partype, param):
                        raise TypeMismatchInStatement(ast)
                    else:
                        if self.isConstDecl:
                            self.willRaiseError = True
                        self.checkStatic = False
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
                                if not Checker.checkParam(x.mtype.partype, param):
                                    raise TypeMismatchInStatement(ast)
                                self.checkClass = False
                                return x.mtype.rettype
                        else:
                            if self.isConstDecl:
                                if str(x.declType) == 'Var':
                                    self.willRaiseError = True
                                    return x.mtype
                            else:
                                if not Checker.checkParam(x.mtype.partype, param):
                                    raise TypeMismatchInStatement(ast)
                                self.checkClass = False
                                return x.mtype.rettype
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                if ast.obj.name in self.classMap:
                    raise IllegalMemberAccess(ast)
                else:
                    raise Undeclared(Identifier(), ast.obj.name)

    # class Return(Stmt):
    # expr: Expr = None
    def visitReturn(self, ast, c):
        return self.visit(ast.expr, c) if ast.expr else None

    # Continue stmt
    def visitContinue(self, ast, c):
        if self.loopDepth > 0:
            return
        raise MustInLoop(ast) 

    # Break stmt
    def visitBreak(self, ast, c):
        if self.loopDepth > 0:
            return
        raise MustInLoop(ast)

    # class For(Stmt):
    # id: Id
    # expr1: Expr
    # expr2: Expr 
    # loop: Stmt
    # expr3: Expr = None
    def visitFor(self, ast, c):
        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        expr3 = self.visit(ast.expr3, c)

        if type(expr1) != IntType or type(expr2) != IntType or type(expr3) != IntType:
            raise TypeMismatchInStatement(ast)

        scalar = Symbol(ast.id, IntType(), 'Var', expr1)

        # Check loop block
        c.append([scalar])
        self.loopDepth += 1
        ret = self.visit(ast.loop, c)
        self.loopDepth -= 1

        return ret if ret else None

    # class If(Stmt):
    # expr: Expr
    # thenStmt: Stmt
    # elseStmt: Stmt = None  # None if there is no else branch
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

    # class Assign(Stmt):
    # lhs: Expr
    # exp: Expr
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
            if type(lType) == type(rType):
                if type(lType) in [IntType, BoolType]:
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

    # class CallExpr(Expr):
    # obj: Expr
    # method: Id
    # param: List[Expr]
    def visitCallExpr(self, ast, c):
        method = ast.method
        param = [self.visit(i, c) for i in ast.param]

        # Static access
        if '$' in str(method.name):
            self.checkStatic = True
            if ast.obj.name in self.classMap:
                x = self.lookup(method, self.classMap[ast.obj.name], lambda x: x.name, 1)
                if not x:
                    raise Undeclared(Method(), method.name)
                else:
                    if not Checker.checkParam(x.mtype.partype, param):
                        raise TypeMismatchInExpression(ast)
                    else:
                        if self.isConstDecl:
                            self.willRaiseError = True
                        self.checkStatic = False
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
                        return x.mtype.rettype
                    else:
                        if not Checker.checkParam(x.mtype.partype, param):
                            raise TypeMismatchInExpression(ast)
                        self.checkClass = False
                        return x.mtype.rettype
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                if ast.obj.name in self.classMap:
                    raise IllegalMemberAccess(ast)
                else:
                    raise Undeclared(Identifier(), ast.obj.name)

    # class NewExpr(Expr):
    # classname: Id
    # param: List[Expr]
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

    # class ArrayCell(LHS):
    # arr: Expr
    # idx: List[Expr]
    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr, c)
        idx = [self.visit(i, c) for i in ast.idx]

        # Not in array type
        if type(arr) != ArrayType:
            raise TypeMismatchInExpression(ast)

        # Subscripting the incorrect type (Not IntType)
        if not all(isinstance(i, IntType) for i in idx):
            raise TypeMismatchInExpression(ast)

        return self.processArrayCell(arr, c, len(idx) - 1)

    # size: int
    # eleType: Type
    def processArrayCell(self, ast, c, depth):
        if depth > 0:
            if type(ast.eleType) == ArrayType:
                return self.processArrayCell(ast.eleType, c, depth - 1)
            else:
                return ast.eleType
        else:
            return ast.eleType

    def visitFieldAccess(self, ast, c):
        # obj: Expr
        # fieldname: Id
        fieldname = ast.fieldname

        if '$' in str(fieldname.name):
            self.checkStatic = True
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
                    self.checkStatic = False
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

    # <--- Type visitor --->
    # class Id(LHS):
    # name: str
    def visitId(self, ast, c):
        # Exclude the first element and traverse the stack from the top
        for i in reversed(c[1:]):
            x = self.lookup(ast, i, lambda x: x.name, 0)
            if x: 
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
                            return x.mtype                    
                    return x.mtype
        if self.checkStatic or self.checkClass:
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
    
    # class ArrayLiteral(Literal):
    # value: List[Expr]
    def visitArrayLiteral(self, ast, c):
        # Raise Type mismatch if length of array literal is 0
        if len(ast.value) == 0:
            raise IllegalArrayLiteral(ast)

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
    