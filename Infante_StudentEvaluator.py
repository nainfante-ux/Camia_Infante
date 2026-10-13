
# [GLOBAL VARIABLE]
PROGRAM_TITLE = "STUDENT PERFORMANCE EVALUATION AND REPORT"


# [FUNCTION 1]
def display_header():
    # [LOCAL VARIABLE]
    header = PROGRAM_TITLE
    print('=' * 50)
    print(header)
    print('=' * 50)
    print("\nSTUDENT PERFORMANCE EVALUATOR")


# [FUNCTION 2]
def get_student_info():
    student_info = input("Enter student name: ")

    assessment_1 = int(input("Enter Assessment 1: "))
    while assessment_1 < 0 or assessment_1 > 100:
        assessment_1 = int(input("Please enter a value between 0 and 100: "))

    assessment_2 = int(input("Enter Assessment 2: "))
    while assessment_2 < 0 or assessment_2 > 100:
        assessment_2 = int(input("Please enter a value between 0 and 100: "))

    assessment_3 = int(input("Enter Assessment 3: "))
    while assessment_3 < 0 or assessment_3 > 100:
        assessment_3 = int(input("Please enter a value between 0 and 100: "))

    # Returns the student's information for use in other functions.
    return student_info, assessment_1, assessment_2, assessment_3


# [FUNCTION 3]
def evaluate_performance(assessment_1, assessment_2, assessment_3):
    # LOCAL VARIABLE: Stores the calculated average.
    average = (assessment_1 + assessment_2 + assessment_3) / 3
    return average


# [FUNCTION 4]
def display_report(student_info, assessment_1, assessment_2,
                   assessment_3, average):

    # [LOCAL VARIABLE]
    if average >= 90:
        performance_status = "Outstanding"
    elif average >= 85:
        performance_status = "Very Satisfactory"
    elif average >= 80:
        performance_status = "Satisfactory"
    elif average >= 75:
        performance_status = "Fairly Satisfactory"
    else:
        performance_status = "Needs Improvement"

    # [DISPLAY RESULTS]
    print("\nSTUDENT PERFORMANCE REPORT")
    print('=' * 50)
    print("Student Name:", student_info)
    print("Assessment Scores:", assessment_1, assessment_2, assessment_3)
    print(f"Average Score: {average:.2f}")
    print("Performance Level:", performance_status)
    print('=' * 50)


# [CALL FUNCTIONS AND DISPLAY]
display_header()

student_info, assessment_1, assessment_2, assessment_3 = get_student_info()

student_average = evaluate_performance(assessment_1, assessment_2, assessment_3)

display_report(student_info, assessment_1, assessment_2,assessment_3, student_average)