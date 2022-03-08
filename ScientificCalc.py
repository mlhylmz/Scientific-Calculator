import math
import SimpCalcClass

class ScientificCalcClass(SimpCalcClass.simpCalcClas):
    def usAl(self):
        print("Sonuç : ",math.pow(self.x,self.y))
    def kareAl(self):
        print("Sonuç : ",math.pow(self.x,self.y))
    def faktoriyel(self):
        print("Sonuç : ",math.factorial(self.x))
    def log(self):
        print("Sonuç : ",math.log(self.x,self.y))
    def sin(self):
        print("Sonuç : ",math.sin(self.x))
    def cos(self):
        print("Sonuç : ",math.cos(self.x))
    def tan(self):
        print("Sonuç : ",math.tan(self.x))
    def cot(self):
        print("Sonuç : ",1 / (math.tan(self.x)))
    def cosec(self):
        print("Sonuç : ",1 / (math.sin(self.x)))
    def sec(self):
        print("Sonuç : ",1 / (math.cos(self.x)))
    def sin1(self):
        print("Sonuç : ",math.sin(math.radians(self.x)))
    def cos1(self):
        print("Sonuç : ",math.cos(math.radians(self.x)))
    def tan1(self):
        print("Sonuç : ",math.tan(math.radians(self.x)))
    def cot1(self):
        print("Sonuç : ",1 / math.tan(math.radians(self.x)))
    def cosec1(self):
        print("Sonuç : ",1 / math.sin(math.radians(self.x)))
    def sec1(self):
        print("Sonuç : ",1 / math.cos(math.radians(self.x)))