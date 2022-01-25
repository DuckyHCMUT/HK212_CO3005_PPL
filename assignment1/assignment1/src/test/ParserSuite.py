import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_bkel_1_301(self):
        input = """Class main{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,301))

    def test_bkel_2_302(self):
        input = """
    Class Rectangle: Shape {
        getArea() {
            Return Self.length * Self.width;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,302))

    def test_bkel_3_303(self):
        input = """
    Class Shape {
        $getNumOfShape( {
            Return Self.length * Self.width;
        }
    }
        """
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input, expect,303))

    def test_304(self):
        input = """abc = 1;"""
        expect = "Error on line 1 col 0: abc"
        self.assertTrue(TestParser.test(input, expect,304))
    
    # Test with normal class declaration and comment
    def test_305(self):
        input = """
    Class Shape: Rectangle {
        ##
        This part should be ignored, just to check, nothing to comment
        ##
        $getSomething(yes: Int){
            Var x : Int=0;
            Self.x = 1;
            Return x;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,305))

    # Test with equal number of variable and value
    def test_306(self):
        input = """
    Class Rectangle: Shape{
        ##
        Get area of a Rectangle
        ##
        Val length, width, k: Float = 20.3, 10.1, 1.2;
        getArea(){
            Val area: Float = length*width*k;
            Return area;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 306))

    # Test with unequal number of variable and value
    def test_307(self):
        input = """
    Class Rectangle: Shape{
        ##
        Get area of a Rectangle
        ##
        Val length, width: Float = 20.31, 1.2, 3.E-8;
        getArea(){
            Val area: Float = length*width;
            Return area;
        }
    }
        """
        expect = "Error on line 6 col 45: ,"
        self.assertTrue(TestParser.test(input, expect, 307))

    # Test case with 1 class, comment and array declaration
    def test_308(self):
        input = """
        Class Rectangle: Shape{
            ## Var somewhat: Int = 2;##
            Val myArray: Array[Float, 3];
                getArray(){
                    Return myArray;
            }
        }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 308))
    
    # Testcase from Justince, original version
    def test_309(self):
        input = """
        Class Trt{
            Var a: String;
            Constructor(x: String){
                Self.a = x;
            }
            Despacito(){
                Return Self.a +. "2";
            }
        }
        Class Shape {
            Var flag: Trt = Null;
            Var x, y : Int;
            Constructor(a,b: Int; d: String){
                flag = New Trt(d);
                Var s: String = flag.Despacito();
                Self.x = b;
                Self.y = a;
                If(d ==. "Hel"){
                    Self.x = a;
                    Self.y = b;
                }
            }
            Destructor(){
                print("No service");
            }
        }
        Class Program {
            ## Muda
            Muda ##
            Var hello: Array[Int, 5];
            Var length, width: Int;
            Var flag2: Shape = New Shape(1,2,"Help");
            main(){
                print(flag2.flag.Despacito());
                flag2.flag.a = "s";
                a = 1.0;
            }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect,309))

    # Testcase from Justince, complicated with declaration
    def test_310(self):
        input = """
    Class Trt{
        Var $a: String;
        Val $a, b: Int;
        Var a: Int = 10;
        Val b, c: Float = 1.5, 3.E8;
        Var x, y, z: Shape = Null, what, ok;
        Constructor(x, y: String; z: Int){
            Var s: Int = 1;
            Self.a = x;
        }
        Despacito(){
            Var b: String = a.foo().a.foo();
            Var c: Int = flag.foo;
            Var d: Float = flag.otherflag.foo();
            Return Self.a +. "2";
        }
    }
    Class Shape {
        Var flag: Trt = Null;
        Var x, y : Int;
        Constructor(a,b: Int; d: String){
            flag = New Trt(d);
            Var s: String = flag.Despacito();
            Self.x = b;
            Self.y = a;
            If(d ==. "Hel"){
                Self.x = a;
                Self.y = b;
            }
        }
        Destructor(){
            print("No service");
        }
    }
    Class Program {
        ## Muda
        Muda ##
        Var hello,hello2: Array[Int, 5], Array[Float, 2];
        Var length, width: Int;
        Var flag2: Shape = New Shape(1,2,"Help");
        main(){
            print(flag2.flag.Despacito());
            flag2.flag.a = "s";
            doSomething = m1.a.b().c.d.e.f.g().c[5];
            a = 1.0;
        }
    }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect,310))
    # Test a program with literal declaration
    def test_311(self):
        input = """
        Class Shape: Rectangle {
            ##
            This part should be ignored, just to check, nothing to comment
            ##
            $getSomething(yes: Int){
                Var x : Float = 12.001;
                Var t : Int = 0;
                Var varvar: Int = 01_0;
                Var y : Float = 0.e1; 
                Var z : Float = 1.E23; 
                Return x;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,311))

    # Test a program with 3 classes and some invocation
    def test_312(self):
        input = """
        Class Shape{
            Var height, length: Float;
        }
        
        Class Rectangle: Shape {
            $getArea() {
                Return Self.height * Self.height;
            }
        }
        
        Class Program {
            main(){
                Out.printInt(Rectangle::$getArea());
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,312))
    # Test a program with only an unclosed string --> Raise error and print only the string content
    def test_313(self):
        input = """ 
            "Hello
        """
        expect = """Hello"""
        self.assertTrue(TestParser.test(input,expect,313))
    def test_314(self):
        input = """
    Class StringWorker{
        getString(someString, anotherString: String){
            Val someString: String = "hello PPL";
            Return someString;
        }
    }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,314))

    # Test from d96 spec pdf
    def test_315(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;

            $getNumOfShape() {
                Val temp: Int = 5;
                Return $numOfShape;
            }
        }

        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }

        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,315))
    
    # Test case for Foreach - In loop
    def test_316(self):
        input = """
        Class Program {
            main() {
                Foreach(x In 100 .. 300 By 5){
                    Out.printInt(x % 10);
                }
                Foreach(y In 300 .. -0 By -2){
                    Self::$doNothing = 1;
                    a::$doNothing();
                    Foreach(z In -1 .. 50000000){
                        print("Hello world");
                    }
                }
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 316))

    def test_317(self):
        input = """
        Class Program {
            main() {
                Val $invalid_value: Int = 100000000; ## Some error should occur here ##
                Return $invalid_value;
            }
        }
        """
        expect = """Error on line 4 col 20: $invalid_value"""
        self.assertTrue(TestParser.test(input,expect,317))

    def test_318(self):
        input = """
        Class Program {
            Var $sus_value: String = "This value is sus!"; ## Susssssss ##
            main() {
                Val valid_value: Int = 100000000;
                valid_value.b.c.d() = Program::$a.b.c().d.e.Self.x::$f()::g.h::$i().j + 1;
                Return (valid_value - Self::$sus_value + Self.what - Program::$a.b.c(Program::$a.b).d.e.Self.x::$f()::$g.h::$i().j);
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,318))

    def test_319(self):
        input = """
        Class Program {
            Var a: Int;
            main() {
                Val valid_value: Float = 0.5;
                Self::$a = Program::a::b.c();
                Return Program::a.b.c;
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,319))

    def test_320(self):
        input = """"""
        expect = """Error on line 1 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input,expect,320))

    def test_321(self):
        input = """
        Class Program {
            Var a: Array[Array[Int, 5], 5];
            main() {
                Val valid_value: Float = 0.5;
                Self::$a = Program::a::b.c();
                Return Program::a.b.c;
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect, 321))

    def test_322(self):
        input = """
        Class Rectangle: Shape{
            Val myArray: Array[Float, 3];
                getArray(){
                    a = a.1;
                    Return myArray;
            }
        }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 322))

    def test_323(self):
        """ Test unequal variable and value"""
        input = """
        Class Rectangle: Shape{
            Val length, width: Int = 1;
            }
        }
            """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 323))


    # def test_2(self):
    #     input = """ """
    #     expect = """ """
    #     self.assertTrue(TestParser.test(input,expect,2))

