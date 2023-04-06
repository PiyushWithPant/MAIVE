<img src = "/assets/pictures/MAIVE%20LOGO.png">

# MAIVE 
##### Mathematics for Artificial Intelligence with Visualization Extended - 2023, Piyush Pant :heart:
         
<hr>

Documentation <a
            target="_blank"
            rel="noopener"
            href="https://piyushwithpant.github.io/MAIVE/"
            title="MAIVE webpage"
            >MAIVE</a>

PyPi <a
            target="_blank"
            rel="noopener"
            href="https://pypi.org/project/MAIVE/"
            title="PYPI Maive"
            >MAIVE</a>


## Get started with MAIVE

MAIVE (मैव) is a powerful python package equipped with advanced mathematics to assist you in the domain of Artificial Intelligence while also providing you with visualization support. The mathematics level begins from high school to advanced, any topic that may be required in the AI domain is provided in the MAIVE. Please understand that the package is still under development, so there might be missing topics (which will be added soon). To become a contributor or if you want to suggest something, please contact us via
          <a
            target="_blank"
            rel="noopener"
            href="https://wa.me/919145728659"
            title="Whatsapp | Piyush Pant"
            >Whatsapp
          </a>
          or through the
          <a
            href="https://piyushwithpant.github.io/"
            target="_blank"
            rel="noopener"
            title="Webpage | Piyush Pant"
            >Webpage </a
          >.
        </p>
      </div>


### # Installation


`$ pip install maive`

<hr>


### Documentation
Please visit the section as per your requirements. It is advised to
read the <b> HOW TO USE? </b> section before using the package.


#### HOW TO USE?

                  <ul>
                    <li>
                      <p><b> To import the package </b></p>
                      <p class="code">
                        <code class=""> from maive.maive import Maive </code>
                        <br />
                        <code class=""> M = Maive() </code>
                        <br />
                        <code class=""> isAP = M.AP_checkIfAP([10,1,34]) </code>
                        <br />
                        <code class=""> print(isAP) </code>
                      </p>
                      <p class="text-center">OR</p>
                      <p class="code">
                        <code class=""> from maive import maive </code>
                        <br />
                        <code class=""> M = maive.Maive() </code>
                        <br />
                        <code class=""> isAP = M.AP_checkIfAP([10,1,34]) </code>
                        <br />
                        <code class=""> print(isAP) </code>
                      </p>
                    </li>
                    <li>
                      <p>
                        All the functions follow a naming convention. A
                        function's naming is divided in two parts with
                        underscore(_). The before underscore is the domain of
                        mathematics that the function belongs to and the part
                        after underscore is the name of the function. for
                        example, the function to generate an AP which is from
                        Arithmetic Progression domain will be like -
                        <code>AP_generateAP()</code>

                        <br />

                        however, there is an exception for global functions like
                        <code> isPerfectSquare() </code>
                      </p>
                    </li>
                    <li>
                      <p>
                        To ensure better performance, please input data with
                        their respective keywords when working with functions.
                        For example,
                        <code> QE_typeOfRoots(a=100, b=-455, c=97) </code> where
                        a,b and c are the coefficients of the quadratic
                        equation.
                      </p>
                    </li>
                  </ul>
                </div>
              </div>
            </div>


                  <h6>Arithmatic Progression</h6>

                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                      <code>AP_generateAP()</code>
                      <p>
                        Function to generate an Arithmatic Progression. Please
                        pass <b>a</b> (First term), <b>d</b> (difference) and
                        <b>n</b> (number of terms) as keyworded arguments. If
                        you do not pass anything, the function will return an
                        Arithmatic progression of 10 terms with random a and d.
                      </p>
                    </li>

                    <li class="list-group-item">
                      <code> AP_checkIfAP() </code>
                      <p>
                        Function to check if a series is an Arithmatic
                        progression or not. Pass the series in form of
                        <b>LIST</b> as argument. The output will be a boolean
                        value i.e. TRUE or FALSE.
                      </p>
                    </li>
                    <li class="list-group-item">
                      <code>AP_findNthElement()</code>
                      <p>
                        Function to find the nth element of an Arithmatic
                        Progression. Please provide <b>a</b> (First term),
                        <b>d</b> (difference) and <b>n</b> (number of terms) as
                        keyworded arguments.
                      </p>
                    </li>
                    <li class="list-group-item">
                      <code>AP_findN()</code>
                      <p>
                        Function to determine the <b>n</b>. Please provide
                        <b>a</b> (First term), <b>d</b> (difference) and
                        <b>an</b> (the nth term) as keyworded arguments.
                      </p>
                    </li>
                    <li class="list-group-item">
                      <code> AP_findDifference() </code>
                      <p>
                        Function to determine the difference d of an Arithmatic
                        Progression. Please provide
                        <b>a</b> (First term), <b>n</b> (number of terms) and
                        <b>an</b> (the nth term) as keyworded arguments.
                      </p>
                    </li>
                    <li class="list-group-item">
                      <code>AP_findSum()</code>
                      <p>
                        Function to determine the sum of an Arithmatic
                        Progression. Please provide <b>a</b> (First term),
                        <b>n</b> (number of terms) and <b>d</b> (difference) as
                        keyworded arguments.
                      </p>
                    </li>
                  </ul>


                  <h6>Quadratic Equations</h6>

                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                      <code>QE_roots()</code>
                      <p>
                        Function to return the roots alpha and beta (A quadratic
                        equation only has 2 roots) of the quadratic equation. It
                        returns a Dictionary with keys alpha and beta as roots.
                        Please provide <b>a</b> (coefficint of x<sup>2</sup> ),
                        <b>b</b> (coefficient of x) and <b>c</b>(constant term)
                        as keyworded arguments.
                      </p>
                    </li>
                    <li class="list-group-item">
                      <code>isPerfectSquare()</code>
                      <p>
                        Function to verify if the given number is a perfect
                        square or not, returns Boolean
                      </p>
                    </li>
                    <li class="list-group-item">
                      <code>QE_typeOfRoots()</code>
                      <p>
                        Function to return the type of roots the quadratic
                        equation has. Please provide <b>a</b> (coefficint of
                        x<sup>2</sup> ), <b>b</b> (coefficient of x) and
                        <b>c</b>(constant term) as keyworded arguments.
                      </p>
                    </li>
                  </ul>

                  <h6>Statistics</h6>

                  <h6>Probability</h6>

