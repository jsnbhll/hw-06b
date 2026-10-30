# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')

    def testEquilateralUpperLimit(self):
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral','200,200,200 should be equilateral')

    def testIsocelesAB(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be isoceles')

    def testIsocelesAC(self):
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 should be isoceles')

    def testIsocelesBC(self):
        self.assertEqual(classifyTriangle(3,2,2),'Isoceles','3,2,2 should be isoceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','3,4,6 should be scalene')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(3,1,2),'NotATriangle','3,1,2 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1,3,2),'NotATriangle','1,3,2 is not a triangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is not a triangle')

    def testNotATriangleTooLong(self):
        self.assertEqual(classifyTriangle(1,2,4),'NotATriangle','1,2,4 is not a triangle')

    def testZeroA(self):
        self.assertEqual(classifyTriangle(0,2,2),'InvalidInput','0,2,2 is invalid input')

    def testZeroB(self):
        self.assertEqual(classifyTriangle(2,0,2),'InvalidInput','2,0,2 is invalid input')

    def testZeroC(self):
        self.assertEqual(classifyTriangle(2,2,0),'InvalidInput','2,2,0 is invalid input')

    def testNegativeSide(self):
        self.assertEqual(classifyTriangle(2,-1,2),'InvalidInput','2,-1,2 is invalid input')

    def testOverLimitA(self):
        self.assertEqual(classifyTriangle(201,2,2),'InvalidInput','201,2,2 is invalid input')

    def testOverLimitB(self):
        self.assertEqual(classifyTriangle(2,201,2),'InvalidInput','2,201,2 is invalid input')

    def testOverLimitC(self):
        self.assertEqual(classifyTriangle(2,2,201),'InvalidInput','2,2,201 is invalid input')

    def testFloatSide(self):
        self.assertEqual(classifyTriangle(3.0,4,5),'InvalidInput','3.0,4,5 is invalid input')

    def testStringSide(self):
        self.assertEqual(classifyTriangle(3,4,'5'),'InvalidInput','3,4,5 as a string is invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

