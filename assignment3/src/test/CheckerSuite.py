import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """
        Class Program {
            Var $x: Int = 2.5

            foo(t: Int; y, z:Float){
                Var f: Int = 5.0;
            }
            main(){

            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 501))