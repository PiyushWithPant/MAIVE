import math
from fractions import Fraction

class QuadraticEquation():
    
    def __init__(self):
        self.equation = ""
        
    def QE_roots(self, **kwargs):
        """Function to return the roots alpha and beta (A quadratic equation only has 2 roots) of the quadratic equation. It returns a Dictionary with keys alpha and beta as roots """
        
        
        try:
           
            if(len(kwargs) == 3):
                
                if( "a" in kwargs and "b" in kwargs and "c" in kwargs):
                    
                    # the type error handling can be added but is not added because user can enter bracket terms also
                    
                    a = kwargs["a"]
                    b = kwargs["b"]
                    c = kwargs["c"]
                    
                    # alpha_num, alpha_den = ( (- b + math.sqrt( b**2 - 4*a*c)) / (2*a) ).as_integer_ratio()
                    # beta_num, beta_den = ( (- b + math.sqrt( b**2 - 4*a*c)) / (2*a) ).as_integer_ratio()
                    
                    alpha = Fraction((- b + math.sqrt( b**2 - 4*a*c)) / (2*a) )
                    beta = Fraction((- b - math.sqrt( b**2 - 4*a*c)) / (2*a) )
                    
                    
                    
                    
                    roots = {
                        "alpha": alpha,
                        "beta": beta,
                    }
                    
                    return roots
                    
                else:
                    raise Exception("Please enter a, b and c as the real numbers of the quadratic equation")
            else:
                raise Exception("Please enter a, b and c as the real numbers of the quadratic equation")
            
        except Exception as e:
            return e
        
        
        return "hi"
        