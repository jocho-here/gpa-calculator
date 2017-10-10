# GPA Calculator
Calculates your GPA

# gpa-meta.csv
This is where you want to put down the information about your grades.  
Some rules:
- AP credits that you earned for your college go right below ap,ap,ap
- Grades for each semester should come after semester indicator line (e.g. fall-2016,fall-2016,fall-2016)
- To add anything for reference but not for calculation, put a new line and add lines after the new line
	- Take a look at the example gpa-meta.csv
- It goes as `course_department-course_number,course_credit_hours,letter_grade_earned`
	- `cs-125,3,b0`
- Grade formating
	- b+: B Plus
	- b0: Regular B
	- b-: B Minus
	- *There is neither adding 0.33 for A+ and F+, nor subtracting 0.33 for F-*

# Grading Scale
- Currently, grading scale is adopted to UIUC grading scales.  If you want to adjust this, please edit the top two lines of `gpa-calculator.py` file
- UIUC grading scale
	- A: 4; B: 3; C: 2; D: 1; F: 0
	- Every + and - signs indicate difference of `1/3`
	- Extras
		- ps: Pass
		- w: Withdraw
		- whatever_youwant_just_add: For your reference

# How-to
- Edit `gpa-meta.csv` accordingly
- Run `python gpa-calculator.py`

# Example Output
```
Total credit hours earned: 30
Pass courses: [('chem-102', '3'), ('math-231', '4')]
Credit hours count towards GPA: 23
Cumulative GPA: 4.0
```
