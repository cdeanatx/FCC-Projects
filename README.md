# FCC-Projects
This is a repository for freeCodeCamp projects. The individual README.md files within the folders outline the scope and goals of each project in more detail.

## Contents
Below is a list of each project contained within this repository.

### Arithmetic Formatter
Takes a list of "math" strings as input and outputs the equations in vertical format.
Input:
`arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])`
Output:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

### Budget App
An app that helps the user with their budget. Example Output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

### Polygon Area Calculator
Uses object oriented programming to create a Rectangle class and a Square class. The Square class is a subclass of Rectangle and inherits methods and attributes.

### Probability Calculator
Program to determine the approximate probability of drawing a certain number of balls randomly from a "hat."

### Time Calculator
Program to determine the new time based on current time and time elapsed. Takes weekday as an optional argument. Example inputs/outputs:
```
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

### Mean, Variance, Standard Deviation Calculator

Function that accepts a list as input and converts it to a 3 x 3 matrix. It then calculates statistics along both axes and for the flattened matrix and returns a dictionary. For example, an input of `[0,1,2,3,4,5,6,7,8]` would return:

```
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

### Demographic Data Analyzer

Program that reads a CSV containing 1994 Global Census data into Pandas to answer various questions, such as:

```
* How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. 
* What is the average age of men?
* What is the percentage of people who have a Bachelor's degree?
* What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
* What percentage of people without advanced education make more than 50K?
* What is the minimum number of hours a person works per week?
* What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
* What country has the highest percentage of people that earn >50K and what is that percentage?
* Identify the most popular occupation for those who earn >50K in India. 
```

### Medical Data Visualizer

Program that takes a CSV of medical data and performs calculations and creates visualizations
