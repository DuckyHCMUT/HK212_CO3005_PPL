import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_bkel_1(self):
        input = """Class main{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,201))

    def test_no_class_program(self):
        input = """abc = 1"""
        expect = "Error on line 1 col 0: abc"
        self.assertTrue(TestParser.test(input, expect,205))

    def test_bkel_2(self):
        input = """
    Class Rectangle: Shape {
        getArea() {
            Return length * (width + 5);
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,202))

    def test_bkel_3(self):
        input = """
    Class Shape {
        $getNumOfShape( {
            Return Self.length * Self.width;
        }
    }
        """
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input, expect,203))
    
    def test_with_comment(self):
        input = """
    Class Shape: Rectangle {
        ##
        This part should be ignored, just to check, nothing to comment
        ##
        $getSomething(yes: Int){
            Var x : Int=0;
            Return x;
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,204))
    
    def test_Thinh_case(self):
        input = """
    Class Trt{
        Var a: String;
        Constructor(x, y: String; z: Int){
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
    }
        """
        expect = """ """
        self.assertTrue(TestParser.test(input, expect,206))

    def test_207(self):
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
        self.assertTrue(TestParser.test(input,expect,207))
