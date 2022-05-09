import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_random_thing_19(self):
        input = """
        Class P {
            Destructor() {
                Return;
            }
        }
        Class Program {
            main() {
                Var p : P;
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Statement: MethodDecl(Id(Destructor),Instance,[],Block([Return()]))"
        self.assertTrue(TestChecker.test(input, expect, 829))
