import random


def student_exp():
    """Determine the advantage a student has for the success in the course
    :param  :
    :return :
    """
    name = input("Please enter your name: ")
    hist = input("Describe your level of experience with Python (beginner, intermediate, advanced, expert): ")
    if hist == 'beginner':
        first_score = random.randint(1, 100)
    if hist == 'intermediate':
        first_score = random.randint(25, 100)
    if hist == 'advanced':
        first_score = random.randint(50, 100)
    if hist == 'expert':
        first_score = random.randint(75, 100)
    return first_score

def quizzes(num_quiz, hist):
    """Predict the grade for the students total quiz scores throughout the course
    :param num_quiz: Total number of quizzes in the course
    """
    num_quiz = num_quiz + 1
    quiz_list = []
    print(hist)
    for quizzes in range(1, num_quiz):
        quiz_1 = random.randint(1, 100)
        if quiz_1 == 100:
            quiz_grade = quiz_1
        if quiz_1 <= 50:
            quiz_2 = random.randint(50, 100)
            quiz_grade = (quiz_1 + quiz_2) / 2
        if quiz_1 >= 50:
            quiz_2 = random.randint(51, 100)
            quiz_grade = (quiz_1 + quiz_2) / 2
        quiz_list.append(quiz_grade)
    print(sum(quiz_list))
    final_quiz_grade = sum(quiz_list) * .15
    # We could try to see if the participation factors into this?
    # So far, there are a total of 8 quizzes
    return final_quiz_grade

print(student_exp())

quizzes(8)

# Create a function that reads in a students prior experience with coding
# def student_exp():
#     """Determine the advantage a student has for the success in the course
#     :param  :
#     :return :
#     """
#     name = input("Please enter your name: ")
#     hist = input("Describe your level of experience with Python (beginner, intermediate, advanced, expert): ")
#     if hist == 'beginner':
#         first_score = random.randint(1, 100)
#     if hist == 'intermediate':
#         first_score = random.randint(25, 100)
#     if hist == 'advanced':
#         first_score = random.randint(50, 100)
#     if hist == 'expert':
#         first_score = random.randint(75, 100)
#     return first_score
#
# print(student_exp())

