import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input,expect,203))

    def test_bkel(self):
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e ;
   e = expr ;
   c = expr ;
   foo(expr);
   return expr;
}
float goo (float a, b) {
   return expr;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_bkel_2(self):
        input = """float goo (float a, b) {
    foo(expr, expr, expr);
    return expr;
}

c = expr;"""
        expect = "Error on line 6 col 0: c"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_bkel(self):
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e ;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1
}
float goo (float a, b) {
   return foo(1, a, b);
}"""
        expect = "Error on line 7 col 0: }"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_bkel_3(self):
        input = """float goo (float a, b) {
   return foo(1, a, b);
}

c = 5;"""
        expect = "Error on line 5 col 0: c"
        self.assertTrue(TestParser.test(input,expect,207))
