import random
import numpy as np

def fun(x, y):
  return (5-x**2+6*x-2*y**2+8*y)*(x**2)
  #return -x**2

class RegneFar(object):

    def __init__(self, antallNoder, id, randTall):
        self.__id = id
        self.__randTall = randTall
        self.__regneArray=[]
        self.__antallNoder = antallNoder
        for i in range(antallNoder):
            self.__regneArray.append(RegneNode(id=i))

    #    print(len(self.__regneArray))

    def __str__(self):
        for n in self.__regneArray:
            return n.tekst()

    def printRegneArray(self):
        for n in self.__regneArray:
            print(n.get_id())
    
    def get_id(self):
        return self.__id

    def get_antall(self):
        return len(self.__regneArray)

    def findMaxPoint(self,x,y):
        tolerance = 0.0000001
        bX = x
        bY = y
        tmpX = x
        tmpY = y
        z = fun(bX,bY)
        v = np.ndarray((self.__antallNoder,),float)
        for s in range(1000):
            for i in range(self.__antallNoder):
                #scale = ((i+1)/self.__antallNoder)/(((self.__antallNoder+1)/2)/self.__antallNoder)
                scale = ((i+1)*2*self.__antallNoder)/(self.__antallNoder*(self.__antallNoder+1))
                #v[i] = self.__regneArray[i].evaluateFunctionAt(
                #    tmpX*scale,tmpY*scale)
                v[i] = fun(tmpX*scale,tmpY*scale)
                #print(("for i ={}, (x= {}, y = {}), z = {}, scale = {}").format(i,tmpX*scale,tmpY*scale,v[i], scale))
                if v[i]>z:
                    bX = tmpX*scale
                    bY = tmpY*scale
                    z = v[i]
            if abs(bX)<tolerance:
                bX = 0
            if abs(bY)<tolerance:
                bY = 0
            tmpX = bX
            tmpY = bY
        if abs(z)<tolerance:
            z = 0    
        
        return bX,bY,z

# lage en while løkke i den over istedet.. Da kan man straffe for lang tid??
   

class RegneNode(object):    
    def __init__(self, id):
        self.__id = id
        self.__weigth = 0.5
    
    def evaluateFunctionAt(self,x,y):
        return fun(x,y)

    #def updateWeight(self, factor):
    #    weigth = weigth * factor
    
    def getWeigth(self):
        return self.__weigth

    def tekst(self):
        return "Id {}".format(self.__id)

    def __str__(self):
        return "Id {}".format(self.__id)
    
    def get_id(self):
        return self.__id
    
a = 300
random.seed(12)
regneFarArray = []
for i in range(25):
    regneFarArray.append(RegneFar(id = i, antallNoder = 25,
        #randTall = random.uniform(-a, a)))
        randTall = random.randint(-a,a)))

random.seed(12)
for n in regneFarArray:
        # x = random.uniform(-a, a)
        # y = random.uniform(-a, a)
         x = random.randint(-a,a)
         y = random.randint(-a,a)
         bestX, bestY, bestZ = n.findMaxPoint(x,y)
         print("ID {} - max point: {} (X = {}, Y = {})".format(
             n.get_id(), round(bestZ,3), round(bestX,3),round(bestY,3)))
         
print(fun(2.78,2.14))
#for n in regneFarArray:
#    print("RegneFar id {}".format(n.get_id()))
#    print("Antall {}".format(n.get_antall()))
#    n.printRegneArray()

# trekk et random tall mellom -30 og 30d