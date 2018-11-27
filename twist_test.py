import random

name = input("Please enter your name: ")
hist = input("Describe your level of experience with Python (beginner, intermediate, advanced, expert): ")

def quiz_range(hist):
    """Determine the advantage a student has for the success in the course
    :param  :
    :return :
    """
    if hist == 'beginner':
        first_score = 0
    if hist == 'intermediate':
        first_score = 30
    if hist == 'advanced':
        first_score = 60
    if hist == 'expert':
        first_score = 80
    return first_score

first_score = int(quiz_range(hist))
print(first_score)

def quizzes(num_quiz, first_score):
    """Predict the grade for the students total quiz scores throughout the course
    :param num_quiz: Total number of quizzes in the course
    """
    num_quiz = num_quiz + 1
    quiz_list = []
    for quizzes in range(1, num_quiz):
        reading_adv = random.uniform(0, .2)
        quiz_raw = random.uniform(first_score, 100)
        quiz_1 = (quiz_raw * reading_adv) + quiz_raw
        if quiz_1 >= 100:
            quiz_grade = 100
        elif quiz_1 < 100:
            quiz_2 = random.uniform(quiz_1, 100)
            quiz_grade = (quiz_1 + quiz_2) / 2
        quiz_list.append(quiz_grade)
    final_quiz_grade = (sum(quiz_list)/8)/100
    # We could try to see if the participation factors into this?
    # So far, there are a total of 8 quizzes
    return final_quiz_grade

print(quizzes(8, first_score))

def assignment_range(hist):
    """Determine the advantage a student has for the success in the course
        :param  :
        :return :
        """
    if hist == 'beginner':
        lower_score = 40
    if hist == 'intermediate':
        lower_score = 60
    if hist == 'advanced':
        lower_score = 75
    if hist == 'expert':
        lower_score = 85
    return lower_score

def participation(num_classes):
    """Predict the grade for the students total participation in class
    :param num_classes: Total number of classes to participate in
    """
    part_total = 0
    total_classes = num_classes + 1
    for c in range(0, total_classes):
        part = random.uniform(0, 10)
        part_total += part
    part_total = part_total/(num_classes * 10)
    return part_total

print(participation(16))
