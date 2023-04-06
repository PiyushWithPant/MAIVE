<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <meta
      name="description"
      content="MAIVE - Mathematics for Artificial Intelligence with Visualization Extended, is an open-source Python Package developed by Mr. Piyush Pant to contribute in the domain of Artificial Intelligence."
    />
    <meta
      name="keywords"
      content="MAIVE, Maths, AI, Machine Learning, Piyush Pant, Probability, Statistics, Algebra"
    />
    <meta name="author" content="Piyush Pant" />

    <link rel="icon" type="image/x-icon" href="favicon.ico" />

    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous"
    />

    <title>Maive - Documentation</title>

    <style></style>

    <link rel="stylesheet" href="./index.css" />
  </head>
  <body>
    <nav
      style="background-color: #ed1703 !important"
      class="navbar navbar-expand-lg bg-body-tertiary"
    >
      <div class="container-fluid">
        <img
          src="./assets/pictures/MAIVE LOGO.png"
          class="img-fluid w-25"
          alt="MAIVE logo"
        />

        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <p class="logoBanner">
                <b>M</b>athematics for <b>A</b>rtificial <b>I</b>ntelligence
                with <b>V</b>isualization <b>E</b>xtended
              </p>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="noti">
      <marquee direction="left" style="color: white">
        Developed by Piyush Pant with
        ❤️&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;From INDIA
        <img
          class="indianFlag"
          src="./assets/pictures/indianFlag.png"
          alt="Indian flag"
        />
        2023&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Last
        Update: April 2023 (The package and documentation is under development:
        Expected full release June 2023)
      </marquee>
    </div>

    <div class="container mb-5 py-3">
      <div class="gettingStarted px-3">
        <h1>Get started with MAIVE</h1>
        <p class="">
          MAIVE (मैव) is a powerful python package equipped with advanced
          mathematics to assist you in the domain of Artificial Intelligence
          while also providing you with visualization support. The mathematics
          level begins from high school to advanced, any topic that may be
          required in the AI domain is provided in the MAIVE. Please understand
          that the package is still under development, so there might be missing
          topics (which will be added soon). To become a contributor or if you
          want to suggest something, please contact us via
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

      <div class="main">
        <div class="installation py-3 px-3">
          <h3># Installation</h3>

          <p class="code my-3">
            $ pip install maive
            <button class="btn btn-default copyButton" onclick="copyText()">
              Copy
            </button>
          </p>

          <p>
            Copy the above code, paste it in your terminal and you are good to
            go!
          </p>
        </div>

        <div class="documentation px-3">
          <h3>Documentation</h3>
          <p>
            Please visit the section as per your requirements. It is advised to
            read the <b> HOW TO USE? </b> section before using the package.
          </p>

          <div class="accordion" id="accordionExample">
            <div class="accordion-item">
              <h2 class="accordion-header" id="headingOne">
                <button
                  class="accordion-button"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseOne"
                  aria-expanded="true"
                  aria-controls="collapseOne"
                >
                  <h6>HOW TO USE?</h6>
                </button>
              </h2>
              <div
                id="collapseOne"
                class="accordion-collapse collapse show"
                aria-labelledby="headingOne"
                data-bs-parent="#accordionExample"
              >
                <div class="accordion-body">
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

            <div class="accordion-item">
              <h2 class="accordion-header" id="headingTwo">
                <button
                  class="accordion-button collapsed"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseTwo"
                  aria-expanded="false"
                  aria-controls="collapseTwo"
                >
                  <h6>Arithmatic Progression</h6>
                </button>
              </h2>
              <div
                id="collapseTwo"
                class="accordion-collapse collapse"
                aria-labelledby="headingTwo"
                data-bs-parent="#accordionExample"
              >
                <div class="accordion-body">
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
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header" id="headingThree">
                <button
                  class="accordion-button collapsed"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseThree"
                  aria-expanded="false"
                  aria-controls="collapseThree"
                >
                  <h6>Quadratic Equations</h6>
                </button>
              </h2>
              <div
                id="collapseThree"
                class="accordion-collapse collapse"
                aria-labelledby="headingThree"
                data-bs-parent="#accordionExample"
              >
                <div class="accordion-body">
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
                </div>
              </div>
            </div>

            <div class="accordion-item">
              <h2 class="accordion-header" id="headingFour">
                <button
                  class="accordion-button collapsed"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseFour"
                  aria-expanded="false"
                  aria-controls="collapseFour"
                >
                  <h6>Statistics</h6>
                </button>
              </h2>
              <div
                id="collapseFour"
                class="accordion-collapse collapse"
                aria-labelledby="headingFour"
                data-bs-parent="#accordionExample"
              >
                <div class="accordion-body">ap</div>
              </div>
            </div>

            <div class="accordion-item">
              <h2 class="accordion-header" id="headingFive">
                <button
                  class="accordion-button collapsed"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseFive"
                  aria-expanded="false"
                  aria-controls="collapseFive"
                >
                  <h6>Probability</h6>
                </button>
              </h2>
              <div
                id="collapseFive"
                class="accordion-collapse collapse"
                aria-labelledby="headingFive"
                data-bs-parent="#accordionExample"
              >
                <div class="accordion-body">ap</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Required Functions -->
    <script>
      function copyText() {
        navigator.clipboard.writeText("pip install maive");
      }
    </script>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous"
    ></script>

    <!-- <script
      src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
      integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"
      integrity="sha384-mQ93GR66B00ZXjt0YO5KlohRA5SY2XofN4zfuZxLkoj1gXtW8ANNCe9d5Y3eG5eD"
      crossorigin="anonymous"
    ></script> -->
  </body>
</html>
