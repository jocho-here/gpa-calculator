import csv, re
import config


def get_points(grade, credit_hour):
    grade = grade.lower()

    if 'w' in grade or 'ps' in grade:
        return 0
	
    base_point = config.grades[grade[0]]

    if grade[0] != 'f':
        base_point += config.diffs[grade[1]]
	
    # min(4.0, base_point) prevents a+ to be over 4.0
    return min(4.0, base_point) * credit_hour

def is_numeric(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

with open('true-gpa-meta.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    cum_points = 0
    cum_credit_hours = 0
    major_points = 0
    major_hours = 0
    total_credit_hours = 0
    pass_course = []

    for row in reader:
        if len(row) == 0:
            break
        if is_numeric(row[1]):
            department, course_num = row[0].split('-')
            credit_hour = int(row[1])
            final_grade = row[2]

            total_credit_hours += credit_hour

            if final_grade == 'ps':
                pass_course.append((row[0], row[1]))
            else:
                if department in config.major:
                    major_points += get_points(final_grade, credit_hour)
                    major_hours += credit_hour
                cum_points += get_points(final_grade, credit_hour)
                cum_credit_hours += credit_hour

    print('')
    print('')
    print('Earned: ', total_credit_hours)
    print('Needed: ', max(0, config.credit_to_grad - total_credit_hours))
    print('Pass: ', pass_course)
    print('GPA hours: ', cum_credit_hours)
    print('Cumulative GPA: ', cum_points/cum_credit_hours)
    print('Major GPA: ', major_points/major_hours)
    print('')
    print('')
