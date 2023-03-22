import math
from fractions import Fraction

class QuadraticEquation():
    
    def __init__(self):
        self.roots = {}
        
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
        
        
      
    
    def QE_typeOfRoots(self, **kwargs):
        
        try:
            pass
        except Exception as e:
            return e
        