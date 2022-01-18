import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_class(self):
        input = """class main{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,204))

    def test_more_class(self):
        input = """ 
            class Rectangle: Shape {
                getArea() {
                    Return self.length * self.width;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,205))

    def test_more_more_class(self):
        input = """ 	
            class Shape {
                $getNumOfShape( {
                    Return self.length * self.width;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,206))