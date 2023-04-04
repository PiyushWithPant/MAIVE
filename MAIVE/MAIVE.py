import math
import random
from fractions import Fraction


class Maive():
    
    
    def __init__(self):
        """MAIVE"""
        
        # Arithmatic Progression
        self.AP = []
        
        # Quadratic Equation
        self.roots = {}
        
        # Probability
        self.event = None
        self.probability = None
        self.isIndependent = None
        
        
        
        
        
    # ARITHMATIC PROGRESSION
    
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
        
        
    
    # QUADRATIC EQUATION
    
    def QE_roots(self, **kwargs):
        """Function to return the roots alpha and beta (A quadratic equation only has 2 roots) of the quadratic equation. It returns a Dictionary with keys alpha and beta as roots """
        
        
        try:
           
            if(len(kwargs) == 3):
                
                if( "a" in kwargs and "b" in kwargs and "c" in kwargs):
                    
                
                    
                    # the type error handling can be added but is not added because user can enter bracket terms also
                    
                    a = kwargs["a"]
                    b = kwargs["b"]
                    c = kwargs["c"]
                    
                    d = b**2 - 4*a*c
                    
                    
                    if(b == c == 0):    # if b==c == 0 then both roots are 0
                        self.roots = {
                            "alpha": 0,
                            "beta": 0,
                        }
                        return self.roots
                    
                    if( d > 0): # real and unequal roots
                    
                        D = math.sqrt( b**2 - 4*a*c)
                            
                        # alpha_num, alpha_den = ( (- b + math.sqrt( b**2 - 4*a*c)) / (2*a) ).as_integer_ratio()
                        # beta_num, beta_den = ( (- b + math.sqrt( b**2 - 4*a*c)) / (2*a) ).as_integer_ratio()
                                                
                        alpha = Fraction((- b + D) / (2*a) )
                        beta = Fraction((- b - D) / (2*a) )
                        
                        
                        self.roots = {
                            "alpha": alpha,
                            "beta": beta,
                        }
                        
                        return self.roots
                    
                    elif(d == 0):   # Real and equal roots
                        self.roots = {
                            "alpha": Fraction(-b/2*a),
                            "beta": Fraction(-b/2*a),
                        }
                        
                        return self.roots
                    
                    elif(d < 0): # Unequal and imaginary roots
                        return "This quadratic equation has unequal and imaginary roots since D < 0"
                    
                    else:
                        raise Exception("Invalid value!")
                    
                else:
                    raise Exception("Please enter a, b and c as the real numbers of the quadratic equation")
            else:
                raise Exception("Please enter a, b and c as the real numbers of the quadratic equation")
            
        except Exception as e:
            return e
        
    
    def isPerfectSquare(self,n):
        """Function to verify if the given number is a perfect square or not, returns Boolean"""
        num = int(math.sqrt(n))
        res = (num * num) == n
        return res
      
    
    def QE_typeOfRoots(self, **kwargs):
        """Function to return the type of roots the quadratic equation has."""
        try:
            if(len(kwargs) == 3):
                
                if( "a" in kwargs and "b" in kwargs and "c" in kwargs):
                    
                    a = kwargs["a"]
                    b = kwargs["b"]
                    c = kwargs["c"]
                    
                    d = b**2 - 4*a*c
                    
                    if(d == 0):
                        return "Real and Equal roots"
                    
                    elif(d < 0):
                        return "Unreal, Unequal and Imaginary (complex) roots"
                    
                    elif(d > 0):
                        
                        if(self.isPerfectSquare(d)):
                            return "Real, unequal and Rational roots"
                        elif(not self.isPerfectSquare(d)):
                            return "Real, unequal and Irrational roots"
                        else:
                            raise Exception("Invalid input!")
                    else:
                        raise Exception("Invalid input!")
                    
                    
                else:
                    raise Exception("Please enter a, b and c as the real numbers of the quadratic equation")
            else:
                raise Exception("Please enter a, b and c as the real numbers of the quadratic equation")
        except Exception as e:
            return e
        
        
        
        
    # PROBABILITY
    
    def P_probability(self, **kwargs):
        """
        To find the probability of an event,\n
        s = sample space \n
        e = favourable event \n
        """
        
        try:
            
            if(not len(kwargs) == 0):
                
                
                
                s = kwargs['s']
                e = kwargs['e']
                
            
                for (key,value) in kwargs.items():  # to check data type of each value in the kwargs
                    
                    if(type(value) != int and type(value) != float):
                        raise Exception("Please enter only INPUT or FLOAT value!")
                    
                    
                # if( s < e): # checking if sample space is greater than e
                #     raise Exception("The sample space cannot be smaller than the favourable event!")
               
                # basic probability
               
                self.probability = round(e/s, 2)
                
                
                if(self.probability > 1 or self.probability < 0):
                    raise Exception("Invalid input!")
                
                return self.probability
            
            else:
                raise Exception("Please provide arguments!")
            
            
        except Exception as e:
            return e
    
    
    
    def P_isIndependentEvent(self, **kwargs):
        """Function to check if two events are independent or not\n
           Please input the following:\n
           1. set of event A and event B in LIST datatype as "a" and "b", otherwise Probability of A intersection B as "pab"\n
           2. probabily of event A as pa and event B as pb\n
           This function returns TRUE if events are independent, otherwise FALSE
        """
        try:
            if(len(kwargs) != 0):
                
                if( ("a" in kwargs and "b" in kwargs) and ("pa" in kwargs) and ("pb" in kwargs)):           
                    
                    # if pab is not provided
                    a = kwargs["a"]
                    b = kwargs["b"]
                    pa = kwargs["pa"]
                    pb = kwargs["pb"]
                    
                
                    a_intersection_b = set(a).intersection(set(b))
                    
                    P_a_intersection_b = len(a_intersection_b)/len(a)
                    
                    product  = pa * pb
                    
                    if( product == P_a_intersection_b):
                        self.isIndependent = True
                        return self.isIndependent
                    
                    else:
                        self.isIndependent = False
                        return self.isIndependent
                    

                                        
                elif("pab" in kwargs and "pa" in kwargs and "pb" in kwargs):
                    
                    pa = kwargs["pa"]
                    pb = kwargs["pb"]
                    
                    product = pa * pb
                    
                    if(kwargs["pab"] ==  product):
                        self.isIndependent = True
                        return self.isIndependent
                    else:
                        self.isIndependent = False
                        return self.isIndependent
                
                else:
                    raise Exception("Please provide a and b as set of events in LIST form OR just pab as probability of A intersection B, along with pa and pb as probability of a and b!")
                
                
                
                
                
                
                pass
            else:
                raise Exception("Please provide events a and b to check their independent nature!")
        except Exception as e:
            return e
        
    
        
        

        
    
        
       
# CREATE DISTRIBUTION AND BUILD = python setup.py sdist bdist_wheel
# UPLOAD PACKAGE = twine upload dist/*
# CHECK DISTRIBUTION = twine check dist/*
# TO UPDATE PACKAGE = twine upload --repository-url https://upload.pypi.org/legacy/ dist/*







        
    

        
    