import setuptools

VERSION = "0.0.3.2"
DESCRIPTION = "Mathematics and Ariticial Intelligence and Visualization Extended"
 

with open("README.md", "r") as fh:
    LONG_DESCRIPTION  = fh.read()

setuptools.setup(
    
    name="MAIVE",  
       
    version=VERSION, 
           
    author="Piyush Pant",  
    
    author_email= "piyushpant15@gmail.com",  
    
    keywords= [
        "MAIVE","Artificial Intelligence", "Machine Learning", "Maths", 
    ],
     
    description=DESCRIPTION,
    
    long_description= LONG_DESCRIPTION ,      # Long description read from the the readme file
    
    long_description_content_type="text/markdown",
    
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    
    # python_requires='>=3.6',                # Minimum version requirement of the package
    
    # py_modules=["quicksample"],             # Name of the python package
    
    # package_dir={'':'quicksample/src'},     # Directory of the source code of the package
    
    
    
    install_requires=["numpy", "matplotlib", "pandas","statsmodels", "seaborn","scikit-learn", "tensorflow"],                     # Install other dependencies if any
)