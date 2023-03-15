import random

class ArithmaticProgression():
    
    def __init__(self):
        # super().__init()
        self.AP = []
    
    def AP_generateAP(self, **kwargs):
        """To generate an Arithmatic progression. If no arguments, then random AP of 10 elements, otherwise provide a, d, and n"""
        
        if(len(kwargs) != 0):
            
            try:

                # if(kwargs["a"] and kwargs["d"] and kwargs["n"]) in kwargs:
                if "a" in kwargs and "d" in kwargs and "n" in kwargs:
                    
                    if((kwargs["a"] == type(int) or kwargs["a"] == type(float)) and (kwargs["d"] == type(int) or kwargs["d"] == type(float)) and (kwargs["n"] == type(int) or kwargs["n"] == type(float)) ):
                        print("correct")
                    else:
                        raise TypeError("Please enter only integer/float values as input")
                        
                    
                else:
                    raise KeyError("Missing input(s) from the user. Please provide only a (first element), d (difference) and n (number of elements)")
            
            except KeyError as e:
                return e
            
            except TypeError as e:
                return e
            

        else:
            a = random.randint(-101,101)
            d = random.randint(-101,101)
            n = 10
            
            
            for i in range(1, n+1):
                element = a + (i-1)*d   # AP formula
                self.AP.append(element)
                
            return self.AP
                
                
            

        
    
    def AP_checkIfAP(self):
        pass
    
    def AP_findNthElement(self):
        pass
    
    def AP_findN(self):
        pass
    
    def AP_findDifference(self):
        pass
    
    def AP_findSum(self):
        pass