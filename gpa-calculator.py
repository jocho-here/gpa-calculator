import csv
import re

grades = {'a':4.00,'b':3.00,'c':2.00,'d':1.00,'f':0.00}
diffs = {'+':0.33, '-':-0.33, '0':0.00}
tech = {'cs', 'math', 'stat'}
credit_to_grad = 128
grade_diff = float(1)/3 # float() has been added just in case anyone is trying to use it in Python 2

def get_points(grade, credit_hour):
	grade = grade.lower()
	points = 0
	diff = 0

	if 'w' in grade or 'ps' in grade:
		return 0
	
	base_point = grades[grade[0]]

	if grade[0] != 'f':
		diff = diffs[grade[1]]
	
	if grade != 'a+' and 'f' not in grade:
		base_point += diff
	
	return base_point * credit_hour

def is_numeric(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

with open('gpa-meta.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	cum_points = 0
	cum_credit_hours = 0
	tech_points = 0
	tech_hours = 0
	total_credit_hours = 0
	pass_course = []

	for row in reader:
		if len(row) == 0:
			break
		if is_numeric(row[1]):
			credit_hour = int(row[1])
			total_credit_hours += credit_hour

			if row[2] == 'ps':
				pass_course.append((row[0], row[1]))
			else:
				if row[0].split('-')[0] in tech:
					tech_points += get_points(row[2], credit_hour)
					tech_hours += credit_hour
				cum_points += get_points(row[2], credit_hour)
				cum_credit_hours += credit_hour
	
	print('')
	print('')
	print('Earned: ', total_credit_hours)
	print('Needed: ', max(0,credit_to_grad - total_credit_hours))
	print('Pass: ', pass_course)
	print('GPA hours: ', cum_credit_hours)
	print('Cumulative GPA: ', cum_points/cum_credit_hours)
	print('Technical GPA: ', tech_points/tech_hours)
	print('')
	print('')
