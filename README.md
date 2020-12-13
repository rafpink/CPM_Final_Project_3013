# CPM_Final_Project_3013
*Critical Path Method for a Construction Project*
*This program was constructed as a final project for CE-UY 3013*

This repository uses python to determine the critical path method (CPM) within a construction project. To make it easier for the person using the program, a .CSV file would be used to identify the task, the predecessors following that task, and the duration of that task. The late start, late finish, early start, early finish, and float would be determined by the program. The program would also determine whether or not the task would be part of the critical path.

The difference between this code and the PYPI criticalpath library is that this code is a lot cleaner. All values are inputted on a different document and shown as a Table using Pandas. The criticalpath library requires you to input all your activities, durations, and predecessor node links right on python, which could be confusing for the average person and the user could potentially get lost in the code.

You need to assume that the project will finish on time and there will be one defined critical path. There may be more than one but the function will only output the first one it sees.

Inputs:
* Activities
* Predecessors
* Duration
* File Name

Outputs:
* Early Start
* Early Finish
* Late Start
* Late Finish
* Float
* If activity is part of the critical path
* Critical Path


## Setup

You will need to download this repository before using this program. It is recommended that you crease a virtual environment for the program using the following code in your command prompt:

```
python3 -m venv venv
```

You then activate the virtual environment by:

```
For Linux/MacOS:
$ source venv/bin/activate

For Windows OS:
> venv\Scripts\activate
```

Finally, you install all the packages and libraries necessary for this program typing:

```
pip install -r requirements.txt
```

You are then ready to execute the code but typing the file name after navigating to the correct directory. For example, if the file is on your desktop in a folder called CPM, you type:

```
cd Desktop\CPM
```

## How to use the program

In order to use the program, you will need to input the activities, predecessors, and duration of each activity on a .CSV file. You will be prompted to input your file name of the .CSV you will be using as soon as you fun the test file. The file name we will use for the demo is called criticalpath_file.csv, which is located in the "Input" folder. If you happen to enter an incorrect file name, the program will then prompt you to input the correct name.

Output:
```
Please input the file name.
(Don't forgot to input the file extension. For example, .CSV or .XLSX)
```

Input:
```
criticalpath_file.csv
```

## Create a .CSV

We are trying to replicate the critical path as shown in the image below. The goal is to replace spreadsheets altogether.

![Capture](https://user-images.githubusercontent.com/58703409/101407702-46008600-38a9-11eb-810e-b4105ea48882.PNG)

There are a total of 10 tasks/nodes with a duration of 23 days for all 10 tasks to be completed.

You start with a simple .CSV file and import that into your code. CSV stands for Comma Separated Text. You could construct one with a basic text editor if need be. Your input for this sample problem in raw form should look like this:

```
ACTIVITY PREDECESSORS  DURATION  
       A,           ,         3
       B,          A,         3
       C,          A,         5
       D,          A,         4
       E,  "B, C, D",         7
       F,     "C, D",         4
       G,          D,         6
       H,     "E, F",         2
       I,     "F, G",         3
       J,     "H, I",         6
```

Your output should eventually look like:

```
  ACTIVITY PREDECESSORS  DURATION  ES  EF  LS  LF  FLOAT IS_CRITICAL?
0        A          NaN         3   0   3   0   3      0            Y
1        B            A         3   3   6   5   8      2            N
2        C            A         5   3   8   3   8      0            Y
3        D            A         4   3   7   4   8      1            N
4        E      B, C, D         7   8  15   8  15      0            Y
5        F         C, D         4   8  12  10  14      2            N
6        G            D         6   7  13   8  14      1            N
7        H         E, F         2  15  17  15  17      0            Y
8        I         F, G         3  13  16  14  17      1            N
9        J         H, I         6  17  23  17  23      0            Y

Critical Path: A --> C --> E --> H --> J
```

The outputs will vary depending on the inputs. The values that should be updated should the ES, EF, LS, FLOAT, and IS_CRITICAL? columns. The critical path should be displayed below was well.
