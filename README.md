# Python-Internals
This repository is part of an assignment for Software Design with Python [SDwP] course, in which we will try to exhaust all the characteristics of python.and it consists of five main tasks and they all in functions in the **main.py** file. 
_________________________________________________________________
*to run this program you just need to download the **.zip** file on your machine and extract it on your desktop. then make sure the path in your terminal is correct **~/Desktop/s.issa** then you can use the key words: task1, print, compile and compare as it follows. 
**p.s. all the results of the following examples are in the OUTPUT folder while the new ones will be in the the same folder (s.issa)** 

## Python version: 
Python 3 or greater(we used Python 3.8.10)
## Used Modules:
* chdir
*  sys
*  timeit
*  dis
*  subprocess
*  marshal
*  py_compile
*  numpy 
*  pandas
*  NamedTemporaryFile
*  defaultdict
*  exists

___________________________________________________________
# Task 1
In this task we are copmaring between  N arbitrary .py files and create a neat table out of their execution time starting with the fastest, and in order to test this task you should open the **main.py** file and run the following command in the trminal:

**$ python3 main.py task1 src1.py src2.py src3.py**

and you can check the results of the first task in the file **task1_output.txt**, and you can test your own  programs executions time and compare between them just make sure they are in the same directory.

______________________________________________________________
# Task 2
for this task we deined a functionun that yield opcodes (and their arguments) for ordinary python programs. In order to use this function you need to copy the following command in your terminal, remove our **.py** file(s) and place it with yours:

**$ python3 main.py print -py src1.py**
 
and you can check the results of the second task in the file **task2_output.txt**
________________________________________________________________
# Task 3
In this task we extended th second task and now we are able to get the bytecode out of the source code or a string. In order to use this function you need to copy the following command in your terminal and place our file(s) with yours:

**$ python3 main.py print -pyc  src1.pyc** (for source code)
**$ python3 main.py print -s "print('Hello world')"** (for string)

you can check the results of getting the bytecode from the source code in the file **task3_output_byc.txt**, and for the string in **task3_output_s.txt**
__________________________________________________________
# Task 4
In this task we  Extended our program to produce (compile) .py files or code snippets right into .pyc

**$ python3 main.py compile -py  src1.pyc** (for source code)
**$ python3 main.py compile -s "print('Hello world')"** (for string)

p.c the source code of the string will be stored in a file called **task4_output_s.pyc**, which will be saved in the same directory.
__________________________________________
# Task 5
For this task we introduced a new action compare. It compares bytecode among different sources and produces neat table with stats of the used opcodes (and only them). you can use this function by the following command:

**$ python3 main.py compare -py src1.py -py src2.py -py src3.py**

you can see the results in the file **task5_output_byc.txt**



