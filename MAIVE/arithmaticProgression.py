import random

class ArithmaticProgression():
    
    def __init__(self):
        # super().__init()
        self.AP = []
    
    def AP_generateAP(self, **kwargs):
        """To generate an Arithmatic progression. If no arguments, then random AP of 10 elements, otherwise provide a, d, and n"""
        
        if(len(kwargs) != 0):
            
            try:
                if(len(kwargs) > 3):
                    raise Exception("Please pass only 'a', 'd' and 'n'.")

                # if(kwargs["a"] and kwargs["d"] and kwargs["n"]) in kwargs:
                if "a" in kwargs and "d" in kwargs and "n" in kwargs:
                    
                    

                    if((type(kwargs["a"]) is int or type(kwargs["a"]) is float) and (type(kwargs["d"]) is int or type(kwargs["d"]) is float) and (type(kwargs["n"]) is int or type(kwargs["n"]) is float) ):
                        
                        # n cannot be below 0 or float
                        if ((kwargs["n"] > 0) and (type(kwargs["n"] is int))):
                            
                            
                            a = kwargs["a"]
                            d = kwargs["d"]
                            n = kwargs["n"]
                            
                            self.AP = [a + (i-1)*d for i in range(1, n+1)]
                        
                            return self.AP
                        
                        else:
                            raise TypeError("The value of 'n' can only be a positive integer greater than 0")
                        
                        
                        
                    else:
                        raise TypeError("Please enter only integer/float values as input")
                        
                    
                else:
                    raise KeyError("Missing input(s) from the user. Please provide only a (first element), d (difference) and n (number of elements)")
            
            except KeyError as e:
                return e
            
            except TypeError as e:
                return e
            
            except Exception as e:
                return e

        else:
            a = random.randint(-101,101)
            d = random.randint(-101,101)
            n = 10
            
            self.AP = [a + (i-1)*d for i in range(1, n+1)]   # AP formula
            
            # for i in range(1, n+1):
            #     element = a + (i-1)*d   # AP formula
                
            #     # self.AP.append(element)
                
            return self.AP
                
                
            

        
    
    def AP_checkIfAP(self, list=[]):
        """Function to check if the LIST is an Arithmatic Progression or not. Returns TRUE or FALSE"""
        
        try:
            if (len(list) != 0):
                if(len(list) >= 3):
                    
                    a = list[0]
                    n = len(list)
                    d = list[1] - a # this should be constant throughout
                    
                    for i in range(2, n): # starting with 3rd element since a, a+d, a+2d and then n-1= (3-1)d = 2d
                        element = a + (i)*d 
                        
                        if(list[i] != element):
                            return False
                    # if the for loop fully executed
                    return True
                    
                    # diff = list[1] - a
                    
                    # diff_test = 0
                    
                    
                    
                    # for element in list:
                            
                    #     # to check if all the elements are int or float
                        
                    #     if(type(element) is not int) and (type(element) is not float):
                    #         raise Exception("Please provide INTEGER or FLOAT datatype in the list only.")

                    #     # checking if AP
                        
                    #     if element == a:
                    #         continue
                        
                    #     diff_test = element - a
                        
                    #     if (diff == diff_test):
                    #         d = diff_test
                    #         return True # an AP
                    #     else:
                    #         return False # not an AP

                else:
                    raise Exception("List should have at least 3 or more elements to check for Arithmatic progression.")
                    
            else:
                raise Exception("LIST not found! Please input a list.")
            
        
        
        except Exception as e:
            return e
    
    
    def AP_findNthElement(self):
        pass
    
    def AP_findN(self):
        pass
    
    def AP_findDifference(self):
        pass
    
    def AP_findSum(self):
        pass