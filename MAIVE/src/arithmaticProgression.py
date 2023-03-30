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
    
    
    def AP_findNthElement(self, **kwargs):
        """Function to find the nth element from an AP. Please provide a, d and n."""
        
        try:
            
            if(len(kwargs) == 3):
                
                if("a" in kwargs and "d" in kwargs and "n" in kwargs):
                
                    if((type(kwargs["a"]) is int or type(kwargs["a"]) is float) and (type(kwargs["d"]) is int or type(kwargs["d"]) is float) and (type(kwargs["n"]) is int)):
                        
                        if (kwargs["n"]>0):
                            
                            a = kwargs["a"]
                            d = kwargs["d"]
                            n = kwargs["n"]
                            
                            element = a + (n-1)*d
                        
                            return element # the nth term
                        
                        else:
                            raise Exception("The value of n cannot be smaller than 0.")
                    
                    else:
                        raise Exception("Please enter only INT or FLOAT datatype value, except n which can only be a positive integer")
                
                else:
                    raise Exception("Only input a, d and n")
            
            else:
                raise Exception("Please input only a (first term), d (difference) and n (nth term to find)")
            
        except Exception as e:
            return e
        
    
    def AP_findN(self, **kwargs):
        """Function to find the the number of term if a, d and an is provided"""
        try:
            if(len(kwargs) == 3):
                
                if("a" in kwargs and "d" in kwargs and "an" in kwargs):
                    
                    if((type(kwargs["a"]) is int or type(kwargs["a"]) is float) and (type(kwargs["d"]) is int or type(kwargs["d"]) is float) and (type(kwargs["an"]) is int or type(kwargs["an"]) is float)):
                        
                        a = kwargs["a"]
                        d = kwargs["d"]
                        an = kwargs["an"]
                        
                        n = int((an - a) / d + 1)
                        
                        if( n < 1): # if n is smaller than 1, then there is no AP
                            raise Exception("Invalid inputs! No A.P. found.")
                        
                        # now we will test achieved n
                        n_test = 0
                        
                        an_test = self.AP_findNthElement(a=a, d=d, n=n)
                        
                        if(an_test == an):
                            return n
                        else:
                            raise Exception("Invalid inputs! No A.P. found.")
                
                        
                        
                    else: 
                        raise Exception("The values can only be an Integer or float")
                    
                else:
                    raise Exception("Input only a, d and an, other keywords won't be accepted")
                
            else:
                raise Exception("Please input only a (first term), d (difference) and an (the nth term)")
        
        except Exception as e:
            return e
        
    
    def AP_findDifference(self, **kwargs):
        try:
            if(len(kwargs) == 3):
                
                if("a" in kwargs and "n" in kwargs and "an" in kwargs):
                    
                    if((type(kwargs["a"]) is int or type(kwargs["a"]) is float) and (type(kwargs["an"]) is int or type(kwargs["an"]) is float) and (type(kwargs["n"]) is int)):
                        
                        if(kwargs["n"] < 3):
                            raise Exception("The AP should have atleast 3 elements in order to find the correct difference")
                        
                        if(kwargs["a"] == kwargs["an"]):
                            raise Exception("This is not an AP. Please enter correct values.")
                        
                        a = kwargs["a"]
                        an = kwargs["an"]
                        n = kwargs["n"]
                        
                        d = (an - a)/(n-1)
                        
                        # testing
                        
                        an_test = self.AP_findNthElement(a=a, d=d, n=n)
                        
                        if(an_test == an):
                            return d
                        else:
                            raise Exception("No AP found! Please pass correct inputs.")
                        
                    else: 
                        raise Exception("The values can only be an Integer or float")
                    
                else:
                    raise Exception("Input only a, n and an, other keywords won't be accepted")
                
            else:
                raise Exception("Please input only a (first term), n (number of element) and an (the nth term)")
        
        except Exception as e:
            return e
    
    def AP_findSum(self, **kwargs):
        try:
            if(len(kwargs) == 3):
                
                if ("a" in kwargs and "d" in kwargs and "n" in kwargs):
                    
                    if((type(kwargs["a"]) is int or type(kwargs["a"]) is float) and (type(kwargs["d"]) is int or type(kwargs["d"]) is float) and (type(kwargs["n"]) is int )):
                        
                        a = kwargs["a"]
                        d = kwargs["d"]
                        n = kwargs["n"]
                        
                        if(n < 3):
                            raise Exception("The value of n cannot be smaller than 3 in order to find the sum of AP")
                        
                        sum = (n/2) * (2*a + (n-1) * d)
                        
                        return sum
                    
                    
                    else:
                        raise Exception("Please enter only Integer or float value")
                    
             
                    
                else:
                    raise Exception("Please input a, d and n only") 
                
            else:
                raise Exception("Please input a (first term), d (difference) and n(number of terms)")
        
        except Exception as e:
            return e
        

# This is enough to give idea about the package, more functions will be added after successful deployment of the dummy version.
