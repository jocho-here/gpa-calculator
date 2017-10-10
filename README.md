# GPA Calculator
Calculates your GPA

## gpa-meta.csv
This is where you want to put down the information about your grades.  
Some rules:
- AP credits that you earned for your college go right below `ap,ap,ap`
- Grades for each semester should come after semester indicator line (e.g. `fall-2016,fall-2016,fall-2016`)
- To add anything for reference but not for calculation, put a new line and add lines after the new line
	- Take a look at the example gpa-meta.csv
- It goes as `course_department-course_number,course_credit_hours,letter_grade_earned`
	- `cs-125,3,b0`
- Grade formating
	- b+: B Plus
	- b0: Regular B
	- b-: B Minus
	- *There is neither adding 0.33 for A+ and F+, nor subtracting 0.33 for F-*
- Example `gpa-meta.csv`
```
course,hours,letter-grade
ap,ap,ap
chem-102,3,ps
math-231,4,ps
fall-2016,fall-2016,first-2016
cs-101,4,a0
gs-101,1,a0
math-241,3,a0
phys-211,4,a0
rhet-105,4,a0
spring-2017,spring-2017,spring-2017
cs-173,3,a+
math-415,0,a+
phys-212,4,a+
phys-213,0,a+

fall-2017,fall-2017,fall-2017
stat-400,4,b0
cs-357,3,a0
cs-440,3,a0
info-490,3,a0
winter-2017-18,winter-2017-18,winter-2017-18
mus-130,3,a0
spring-2018,spring-2018,spring-2018
cs-374,4,a0
cs-412,3,a0
cs-421,3,a0
info-490,3,a0
```
## Grading Scale
- Current grading scale is from UIUC grading scales.  If you want to adjust this, please edit the top two lines of `gpa-calculator.py`
```
# These lines
grades = {'a':4.00,'b':3.00,'c':2.00,'d':1.00,'f':0.00}
diffs = {'+':0.33, '-':-0.33, '0':0.00}
```
- Extras
	- ps: Pass
	- w: Withdraw
	- whatever_youwant_just_add: For your reference

## How-to
- Edit `gpa-meta.csv` accordingly
- Run `python gpa-calculator.py`

## Example Output
```
Total credit hours earned: 30
Pass courses: [('chem-102', '3'), ('math-231', '4')]
Credit hours count towards GPA: 23
Cumulative GPA: 4.0
```
