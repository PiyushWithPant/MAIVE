class Probability:
    
    def __init__(self):
        self.event = 0
        self.probability = 0
        
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
        try:
            pass
        except Exception as e:
            return e
        
    
        
        