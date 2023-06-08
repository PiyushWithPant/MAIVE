import math
import random
from fractions import Fraction

import numpy as np
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import statsmodels.api as sms

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.feature_selection import f_regression

from sklearn.cluster import KMeans




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
        self.frequency = None
        
        
        
        
        
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
           2. Probabily of event A as 'pa' and event B as 'pb'\n
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
                    pab = kwargs["pab"]
                    
                    product = pa * pb
                    
                    if(pab ==  product):
                        self.isIndependent = True
                        return self.isIndependent
                    else:
                        self.isIndependent = False
                        return self.isIndependent
                
                else:
                    raise Exception("Please provide a and b as set of events in LIST form OR just pab as probability of A intersection B, along with pa and pb as probability of a and b!")
                
            else:
                raise Exception("Please provide events a and b to check their independent nature!")
        except Exception as e:
            return e
        
    
    
    
    def P_frequency(self, listOfEvents, event):
        
        """
        Function to return the frequency (in numbers) of an event in a given list of events.\n
        Input the data in order like this ( list_of_events , event_of_which_you_need_frequency)
        
        """
        
        try:
            
            if(type(listOfEvents) == list):
                
                if(len(listOfEvents) == 0):
                    raise Exception("The list is empty")
                
                
                self.frequency = 0
                
                for object in listOfEvents:
                    
                    if( object == event):
                        
                        self.frequency += 1
                        
                
                        
                return self.frequency
                    
                    
                    
                    
            
            else:
                raise Exception("Please input a list of events/objects, other formats are not accepted.")
            
            
        except Exception as e:
            return e
        
    
    
    
        

    def P_frequencyDistribution(self, data):
        """
        Function to generate a frequency distribution table. Returns a dictionary with keys as list data items and values as their respective frequency
        """
        try:
            if(type(data) == list):
                
                table =  {}  # this table will hold values and their frequency
        
                if(len(data) > 0):
                    
                    for i in data:
                        
                        table[i] = 0    # initializing the count of frequency
                        
                        for j in data:
                            
                            if i == j:
                                
                                table[i] += 1   # adding 1, even if it finds itself since we started it with 0
                    
                    return table
                
                else:
                    raise Exception("The list is empty, please provide elements in the list as well.")
            else:
                raise Exception("Please input a list of events/objects, other formats are not accepted")
            
        except Exception as e:
            return e
        
    
    
    
    
    
    def P_relativeFrequency(self, data):
        """
        Function to generate relative frequency 
        """
        try:
            if(type(data) == list):
        
                if(len(data) > 0):

                    
                    frequencyTable = self.P_frequencyDistribution(data)
                    
                    table = {}
                    
                    for key, value in frequencyTable.items():
                        table[key] = value / len(data)
                        
                        
                    return table
                    
                    
                
                else:
                    raise Exception("The list is empty, please provide elements in the list as well.")
            else:
                raise Exception("Please input a list of events/objects, other formats are not accepted")
            
            
        except Exception as e:
            return e
    
    
    def P_compliment(self, a):
        """Function to return the compliment of an event. Please input the probability of the event as argument."""
        try:
            
            if(type(a) == int or type(a) == float):
                
                if(a > 1 or a < 0):
                    raise Exception("Please provide correct value of the probability of event 'a'.")
                
                return 1-a

            else:
                raise Exception("Please provide INT or FLOAT datatype only")
            
            
        except Exception as e:
            return e
    
    
    
    def P_conditionalProbability(self, **kwargs):
        """Function to return the conditional probability i.e. P(a|b). Please input keyworded arguments as\n
        CASE A:  'pab' Probability of A intersection B and 'pb' Probability of event B with 's' as sample space\n
        NOTE: If you don't have pab and pb, then enter \n
        CASE B: 'a' List of set A and 'b' List of set B with 's' as sample space\n
        It will return the INT/FLOAT value which is result of P(a|b)
        """
        
        try:
            if(len(kwargs) == 3):
                
                if("pab" in kwargs and "pb" in kwargs and "s" in kwargs):
                    
                    return round(kwargs["pab"]/kwargs["pb"], 2)
                
                elif("a" in kwargs and "b" in kwargs and "s" in kwargs):
                    
                    if( type(kwargs["a"]) != list or type(kwargs["b"]) != list):
                        raise Exception("Please enter a and b as LIST")
                    
                    if( len(kwargs["a"]) == 0 or len(kwargs["b"]) == 0):
                        raise Exception("The list is empty")
                    
                    if( kwargs["s"] < ( len(kwargs["a"]) + len(kwargs["b"]) )):
                        raise Exception("Sample value is not appropriate.")
                        
                   
                    ab = len(set(kwargs["a"]).intersection(set(kwargs["b"])))
                    
                    Pab = ab / kwargs["s"]
                    Pb = len(kwargs["b"]) / kwargs["s"]
                    
                    return round(Pab/Pb,2)
                    
                else:
                    raise Exception("Please input as per CASE A or CASE B (Read function documentation).")
                  
            
            
            else:
                raise Exception("Please input as per CASE A or CASE B (Read function documentation).")
                
        except Exception as e:
            return e
    

    
    def probabilityDistributionFunction(self, data):
        """
        Returns the graph of Probability Distibution Function\n
        Input the data as an attribute (LIST)
    
        """
        try:

            # Parameters for the normal distribution
            mu = self.mean(data)  # mean
            sigma = self.standardDeviationS(data)  # standard deviation

            # Generate an array of values for the x-axis
            # x = np.linspace(-5, 5, 100)
            x = np.array(data)

            # Calculate the corresponding probability density values using the normal distribution function
            pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2))

            # Plot the PDF
            plt.plot(x, pdf)
            plt.xlabel('x')
            plt.ylabel('Probability Density')
            plt.title('PDF')
            return plt.show()
    
        
        except Exception as e:
            return e
    
    
    
    
    
    # STATISTICS
    
    def mean(self, list):
        """
        Returns the mean value of the sample presented as a LIST
        """
        try:
            
            # total = sum(list)
            # length = len(list)
            # mean = total / length
            # return mean
            
            m = st.mean(list)
            return m
            
        except Exception as e:
            return e
    
    
    def mode(self, list):
        """
        Returns the mode value of the sample presented as a LIST
        """
        try:
            m = st.mode(list)
            return m
        except Exception as e:
            return e
    
    
    def median(self, list):
        """
        Returns the median value of the sample presented as a LIST
        """
        try:
            m = st.median(list)
            return m
        except Exception as e:
            return e
    
    
    def varianceS(self, list):
        """
        Returns the variance of the SAMPLE presented as a list
        """
        try:
            v = st.variance(list)
            return v
        except Exception as e:
            return e
        
    def varianceP(self, list):
        """
        Returns the variance of the POPULATION presented as a list
        """
        try:
            v = st.pvariance(list)
            return v
        except Exception as e:
            return e
        
        
    
    def standardDeviationS(self, list):
        """
        Returns the standard deviation of Sample passed as a list
        """
        try:
            sd = st.stdev(list)
            return sd
        except Exception as e:
            return e
    
    def standardDeviationP(self, list):
        """
        Returns the standard deviation of population passed as a list
        """
        try:
            
            sd = st.pstdev(list)
            return sd
        except Exception as e:
            return e
    
    def covariance(self,x,y):
        """
        Returns the covariance between two features x and y passed as a list
        """
        try:
            
            cov = st.covariance(x,y)
            return cov
        
        except Exception as e:
            return e
    
    def correlation(self, x,y):
        """
        Returns the correlation between two features x and y passed as a list
        """
        try:
            
            cor = st.correlation(x,y)
            return cor
        
        except Exception as e:
            return e
    
    
        
       
    # DATA SCIENCE AND ARTIFICIAL INTELLIGENCE
    
        
    def confusionMatrix(self, model, x, y):
        """
        Returns the confusion matrix for your ML model. (For Logistic regression model)\n
        Input as - confusionMatrix(model, x, y)\n
        where model = logistic regression model. x = input, and y = target
        """
        try:
            
            #Predict the values using the Logit model
            pred_values = model.predict(x)
            # Specify the bins 
            bins=np.array([0,0.5,1])
            # Create a histogram, where if values are between 0 and 0.5 tell will be considered 0
            # if they are between 0.5 and 1, they will be considered 1
            cm = np.histogram2d(y, pred_values, bins=bins)[0]
            # Calculate the accuracy
            # accuracy = (cm[0,0]+cm[1,1])/cm.sum()
            
            return cm
            
            
        except Exception as e:
            return e
        
        
    def logisticModelAccuracy(self, model, x, y):
        """
        Returns the accuracy of your ML model. (For Logistic regression model)\n
        Input as - confusionMatrix(model, x, y)\n
        where model = logistic regression model. x = input, and y = target
        """
        try:
            
            pred_values = model.predict(x)

            bins=np.array([0,0.5,1])

            cm = np.histogram2d(y, pred_values, bins=bins)[0]
            # Calculate the accuracy
            accuracy = (cm[0,0]+cm[1,1])/cm.sum()
            
            return accuracy
            
            
        except Exception as e:
            return e
        
        
        
        
    def r2(self, model, x, y):
        """
        Returns the R2 of the ML model.\n
        Input as - r2(model, x , y) \n
        1. model - linear model\n
        2. x - reshaped input array\n
        3. y - target data array
        """
        try:
            
            return model.score(x,y)
        
        except Exception as e:
            return e
    
    
    
    def adjustedR2(self, model, x , y):
        """
        Returns the adjusted R2 of the ML model. Input as => adjustedR2(model, x, y)
        """
        try:
            
            m = x.shape[0]
            n = x.shape[1]
            
            r2 = model.score(x,y)
            
            adj = 1 - (1-r2) * (m-1)/(m-n-1)
            
            return adj
            
        except Exception as e:
            return e
    
    
    
    def p_value(self, x, y):
        """
        Returns the p-value of the model. \n
        Input the X and Y (reshaped)\n
        
        """
        try:
            f_stats, p_value = f_regression(x,y)
            return p_value
        
        except Exception as e:
            return e 
        
        
        
    def f_stats(self, x, y):
        """
        Returns the f-stats of the model. \n
        Input the X and Y (reshaped)\n
        
        """
        try:
            f_stats, p_value = f_regression(x,y)
            return f_stats
        
        except Exception as e:
            return e 
        
        
        
    def bias(self, model):
        """
        Returns the bias of the model. \n
        Input the trained model as bias(model) [Linear model preferrably]
        """
        try:
            return model.intercept_
        except Exception as e:
            return e
    
    
    
    def weights(self, model):
        """
        Returns the weight(s) of the features. \n
        Input the trained model as weights(model) [Linear model preferrably]
        """
        try:
            weights = model.coef_
            
            return weights
        
        except Exception as e:
            return e
    
    
    
    
    def regressionReport(self, x, y):
        """
        Returns regression report as a dataframe. \n
        Input x and y  (reshaped)
        """
        try:
            
            X = sms.add_constant(x)
            
            linReg = sms.OLS(y,X).fit()
            
            return linReg.summary()
            
        except Exception as e:
            return e
        
        
        
    def logisticReport(self, x ,y):
        """
        Returns logistic report as a dataframe. \n
        Input x and y  (reshaped)
        """
        try:
            
            X = sms.add_constant(x)
            
            logReg = sms.logit(y,X).fit()
            
            return logReg.summary()
            
            
        except Exception as e:
            return e
        
        
        
    def scatterPlot(self, x, y, xlabel, ylabel, title):
        """
        Returns scatter plot of the input x and y along with their labels, title, etc. Input in sequence as-\n
        scatterPlot( x, y, xlabel, ylabel, title)
        """
        try:
            plt.scatter(x,y)
            plt.xlabel(xlabel, fontsize=15)
            plt.ylabel(ylabel, fontsize=15)
            plt.title(title, fontsize=20)
            return plt.show()
            
            
        except Exception as e:
            return e
        
    
    
    def distPlot(self,x):
        """
        Returns the distribution of the feature passed.
        """
        try:
           
            return sns.displot(x), plt.show()
            
        except Exception as e:
            return e
        
    
    
       
    def Cluster(self):
        """
        Function to perform the clustering of the provided dataset using KMeans algorithm
        """
        try:
            pass
        except Exception as e:
            return e
        
    def elbowMethod(self):
        """
        Returns the visual representation of the elbow method showing WCSS for number of clusters.
        """
        try:
            pass
        except Exception as e:
            return e
       
       
       
    def LinearRegression(self, x, y):
        """
        Returns the trained Linear Regression model.\n
        Input as - LinearRegression( x , y )\n
        where x = input data, y = target data\n
        Note: Please ensure data format is compatible.
        """
        try:
            
            X = x.values.reshape(-1,1)
            
            model = LinearRegression()
            
            model.fit(X, y)
            
            return model
            
        except Exception as e:
            return e
       
       
       
       
    def LogisticRegression(self, x,y):
        """
        Returns the trained Logistics Regression model.\n
        Input as - LogisticRegression( x , y )\n
        where x = input data, y = target data\n
        Note: Please ensure data format is compatible.
        """
        try:
            X = x.values.reshape(-1,1)
            
            model = LogisticRegression()
            
            model.fit(X, y)
            
            return model
            
        except Exception as e:
            return e
       
       
      
    def summaryTable(self,x, y):
        """
        Returns a dataframe that shows the summary of the Linear regression model.\n
        Input as - summaryTable(x, y)\n
        x = input data (with feature names), y = target data
        """
        try:
            
            reg = LinearRegression()

            reg.fit(x, y)
            
            summary = pd.DataFrame(
                data = x.columns.values,
                columns =['Features']
            )

            summary['Weight'] = reg.coef_
            pvalue = self.p_value(x,y)
            summary['p-value'] = pvalue.round(2)

            return summary
            
        except Exception as e:
            return e
       
       
       
      
    def createNPZ(self,):
        """
        Saves the given data file in NPZ format
        """
        try:
            pass
        except Exception as e:
            return e
       
       
    
      
    def createCSV(self):
        """
        Saves the given data file in CSV format
        """
        try:
            pass
        except Exception as e:
            return e
       
    
    def featureScaling(self):
        """
        Performs feature scaling on the given data and returns it
        """
        try:
            pass
        except Exception as e:
            return e
       
       
    def nn(self):
        """
        To create your basic Neural Network\n
        1. Add number of layers you want as layers\n
        2. Optimizer as opt\n
        3. Loss Function as loss\n
        4. Epochs as e
        """
        try:
            pass
        except Exception as e:
            return e
       
       
      
       
       
       
       
# CREATE DISTRIBUTION AND BUILD = python setup.py sdist bdist_wheel
# UPLOAD PACKAGE = twine upload dist/*
# CHECK DISTRIBUTION = twine check dist/*
# TO UPDATE PACKAGE = twine upload --repository-url https://upload.pypi.org/legacy/ dist/*







        
    

        
    