class Probability:
    
    def __init__(self):
        self.event = 0
        self.probability = 0
        
    def P_probability(self, **kwargs):
        try:
            
            if(not len(kwargs) == 0):
            
                for (key,value) in kwargs.items():
                    print(value)
                s = kwargs['s']
                e = kwargs['e']
                self.probability = s/e
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
        
    
        
        