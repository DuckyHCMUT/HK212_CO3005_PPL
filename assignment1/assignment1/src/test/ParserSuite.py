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
        self.assertTrue(TestParser.test(input, expect, 302))

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
        """ Erroneous program with no Class"""
        input = """abc = 1;"""
        expect = "Error on line 1 col 0: abc"
        self.assertTrue(TestParser.test(input, expect, 304))

    def test_305(self):
        """Simple program: 1 Class and 1 Method"""
        input = """Class Program {
            main() {Return;}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 305))

    def test_306(self):
        input = """
    Class Shape: Rectangle {
        ##
        This part should be ignored, just to check, nothing to comment
        ##
        $getSomething(yes: Int){
            Var x : Int = 0;
            Self.x = 1;
            Return x;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 306))

    def test_307(self):
        """A little bit more complex program"""
        input = """Class Program {
            main() {
                Output.putStrLn(1);
                Output.putStrLn(10);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 307))

    def test_308(self):
        """Miss ) after the main"""
        input = """Class Program {
            main( {}
        }"""
        expect = "Error on line 2 col 18: {"
        self.assertTrue(TestParser.test(input, expect, 308))

    def test_309(self):
        """ More complex program with If statement"""
        input = """Class Program {
            main() {
                If (a <= 1) {
                    Out.putStrLn(5);
                }
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 309))

    def test_310(self):
        """Test nested if program"""
        input = """Class Program {
            main() {
                If (a == 3) {
                    Out.putIntLn(4);
                    If (b == 4) {
                        Out.putStrLn(4);
                        Out.putStrLn(5);
                    }
                    If ((a == 3) && (b == 4)) {
                        Out.putIntLn(4);
                    }
                    If ((a == 3) || (b == 4)) {
                        Out.putIntLn(5);
                    }
                    If (!(a == 3) && (b != 4)) {
                        Out.putIntLn(4);
                        If ((a > 3) || (b <= 4)) {
                            Out.putIntLn(5);
                        }
                    }
                }
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 310))

    def test_311(self):
        """ Test 1 empty and 1 ok program"""
        input = """Class Rectangle {} Class Program{main(){Return;}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 311))

    def test_312(self):
        """ Test empty classes """
        input = """Class Shape{} Class Circle{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 312))

    def test_313(self):
        """ Longer program"""
        input = """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;

            main() {
                Out.println(4);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 313))

    def test_314(self):
        """ Wrong attribute decleration position"""
        input = """Class Program {
            Val a : Int, b : String;

            main() {
                Out.println(4);
                Return;
            }
        }"""
        expect = "Error on line 2 col 23: ,"
        self.assertTrue(TestParser.test(input, expect, 314))

    def test_315(self):
        """ Test with equal number of variable and value """
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
        self.assertTrue(TestParser.test(input, expect, 315))

    def test_316(self):
        """ Test with unequal number of variable and value """
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
        self.assertTrue(TestParser.test(input, expect, 316))

    def test_317(self):
        """ Test case with 1 class, comment and array declaration """
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
        self.assertTrue(TestParser.test(input, expect, 317))

    def test_318(self):
        """ More complex program """
        input = """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d, floatNum_1 : Float = 1.0, 2e10;
            Var $a : Float;

            main() {
                Out.println(Self.floatNum_1);
                Return;
            }
        }
        """
        expect = "Error on line 4 col 53: ;"
        self.assertTrue(TestParser.test(input, expect, 318))

    def test_319(self):
        """ Test very complex program """
        input = """Class TestNameNodeMetrics {
  Val CONF : Int = New HdfsConfiguration();
  Var $DFS_REDUNDANCY_INTERVAL : Int = 1;
  Val $TEST_ROOT_DIR_PATH : String = New Path("/testNameNodeMetrics");
  Val NN_METRICS : String = "NameNodeActivity";
  Var BLOCK_SIZE : Float = 1024e10 * 2048.1;

  Var $DATANODE_COUNT : Int = EC_POLICY.getNumDataUnits() + EC_POLICY.getNumParityUnits() + 1;

  Val cluster : Int;
  Val fs : String;

   getTestPath(fileName : String) {
    Return New Path(TEST_ROOT_DIR_PATH, fileName);
  }

  setUp(a : Int; b : Float; c : String) {
    cluster.waitActive();
    STH.someFunc();
    fs.enableErasureCodingPolicy(EC_POLICY.getName());
    ecDir = Self::$getTestPath("/ec");
    fs.setErasureCodingPolicy(ecDir, EC_POLICY.getName());
  }

  tearDown() {
    Val source : Float = DefaultMetricsSystem.instance();
    If (source != Null) {
      ##
      Run only once since the UGI metrics is cleaned up during teardown
      ##
      SOMETHING.assertQuantileGauges("GetGroups1s", rb);
    }
    If (hostsFileWriter != Null) {
        Self.something = 5;
      hostsFileWriter.cleanup();
      hostsFileWriter = Null;
    }
    If (myCluster != Null) {
      myCluster.shutdown();
      myCluster = Null;
    }

    Val includeHosts : Array[Int, 100] = New StringBuilder(dnAddresses.length - 1);
    Foreach (i In 1 .. 100 By 1) {
      includeHosts[i] = dnAddresses[(i + 1)];
    }
  }
}

Class Program {
  main() {
    Out.println("Hello World");
    Return;
  }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 319))

    def test_320(self):
        """ Test longer longer program """
        input = """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;
            Val a, b : Int;
            Var $a : Float;

            getArea(w : Int; h : Float; a : String) {
                Out.println(a);
                Out.something(w);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var c, d : Float = 1.0, 2e10;
            }

            $something(w : Int) {
                Out.println(40);
                Out.something(50);
                Var a : Int = 4 + 2;
                Val b : String = "Hello World";
                Var c, d : Float = 1.0, 2e10 - 10;
            }

            Something() {
                Out.println(4000);
                Out.something(5000);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var c, d : Float = 1.0, 2e10;
            }

            main() {
                Out.println(nothing);
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 320))

    def test_321(self):
        """ Test longer longerrrrrrrrrrrrrrrrrrr program """
        input = """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var c, $d : Float = 1.0, 2e10;

            Something() {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var c, d : Float = 1.0, 2e10;
            }

            main() {
                Out.println(4);
                Return;
            }
        }
        Class Shape {
            Val a, b : Int;
            Var $a : Float;

            getArea(w : Int; h : Float; a : String) {
                Out.println(400);
                Out.something(500);
                Var a : Int = 4;
                Val b : String = "Hello Worldddddddddddd";
                Var c, d : Float = 1.0, 2.5e03;
            }

            $something(w : Int) {
                Out.println(4000);
                Out.something(5000);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var c, d : Float = 1.0, 2e10;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 321))

    def test_322(self):
        """ Test with Array this time """
        input = """Class Program {
            Val a, b: Array[Int, 3];
            Var c: Array[String, 10_0001];
            Var d: Array[Float, 1];
            Var $c, $d, $e: Array[Boolean, 10];
            main() {
               Out.println("Xo hang kiem 30 nghin");
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 322))

    def test_323(self):
        """ Testcase from Justince """
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
                a.print(no);
            }
        }
        Class Program {
            ## Muda
            Muda ##
            Var hello: Array[Int, 5];
            Var length, width: Int;
            Var flag2: Shape = New Shape(1,2,"Help");
            main(){
                Self.print(flag2.flag.Despacito());
                flag2.flag.a = "s";
                a = 1.0;
            }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 323))

        
    def test_324(self):
        """ Testcase from Justince, complicated with declaration """
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
            Self.print("No service");
        }
    }
    Class Program {
        ## Muda
        Muda ##
        Var hello, hello2: Array[Float, 2];
        Var length, width: Int;
        Var flag2: Shape = New Shape(1,2,"Help");
        main(){
            Self.print(flag2.flag.Despacito());
            flag2.flag.a = "s";
            doSomething = m1.a.b().c.d.e.f.g().c[5];
            a = 1.0;
        }
    }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 324))

    def test_325(self):
        """ Test a program with 3 classes and some invocation """
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
        self.assertTrue(TestParser.test(input, expect, 325))

    def test_326(self):
        """ Test statements inside function, assignments only"""
        input = """Class Program {
            Val a, b: Array[Int, 0x1234];
            Var c: Array[String, 1_2];
            main() {
               a = 1;
               d = "Nothing";
               c = 1e15;
               d = 0x1637_ABCB;
               e = True;
               Return (c + d);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 326))

    def test_327(self):
        """ Test a program with literal declaration """
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
        self.assertTrue(TestParser.test(input, expect, 327))

    def test_328(self):
        """ Test statements inside function, assign Array"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            Var c: Array[Int, 10] = Array(1, 2, 3, 4, 5);
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));
               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 328))

    def test_329(self):
        """ Test a program with only an unclosed string --> Raise error and print only the string content """
        input = """ 
            "Hello
        """
        expect = """Hello
"""
        self.assertTrue(TestParser.test(input, expect, 329))

    def test_330(self):
        """ Test statements inside function, assign identifiers to identifiers"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 1_023];
            main() {
               a = 111;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(9, 8, 7));
               f = e;
               d = "Weirdo things and stuff";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 330))

    def test_331(self):
        input = """
    Class StringWorker{
        getString(someString, anotherString: String){
            Val someString: String = "hello PPL";
            Return someString;
        }
    }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 331))


    def test_332(self):
        """ Test statements inside function """
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6)) + Array(1, 2, 3);

               c = a + b;
               c = (a +. b) ==. c;
               d = f.callFunc() - g::$something(a, b);
               e = g::$somethingElse;
               f = g.someValue();

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 332))

    def test_333(self):
        """ Test statements inside function """
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1.234;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array("4", "5", 6));
               f.callFunc();
               Sth.callSomething();

               c = a + b;
               c = a +. (b ==. c);
               d = f.callFunc() - g::$something(a, b);
               e = g::$somethingElse;
               f = g.someValue().evenMore();

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 333))

    def test_334(self):
        """ Test from d96 spec pdf """
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
        expect = """Error on line 9 col 23: $numOfShape"""
        self.assertTrue(TestParser.test(input, expect, 334))

    def test_335(self):
        """ Test statements inside function """
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            not_a_main_program() {
               a = 1000000000;
               c = Array();
               e = Array(Array(1 + 2, 2 * 5, 3), Array(4, 5, 6));
               f.callFunc();
               Sth::$callSomething();

               c = a - -b;
               c = (a < b) > c;
               Val d: Int = f.callFunc() - g::$something(a, b);
               e = g::$somethingElse;
               f = g.someValue();
               Val abc: String = f.something();
               Var c: Float = ((a - b) * (c / d)) + (e + f) % 7;

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 335))

    def test_336(self):
        """ Test block statement"""
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class Shape {
            
        }
        Class Rectangle : Shape {
            something() {
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 336))

    def test_337(self):
        """ Test Constructor and Destructor"""
        input = """
            Class TestMammal {
                Constructor(w: Int; s: Float; a: String; b: Array[Int, 5]; c: Boolean) {
                    Var a : Int = 15;
                    Var a, c : Boolean = False, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                    Return;
                }

                Destructor() {
                    Var a : Int = 16;
                    Var a, c : Boolean = True, False;
                    c = (a + b) * (c + d) - (y - z) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                }

                Yell(w: Int; h: Float) {
                    Var myBird : Bird = New Bird();

                    myFish.label();
                    myFish.move();
                    myFish.die();
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish(1, 3, 2);

                    myFish.label();
                    myFish.move();
                    myFish.die();
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 337))

    def test_338(self):
        """ Test list of expression in params of function calling and Self keyword"""
        input = """
            Class TestBird {
                Constructor(w: Int; s: Float; a: String; b: Array[Int, 5]; c: Boolean) {
                    Var a : Int = 1;
                    Var a, c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                    Return;
                }

                Destructor() {
                    Var a : Int = 1;
                    Var a, c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function((a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1)) * f.a - f::$b;
                }

                Yell(w: Int; h: Float) {
                    Var myBird : Bird = New Bird();
                    Self.calling();

                    myBird.label();
                    myBird.move();
                    myBird.eat();
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish(1, 2, (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1));

                    myFish.label();
                    myFish.move();
                    myFish.eat();
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 338))


    def test_339(self):
        """ Test constructor without params and destructor"""
        input = """
            Class TestBird {
                Constructor() {
                    Var a : Int = 15;
                    Var a, c : Boolean = False, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                    Return;
                }

                Destructor() {
                    Var a : Int = 16;
                    Var a, c : Boolean = True, False;
                    c = (a + b) * (c + d) - (y - z) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                }

                Yell(w: Int; h: Float) {
                    Var myBird : Bird = New Bird();

                    myBird.label();
                    myBird.move();
                    myBird.eat();
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish();

                    myFish.label();
                    myFish.move();
                    myFish.eat();
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 339))

    def test_340(self):
        """ Invalid static variable declaration """
        input = """
        Class Program {
            main() {
                Val $invalid_value: Int = 100000000; ## Some error should occur here ##
                Return $invalid_value;
            }
        }
        """
        expect = """Error on line 4 col 20: $invalid_value"""
        self.assertTrue(TestParser.test(input, expect, 340))

    def test_341(self):
        """ Suspicious but valid static variable declaration """
        input = """
        Class Program {
            Var $sus_value: String = "This value is sus!"; ## Susssssss ##
            main() {
                Val valid_value: Int = 100000000;
                valid_value.b.c.d() = Program::$a.b.c().d.e.x::$f()::g.h::$i().j + 1;
                Return (valid_value - Self::$sus_value + Self.what - Program::$a.b.c(Program::$a.b).d.e.x::$f()::$g.h::$i().j);
            }
        }
        """
        expect = """Error on line 6 col 61: ::"""
        self.assertTrue(TestParser.test(input, expect, 341))

    def test_342(self):
        """ Test chaining rule of instance method invocation: a.b().c() """
        input = """
    Class TestNameNodeMetrics {
        Val CONF : Int = New HdfsConfiguration();
        Var $DFS_REDUNDANCY_INTERVAL : Int = 100;
        Val $TEST_ROOT_DIR_PATH : String = New Path("/testNameNodeMetrics");
        Val NN_METRICS : String = "NameNodeActivity";

        ## Number of dnodes in the cluster ##
        Var $DATANODE_COUNT : Int = EC_POLICY.getNumDataUnits() - 1;

        Val cluster : Int;
        Val fs : String;

        getTestPath(fileName : String) {
            Return New Path(TEST_ROOT_DIR_PATH, fileName);
        }

        setUp(a : Int; b : Float) {
            cluster.waitActive();
            Self::$someFunc();
            fs.enableErasureCodingPolicy(EC_POLICY.getName());
            ecDir = Self.getTestPath("/ec");
            fs.setErasureCodingPolicy(ecDir, EC_POLICY.getName());
        }

        tearDown() {
            Val source : Float = DefaultMetricsSystem.instance().getSource("UgiMetrics");
            If (source != Null) {
                Self::$assertQuantileGauges("GetGroups1s", rb);
            }

            Val includeHosts : Array[Int, 100] = New StringBuilder(dnAddresses.length - 1);
            Foreach (i In 1 .. 1000 By 2) {
            includeHosts[i] = dnAddresses[(i + 1)];
            }
        }
    }

    Class Program {
        main() {
            Output.println("Hello World");
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 342))

    def test_343(self):
        """ Test function with return statement """
        input = """
            Class Shape {
                $getNumOfShape( {
                    Return Self.length * Self.width;
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish();

                    myFish.label();
                    myFish.move();
                    myFish.die();
                    {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                    }
                    Return;
                }
            }
        """
        expect = "Error on line 3 col 32: {"
        self.assertTrue(TestParser.test(input, expect, 343))

    def test_344(self):
        """ Test matrix multiplications"""
        input = """
    Class Program {
        main() {
            If (col1 != row2) {
                Out.println("Matrix multiplication is not possible");
            }

            Else {
                Var a : Array[Array[Int, 100], 100];
                Var b : Array[Array[Int, 100], 100];
                Var c : Array[Array[Int, 100], 100];

                Out.println("Enter values for matrix A : \\n");
                Foreach (i In 0 .. row1 By 1) {
                    Foreach (j In 0 .. col1) {
                        a[i][j] = s.nextInt();
                    }
                }

                Out.println("Enter values for matrix B : \\n");
                Foreach (i In 0 .. row2 By 1) {
                    Foreach (j In 0 .. col2) {
                        b[i][j] = s.nextInt();
                    }
                }

                Out.println("Matrix multiplication is : \\n");
                Foreach (i In 0 .. rows1 By 1) {
                    Foreach (j In 0 .. col2 By (0 + 1) * 2 - 1) {
                        c[i][j]=0;
                        Foreach (k In 0 .. col1 By 1) {
                            c[i][j] = c[i][j] + a[i][k] * b[k][j];
                        }
                        c = a + b > c + d;
                        Out.print(c[i][j] +. " ");
                    }
                    Out.println();
                }
            }
            Return;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 344))

    def test_345(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + a.foo();
                a.foo2(param1, param2);
                a1 = a.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehiclee{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){

            }
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    a.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    a.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 345))

    def test_346(self):
        input = """Class Program {
            getName() {
                Var b: Float = 0.3;
            }
            main() {
                If (a >= b) {
                    Var a: Int = 0;
                    a = a + 3;
                }
                Elseif (b >= c) {
                    getName(a >= b);
                }
                Elseif (12 >= g) {
                    insert("String");
                }
                Else {
                    Tam = Self.Tam;
                }
            }
        }"""
        expect = "Error on line 11 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 346))    

    def test_347(self):
        """constructor must have a return statement"""
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
                Return;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
            }
            mapWorker() {
                Out.println("Cleaning");
                Foreach (k In 0 .. Self.key.length() By 2)
                {
                    myK = Self.key[k];

                    Cleaner.free(myK);
                    Self.key = Null;
                }
                Cleaner.free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];

                    Cleaner.free(el);
                    Self.value = Null;
                }
                Cleaner.free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = 1;
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 100, 321;
                Var x, y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 347))

    def test_348(self):
        """ Test incorrect chaining"""
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
        expect = """Error on line 6 col 36: a"""
        self.assertTrue(TestParser.test(input, expect, 348))

    def test_349(self):
        """ Test simple program (But wrong!)"""
        input = """Class Program {
            main() {
                Val b : Int = a[5].func()[6];
                Return;
            }
        }"""
        expect = "Error on line 3 col 34: ."
        self.assertTrue(TestParser.test(input, expect, 349))

    def test_350(self):
        """ Test program with indexing-function call"""
        input = """Class Program {
            main() {
                a[1].func();
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 350))

    def test_351(self):
        """ Null program"""
        input = """"""
        expect = """Error on line 1 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 351))

    def test_352(self):
        """ Test Foreach loop """
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
                        Out.print("Hello world");
                    }
                }
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 352))

    def test_353(self):
        input = """
        Class Rectangle: Shape{
            Val myArray: Array[Float, 3];
                getArray(){
                    a = a.1;
                    Return myArray;
            }
        }
            """
        expect = "Error on line 5 col 26: 1"
        self.assertTrue(TestParser.test(input, expect, 353))

    def test_354(self):
        input = """
        Class Program {
            main() {
                Val a : Array[Array[Int, 10], 0x15];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 354))

    def test_355(self):
        input = """Class Program {
            main() {
                a[5] = 1;
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 355))

    def test_356(self):
        input = """
        Class Program {
            main() {
                a.func()[5].fun();
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 356))

    def test_357(self):
        """ Test static parameter are not allowed"""
        input = """
        Class Program {
            main($a : Int) {
                
            }
        }
        """
        expect = "Error on line 3 col 17: $a"
        self.assertTrue(TestParser.test(input, expect, 357))

    def test_358(self):
        input = """Class Program {
            main() {
                Out.println(a.a[5]);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 358))

    def test_359(self):
        """ Test unequal variable and value"""
        input = """
        Class Rectangle: Shape{
            Val length, width: Int = 1, 2;
            doSomething(){
                Val a, b, c: Int = 1; ##Error goes here##
            }
        }
            """
        expect = "Error on line 5 col 36: ;"
        self.assertTrue(TestParser.test(input, expect, 359))

    def test_360(self):
        """ Test Array min size must be > 0"""
        input = """
        Class Program {
            Val $hehehehe : Array[Int, 0];
            main() {
                Val a : Array[Int, 0b0];
                Var b : Array[Int, 0x0];
                Val c : Array[Int, 0B0];
                Val d : Array[Int, 00];
                Var e : Array[Int, 0X0];
            }
        }"""
        expect = "Error on line 3 col 39: 0"
        self.assertTrue(TestParser.test(input, expect, 360))

    def test_361(self):
        """ Test Array min size must be > 0"""
        input = """
        Class Program {
            Val c : Array[Int, 0b1101];
            main() {
                Val a : Array[Int, 0x1234ABCD];
                Var b : Array[Array[Int, 0x1234ABCD], 0x1234ABCD];
                Val c : Array[Int, 500000];
                Val c : Array[Int, 0312123];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 361))

    def test_362(self):
        """ Test failed Foreach program """
        input = """
        Class Program {
            main() {
                Foreach (i In 1..100 By 2) {
                        Out.printInt(i);
                    }
                }
            }
        """
        expect = "Error on line 4 col 33: 100"
        self.assertTrue(TestParser.test(input, expect, 362))

    def test_363(self):
        """ Test simple program with weird stuff """
        input = """Class Program {
            main() {
                a[1].func()[0].bar();
                a[1].func();
                a[1] = 1;
                Val b : String = a.func()[1];
                Out.println(a.a[1]);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 363))

    def test_364(self):
        """ Test index operator is not allowed in foreach"""
        input = """
        Class Program {
            main() {
                Foreach (Program::$a[1].b In 1 .. 100) {
                    Out.println(4);
                }
            }
        }"""
        expect = "Error on line 4 col 36: ["
        self.assertTrue(TestParser.test(input, expect, 364))

    def test_365(self):
        """ Test ionstance and static access function"""
        input = """
        Class Program {
            main() {
                Foreach (Self::$func().b.c In 1 .. 100) {
                    Out.println(4);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 365))

    def test_366(self):
        """constructor that has no return statement"""
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
            }
            clean() {
                Out.println("Cleaning");
                Foreach (k In 0 .. Self.key.length() By 1)
                {
                    el = Self.key[k];

                    a.free(el);
                    Self.key = Null;
                }
                a.free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];

                    a.free(el);
                    Self.value = Null;
                }
                a.free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = 1;
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var x, y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 366))

    def test_367(self):
        """ Assign more expression than the var declaration"""
        input = """
        Class Program {
            main() {
                Val a : Int = 1, 2;
                Return;
            }
        }"""
        expect = "Error on line 4 col 31: ,"
        self.assertTrue(TestParser.test(input, expect, 367))

    def test_368(self):
        """ Test continue statement"""
        input = """
        Class Simple {

   main() {
      Val numbers : Array[Int, 5] = Array(10, 20, 30, 40, 50);

      Foreach (i In 0 .. 4 By 1) {
         If ( x == 30 ) {
            Continue;
         }
         System.out.print( x );
         System.out.print("\\n");
      }
   }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 368))

    def test_369(self):
        """testing func params declare"""
        input = """
        Class Program {
            Val a: Int = 1;
            fooBar(a, b : Int; c : Float) {
                Program.fooBar1();
            }
            main() {
                Program.fooBar(a, b, c);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 369))

    def test_370(self):
        """ Test array literal syntax"""
        input = """
        Class Program {
            main() {
                Val a : Array[Int, 1] = Array(1, );
            }
        }"""
        expect = "Error on line 4 col 49: )"
        self.assertTrue(TestParser.test(input, expect, 370))

    def test_371(self):
        """ Test (1 + 1).x is valid"""
        input = """
        Class Program {
            main() {
                a = (1 + 1).x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 371))

    def test_372(self):
        """ Test New X()::$a is illegal"""
        input = """
        Class Program {
            main() {
                Val a : Int = a[1] + b[2]; 
                a = New X()::$a();
            }
        }"""
        expect = "Error on line 5 col 27: ::"
        self.assertTrue(TestParser.test(input, expect, 372))

    def test_373(self):
        """ Test New X()::$a is illegal"""
        input = """
        Class Program {
            main() {
                New X()::$a();
            }
        }"""
        expect = "Error on line 4 col 23: ::"
        self.assertTrue(TestParser.test(input, expect, 373))

    def test_374(self):
        """Test scalar variables"""
        input = """
        Class Program {
            main() {
                Foreach (a::$b In 1 .. 1006) {
                    Out.println(12);
                }
                Foreach (a.a In 1 .. 1007) {
                    Out.println(13);
                }
                Foreach (Self.func In 1 .. 1008) {
                    Out.println(14);
                }
                Foreach (Self::$func().b.c In 1 .. 1009) {
                    Out.println(15);
                }
                Foreach (Self::$a.b.c In 1 .. 1010) {
                    Out.println(16);
                }
                Foreach (Self.a.b.c In 1 .. 1011) {
                    Out.println(17);
                }
                Foreach (Self::$a In 1 .. 1012) {
                    Out.println(18);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 374))

    def test_375(self):
        """ Test failed scalar variables"""
        input = """
        Class Program {
            main() {
                Foreach (Program.a::$b In 1 .. 100) {
                    Out.println(400);
                }
            }
        }"""
        expect = "Error on line 4 col 34: ::"
        self.assertTrue(TestParser.test(input, expect, 375))

    def test_376(self):
        """ Test scalar variables"""
        input = """Class Program {
            main() {
                a[1].func();
                a[1] = 2.5;
                Out.println(a.a[2]);
                a[1][2].a[3].func()[4].a[5].func();
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 376))

    def test_377(self):
        """ Test scalar variables"""
        input = """Class Program {
            main() {
                a::$a[5].func()[0];
                a::$a;
                a[4]::$func();
                Return;
            }
        }"""
        expect = "Error on line 3 col 34: ;"
        self.assertTrue(TestParser.test(input, expect, 377))

    def test_378(self):
        """ Test statements inside function, operator in action, non associative operator
        and wrong assignment operators (nested equal signs)"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 100;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));

               ## c = a + b; ##
               c = (a +. b) ==. c;
               c = ((a - b) * (c / d)) + (e + f) % 5;
               f[3] = d = e = c[1];

               Return f[3];
            }
        }
        """
        expect = "Error on line 13 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 378))

    def test_379(self):
        """ Test index operator and member access"""
        input = """Class Program {
            main() {
                Var a : Int = (a::$a[1]).func()[0];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 379))

    def test_380(self):
        """ Test index operator and member access"""
        input = """Class Program {
            main() {
                Val a : Int;
                Foreach (i In 1 .. 1000 By 5)
                {
                    Clip.printf("enter the number:");
                    Clip.scanf("%d", a);
                    If ( a == 0 ) {
                        Break;
                        Return 100;
                    }
                    Else {
                        Continue;
                    }
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 380))

    def test_381(self):
        """ Test scalar variables"""
        input = """
        Class Program {
            main() {
                Val b : Int = a::$a;
                a::$func();
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 381))

    def test_382(self):
        """ Test for a statement cannot be a index access"""
        input = """
        Class Program {
            main() {
                a[5].func()[0];
                b[6].func();
                c[7] = 1;
                Out.println(a.a[10]);
                Return a[10];
            }
        }"""
        expect = "Error on line 4 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 382))

    def test_383(self):
        """ Test as index has lower priority than  member access -> cover by ()"""
        input = """
        Class Program {
            main() {
                Val myVarB : Int = (a[5]).func()[10];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 383))

    def test_384(self):
        """ Constructor and Destructor with return statements (Only available for assignment 1)"""
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Var $myMap: Map = New Map(Self.key, Self.value);
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
                Return;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
                Return;
            }
        }

        Class Program {
            main() {
                Val sth : Map = New Map(arr1, arr2);
                Return Null;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 384))


    def test_385(self):
        """ Test element operator as operands"""
        input = """
        Class Program {
            main() {
                a[1][2] = b[1][2][3] - c[1][2][3];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 385))

    def test_386(self):
        """ Test nested If-Elseif-Else"""
        input = """
        Class Program {
            Val a: Int = 1;
            fooBar() {
                Self::$fooBar();
            }
            main() {
                If (1 >= 2) {
                    Out.fooBar(True);
                } 
                Elseif (a <= 2) {
                    Self::$fooBar();
                } 
                Elseif (a[1][2] <= a[1] * a.a + Some::$a()) {
                    Out.println(400);
                } 
                Else {
                    Out.println("What are you looking for?");
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 386))

    def test_387(self):
        """ Test function params declare"""
        input = """
        Class Program {
            Val a: Int = 1;
            fooBar(a, b : Int; c : Float) {
                Self.fooBar1(True, False, Null);
            }
            main() {
                Self.fooBar(x, y, "ZhongGuo ren");
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 387))

    def test_388(self):
        """ Test return statement in main"""
        input = """
        Class D {
            Constructor() {
                a = True;
                b = False;
                Return;
            }
        }
        Class Program {
            main() {
                Return "Zhege ke bu ke ma?";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 388))

    def test_389(self):
        """ Test static and instance"""
        input = """
        Class C {
            foo() {
                Return nothingToReturnHehehehe;
            }
        }
        Class B : C{
            Val a : C;
            Val $b : B;
            Constructor() {
                a = New C();
                Self::$b = New B();
                Return;
            }
        }

        Class Program {
            main() {
                Val a : A = New A();
                a::$b.a.foo();
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 389))

    def test_390(self):
        """ Test multiple nested double colon """
        input = """
        Class C {
            foo() {
                Return nothingToReturnHehehehe;
            }
        }
        Class B : C{
            Val a : C;
            Val $b : B;
            Constructor() {
                a = New C();
                Self::$b = New B();
                Return;
            }
        }

        Class Program {
            main() {
                Val a : A = New A();
                a::$b::$c();
                Return;
            }
        }"""
        expect = "Error on line 20 col 21: ::"
        self.assertTrue(TestParser.test(input, expect, 390))

    def test_391(self):
        """ Test actual program to work on linked list"""
        input = """
        Class Node {
            Var data : Int;
            Val next : Node;

            Constructor(d : Int)
            {
                data = d;
                next = Null;
            }

            reverse(node : Node)
            {
                Var prev : Node = Null;
                Val current : Node = node;
                Val next : Node = Null;
                Foreach (i In 1 .. forever By 1) {
                    If (current == Null) {
                        Break;
                    } 
                    Else {
                        next = current.next;
                        current.next = prev;
                        prev = current;
                        current = next;
                    }
                }
                node = prev;
                Return node;
            }

            printList(node : Node)
            {
                Foreach (a In 1 .. n By 1) {
                    If (node != Null) {
                        System.out.print(node.data +. " ");
                        node = node.next;
                    } 
                    Else {
                        Break;
                    }
                }
            }
        }

        Class Program {
            main()
            {
                Val num1, num2: Int = 100, 200;
                Val list : LinkedList = New LinkedList();
                list.head = New Node(num1);
                list.head.next = New Node(num2);
                list.head.next.next = New Node(-516e21);
                list.head.next.next.next = New Node(985.414400e2);

                System.out.println("Given Linked list: \\n");
                list.printList(head);
                head = list.reverse(head);
                System.out.println("");
                System.out.println("Reversed linked list: ");
                list.printList(head);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 391))

    def test_392(self):
        """ Test continue statement """
        input = """
        Class Program {
            main() {
                Val numbers : Array[Int, 5] = Array(9, 8, 7.5, 6.9, 3);

                Foreach (i In 0 .. 10 By 1) {
                    If ( x > 6 ) {
                        Continue;
                    }
                    Else{
                        System.out.print("Passed\\n");
                    }
                    System.out.print(x);
                    System.out.print("\\n");
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 392))

    def test_393(self):
        """ Test on invalid member access (incorrect usage of double colon and dot)"""
        input = """
        Class Program {
            main() {
                b = a::c;
                Return;
            }
        }"""
        expect = "Error on line 4 col 23: c"
        self.assertTrue(TestParser.test(input, expect, 393))

    def test_394(self):
        """Test chaining function"""
        input = """
        Class Program {
            main() {
                a = a.b.c.d().e().f() + Self::$a();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 394))

    def test_395(self):
        """ Test wrong static access"""
        input = """
        Class Program {
            main() {
                Bike::$abc = 100;
                f = Sth::sthWeird;
            }
        }
        """
        expect = "Error on line 5 col 25: sthWeird"
        self.assertTrue(TestParser.test(input, expect, 395))

    def test_396(self):
        """Test static chaining """
        input = """
        Class Program {
            main() {
                Car::$abc = 100;
                a = a::$b::$c;
                a = (a::$b)::$c;
            }
        }"""
        expect = "Error on line 5 col 25: ::"
        self.assertTrue(TestParser.test(input, expect, 396))

    def test_397(self):
        """ Test wrongly access the New keyword"""
        input = """
        Class Program {
            main() {
                a = a.New A();
            }
        }"""
        expect = "Error on line 4 col 22: New"
        self.assertTrue(TestParser.test(input, expect, 397))

    def test_398(self):
        """ Test Keyword used as identifier"""
        input = """
        Class Continue {
            main() {
            }
        }"""
        expect = "Error on line 2 col 14: Continue"
        self.assertTrue(TestParser.test(input, expect, 398))

    def test_399(self):
        """ Test abnormal chaining of string literal """
        input = """
        Class Program {
            main() {
                a = "123"::$getValue();
            }
        }"""
        expect = "Error on line 4 col 25: ::"
        self.assertTrue(TestParser.test(input, expect, 399))

    def test_400(self):
        """ Test static attribute is not allowed in method"""
        input = """
        Class Program {
            Var $b : Int; ## Valid ##
            main() {
                Var $a : Int; ## Invalid ##
            }
        }"""
        expect = "Error on line 5 col 20: $a"
        self.assertTrue(TestParser.test(input, expect, 400))

    def test_401(self):
        """ Test no keyword Then in if statement (voided in later assignment spec)"""
        input = """
        Class Program {
            main() {
                If (a == 1) 
                Then {
                    self.Out.print(HelloWorld());
                }
                Return;
            }
        }
        """
        expect = "Error on line 5 col 16: Then"
        self.assertTrue(TestParser.test(input, expect, 401))

    def test_402(self):
        """ Test method call without access operator"""
        input = """Class Program {
            getName() {
                Var b: Float = 0.3;
            }
            main() {
                If (a >= b) {
                    Var a: Int = 0;
                    a = a + 45;
                }
                Elseif (b >= c) {
                    getName(a == b);
                }
                Elseif (12 >= g) {
                    insert("Please do not print this");
                }
            }
        }
        """
        expect = "Error on line 11 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 402))

    def test_403(self):
        """ Test destructor with passed parameter(s)"""
        input = """
        Class Program {
            Destructor(w: Float) {
                Self.call();
            }
            main() {
                Self.a();
                Return;
            }
        }
        """
        expect = "Error on line 3 col 23: w"
        self.assertTrue(TestParser.test(input, expect, 403))

    def test_404(self):
        """ Test New operator can not be followed by a static member access """
        input = """Class Program {
            main() {
                New X()::$abc();
            }
        }"""
        expect = "Error on line 3 col 23: ::"
        self.assertTrue(TestParser.test(input, expect, 404))
