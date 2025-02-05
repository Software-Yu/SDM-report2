#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        #同値分割法(有効同値、無効同値)
        def test_sample1 (self):     #有効同値（＜)   
                self.assertEqual (250500, calc(501,500))  
                
        def test_sample2 (self):     #有効同値(境界条件付近(上限下限)) 
                self.assertEqual (499500, calc(500,999))              
                self.assertEqual (500, calc(1,500))        
                
        def test_sample3 (self):     #無効同値(マイナス)
                self.assertEqual (-1, calc(-1,500))
                self.assertEqual (-1, calc(-1,-2)) 
                
        def test_sample4 (self):     #無効同値(少数)
                self.assertEqual (-1, calc(1.1,1.2)) 
                self.assertEqual (-1, calc(1.1,500))
                
        def test_sample5 (self):     #無効同値(境界条件付近(範囲外の小大))
                self.assertEqual (-1, calc(500,1000))     
                self.assertEqual (-1, calc(0,500))     
                 
        def test_sample6 (self):     #無効同値(数値以外)                
                self.assertEqual (-1, calc("a",500))  
                self.assertEqual (-1, calc("a","b"))  

         #境界値分析(1,999,0,1000を境界値とし、重点的に入力)
        def test_sample7 (self):     #両方上限、両方下限、下限と上限
                self.assertEqual (1, calc(1,1)) 
                self.assertEqual (998001, calc(999,999)) 
                self.assertEqual (999, calc(1,999)) 
        
        def test_sample8 (self):     #範囲外(小)と下限、上限と範囲外(大)
                self.assertEqual (-1, calc(0,1))
                self.assertEqual (-1, calc(999,1000)) 
                
        def test_sample9 (self):     #範囲外(小)と上限、下限と範囲外(大)
                self.assertEqual (-1, calc(0,999))
                self.assertEqual (-1, calc(1,1000)) 
                
        def test_sample99 (self):    #両方範囲外(小)、両方範囲外(大)、範囲外(小)と範囲外(大)
                self.assertEqual (-1, calc(-1,0))
                self.assertEqual (-1, calc(1000,1001)) 
                self.assertEqual (-1, calc(0,1000))
                    


        
