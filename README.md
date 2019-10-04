# Introduction
This repository contains the following:
  * This ReadMe file
  * Collatz.py which is the original plain single integer Collatz Conjecture test
  * Collatz_Range.py which tests each integer from 2 up, in sequence to return:
    * The integer tested
    * The number of iterations it took to test
    * The time it took to test

# What is the Collatz Conjecture?
The Collatz Conjecture implies that for each positive integer n, given the following binary calculation, the resultant integer will always be 1 with the calculations as follows:

If n is even then divide by 2

If n is odd then multiply by 3 and then add 1

Currently this Conjecture has not been proven for all positive integers.

## Instructions
Running the code in this repository requires that you have Visual Studio Code (or other Python code writing software) installed on your machine. This software is available from [here](https://code.vidsualstudio.com/download).

In addition, a Command Line Interface (CLI) tool such as CMDer is necessary to call the program code. This software can be located [here](https://cmder.net).

To run this software, download the python code into a folder on your machine noting the path where you've saved this code.

Open your CLI and navigate to the path where you've saved the code then type 'python filename' where filname is the name of the python code file (e.g. collatz.py)

## Sample outputs
### collatz.py

On my machine, the Collatz program is saved as follows: 
![Directory Screen Grab](https://github.com/Seamie-irl/Collatz/tree/master/images/1.jpg "Screen shot of directory")

Entering the command
``` 
python collatz.py 
``` 
in your CLI and hitting *Enter* will return the following:

![Run program](https://github.com/Seamie_irl/Collatz/tree/master/images/3.jpg "Screen grab on run")

From here you must enter a positive integer (i.e. a whole number greater than or equal to 1).

If you don't enter a whole number you'll get the following response:

![Not a whole number error response](https://github.com/Seamie_irl/Collatz/tree/master/images/4.jpg "Whole number error")

If you enter a negative integer you'll get the following response:

![Negative Integer error response](https://github.com/Seamie_irl/Collatz/tree/master/images/5.JPG "Negative Integer Error")

Otherwise, if you enter a positive integer such as 107, for example, you'll receive the following output:

![Result](https://github.com/Seamie_irl/Collatz/tree/master/images/6.PNG "Result")



