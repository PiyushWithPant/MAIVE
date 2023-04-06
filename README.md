<img src = "/assets/pictures/MAIVE%20LOGO.png">

# MAIVE

###### Mathematics for Artificial Intelligence with Visualization Extended - 2023, Piyush Pant :heart:

<hr>

Documentation <a target="_blank" rel="noopener" href="https://piyushwithpant.github.io/MAIVE/" title="MAIVE webpage" >MAIVE</a>

PyPi <a target="_blank" rel="noopener" href="https://pypi.org/project/MAIVE/" title="PYPI Maive" >MAIVE</a>

## Get started with MAIVE

MAIVE (मैव) is a powerful python package equipped with advanced mathematics to assist you in the domain of Artificial Intelligence while also providing you with visualization support. The mathematics level begins from high school to advanced, any topic that may be required in the AI domain is provided in the MAIVE. Please understand that the package is still under development, so there might be missing topics (which will be added soon). To become a contributor or if you want to suggest something, please contact us via
<a target="_blank" rel="noopener" href="https://wa.me/919145728659" title="Whatsapp | Piyush Pant" >Whatsapp</a>
or through the
<a href="https://piyushwithpant.github.io/" target="_blank" rel="noopener" title="Webpage | Piyush Pant" >Webpage </a>.

### # Installation

`$ pip install maive`

<hr>

### Documentation

Please visit the section as per your requirements. It is advised to
read the <b> HOW TO USE? </b> section before using the package.

#### HOW TO USE?

<ul>
  <li>
    <b> To import the package </b>

<code > from maive.maive import Maive </code>
<br />
<code > M = Maive() </code>
<br />
<code > isAP = M.AP_checkIfAP([10,1,34]) </code>
<br />
<code > print(isAP) </code>

OR

<code > from maive import maive </code>
<br />
<code > M = maive.Maive() </code>
<br />
<code > isAP = M.AP_checkIfAP([10,1,34]) </code>
<br />
<code > print(isAP) </code>

  </li>
  <li>
 All the functions follow a naming convention. A function's naming is divided in two parts with underscore(_). The before underscore is the domain of mathematics that the function belongs to and the part after underscore is the name of the function. for example, the function to generate an AP which is from Arithmetic Progression domain will be like - <code?>AP_generateAP()</code>
however, there is an exception for global functions like
<code> isPerfectSquare() </code>

  </li>
  <li>
 To ensure better performance, please input data with their respective keywords when working with functions. For example, <code> QE_typeOfRoots(a=100, b=-455, c=97) </code> where a,b and c are the coefficients of the quadratic equation.
  </li>
</ul>

<h6>Arithmatic Progression</h6>

<ul>
  <li >
    <code>AP_generateAP()</code>
 Function to generate an Arithmatic Progression. Please pass <b>a</b> (First term), <b>d</b> (difference) and <b>n</b> (number of terms) as keyworded arguments. If you do not pass anything, the function will return an Arithmatic progression of 10 terms with random a and d.

  </li>

<li >
  <code> AP_checkIfAP() </code>
    Function to check if a series is an Arithmatic
    progression or not. Pass the series in form of
    <b>LIST</b> as argument. The output will be a boolean
    value i.e. TRUE or FALSE.
</li>
<li >
  <code>AP_findNthElement()</code>
    Function to find the nth element of an Arithmatic
    Progression. Please provide <b>a</b> (First term),
    <b>d</b> (difference) and <b>n</b> (number of terms) as
    keyworded arguments.
</li>
<li >
  <code>AP_findN()</code>
    Function to determine the <b>n</b>. Please provide
    <b>a</b> (First term), <b>d</b> (difference) and
    <b>an</b> (the nth term) as keyworded arguments.
</li>
<li >
  <code> AP_findDifference() </code>
    Function to determine the difference d of an Arithmatic
    Progression. Please provide
    <b>a</b> (First term), <b>n</b> (number of terms) and
    <b>an</b> (the nth term) as keyworded arguments.
</li>
<li >
  <code>AP_findSum()</code>
    Function to determine the sum of an Arithmatic
    Progression. Please provide <b>a</b> (First term),
    <b>n</b> (number of terms) and <b>d</b> (difference) as
    keyworded arguments.
</li>

<h6>Quadratic Equations</h6>
<ul>

<li >
  <code>QE_roots()</code>
    Function to return the roots alpha and beta (A quadratic
    equation only has 2 roots) of the quadratic equation. It
    returns a Dictionary with keys alpha and beta as roots.
    Please provide <b>a</b> (coefficint of x<sup>2</sup> ),
    <b>b</b> (coefficient of x) and <b>c</b>(constant term)
    as keyworded arguments.
</li>
<li >
  <code>isPerfectSquare()</code>
    Function to verify if the given number is a perfect
    square or not, returns Boolean
</li>
<li >
  <code>QE_typeOfRoots()</code>
    Function to return the type of roots the quadratic
    equation has. Please provide <b>a</b> (coefficint of
    x<sup>2</sup> ), <b>b</b> (coefficient of x) and
    <b>c</b>(constant term) as keyworded arguments.
</li>
</ul>

<h6>Probability</h6>

<h6>Statistics</h6>
