import random
import matplotlib.pyplot as plt
import pandas as pd


def quiz_range(hist):
    """Determine the advantage a student has for the success in the course
    :param hist: A students prior history with coding
    :return first_score: The lower bounded score for assignments based on a student's history
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


def quizzes(num_quiz, first_score):
    """Predict the grade for the students total quiz scores throughout the course
    :param num_quiz: Total number of quizzes in the course
    :param first_score: Given the history of the student, the first_score predicts a lower bound for quiz grades
    """
    num_quiz_range = num_quiz + 1
    quiz_list = []
    for quizzes in range(1, num_quiz_range):
        reading_adv = random.uniform(0, .2)
        quiz_raw = random.uniform(first_score, 100)
        quiz_1 = (quiz_raw * reading_adv) + quiz_raw
        if quiz_1 >= 100:
            quiz_grade = 100
        elif quiz_1 < 100:
            quiz_2 = random.uniform(quiz_1, 100)
            quiz_grade = (quiz_1 + quiz_2) / 2
        quiz_list.append(quiz_grade)
    final_quiz_grade = (sum(quiz_list)/num_quiz)/100
    return final_quiz_grade


def assignment_range(hist):
    """Determine the advantage a student has for the success in the course
        :param hist: A students prior history with coding
        :return lower_score: The lower bounded score for assignments based on a student's history
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
    for classes in range(num_classes):
        part = random.uniform(0, 10)
        part_total += part
    part_total = part_total/(num_classes * 10)
    return part_total


def choose_partner(hist):  # Create a function to choose a partner at random
    if hist == 'beginner':
        position = 1
    if hist == 'intermediate':
        position = 2
    if hist == 'advanced':
        position = 3
    if hist == 'expert':
        position = 4

    if position == 1:
        options = [1, 2]
    elif position == 2:
        options = [1, 2, 3]
    elif position == 3:
        options = [2, 3, 4]
    elif position == 4:
        options = [3, 4]

    partner_position = random.choice(options)

    # if partner is matching your skill level
    if partner_position - position == 0:
        percent_adj = 0.0
    # if partner is above your skill level
    elif partner_position - position == 1:
        percent_adj = .05
    # if partner is below your skill level
    elif partner_position - position == -1:
        percent_adj = -.05
    return percent_adj

# Create a function that randomly determines the outcome of choosing partners in 3 group assignments
def group_assign(hist, num_g_assign, lower_score):
    """Predict the grade for the student's grades on the group assignments
    :param num_g_assign: Total number of group assignments
    :param lower_score: Given the history of the student, the lower_score predicts a lower bound for quiz grades
    """
    percent_counter = 0
    total_points = 0

    for hw in range(num_g_assign):
        percent_counter += choose_partner(hist)
        raw_score = random.uniform(lower_score, 100)
        total_points += ((raw_score * percent_counter) + raw_score)
    total_points = (total_points/num_g_assign)/100

    return total_points


# Create a function that randomly determines the outcome of indiviudal assignments
def ind_assign(num_i_assign, lower_score):
    """Predict the grade for the student's individual assignments
    :param num_i_assign: Total number of individual assignments
    :param lower_score: Given the history of the student, the lower_score predicts a lower bound for quiz grades
    """
    # They should have an advantage if they have had prior experience
    num_assign = num_i_assign + 1
    ind_score = 0
    for hw in range(1, num_assign):
        hw_raw = random.uniform(lower_score, 100)
        ind_score = ind_score + hw_raw
    final_ind_grade = (ind_score / num_i_assign) / 100
    return final_ind_grade


def partner_generator(hist):
    """Determine the advantage or disadvantage a student has when randomly paired with other students
        :param hist: A students prior history with coding
        :return percent_adj: The percent adjustment based on partner skill
        """
    percent_adj = 0
    if hist == 'beginner':
        position = 1
    if hist == 'intermediate':
        position = 2
    if hist == 'advanced':
        position = 3
    if hist == 'expert':
        position = 4

    # get random skill level for partner
    partner_position = random.randint(1, 5)

    # if partner is matching your skill level
    if partner_position - position == 0 and position == 1:
        percent_adj += -.10
    if partner_position - position == 0 and position == 2:
        percent_adj += -.05
    if partner_position - position == 0 and position == 3:
        percent_adj += -.02
    if partner_position - position == 0 and position == 4:
        percent_adj += 0

    # if partner is above your skill level
    if partner_position - position == 1:
        percent_adj += .05
    if partner_position - position == 2:
        percent_adj += .10
    if partner_position - position == 3:
        percent_adj += .15

    # if partner is below your skill level
    if partner_position - position == -1:
        percent_adj += -.05
    if partner_position - position == -2:
        percent_adj += -.10
    if partner_position - position == -3:
        percent_adj += -.15
    return percent_adj


def random_partner(hist, lower_score):
    """Determine the advantage or disadvantage a student has when randomly paired with other students
        :param hist: A students prior history with coding
        :param lower_score: The lower bounded score for assignments based on a student's history
        :return total_points: The score on the assignment when randomly paired with partners
        """

    # generate the total number of partners in your group
    number_partners = random.randint(1, 3)

    percent_counter = 0
    for num in range(number_partners):
        percent_counter += partner_generator(hist)

    adjustment = percent_counter / number_partners
    raw_score = random.uniform(lower_score, 100)
    total_points = ((raw_score * adjustment) + raw_score) / 100

    return total_points


# Create a function that randomly determines the final project grade
def final_proj(hist, lower_score):
    """Predict the grade for the student's final project
    :param hist: A students prior history with coding
    :param lower_score: Given the history of the student, the lower_score predicts a lower bound for quiz grades
    :return final_proj_grade; Final project grade
    """
    odds = random.randint(1, 2)
    if odds == 1: # You have decided to choose a partner
        percent = choose_partner(hist)
        raw_score = random.uniform(lower_score, 100)
        final_proj_grade = ((raw_score * percent) + raw_score) / 100
    elif odds == 2: # You have decided to work alone
        raw_score = random.uniform(lower_score, 100)
        final_proj_grade = raw_score / 100
    return final_proj_grade


# Create a function that adds all the grades up into one for a final probability
def grade(part_points, quiz_points, ind_points, rand_group_points, group_points, final_points): # add parameters for the group/ind assignments and final
    """Use all of the following information and the weight of each grade to determine the final grade
        for the student in this course. Will they pass the course?
    :param part_points: The total participation points calculated
    :param quiz_points: The total quiz points calculated
    :param ind_points: The total individual assignment points
    """
    final_participation = part_points * .10
    final_quizzes = quiz_points * .15
    final_ind_assign = ind_points * .2763  # (10.53% per assignment (3) and 5.25% for the first ind assignment) * 75
    final_rand_points = rand_group_points * .078975
    final_group_points = group_points * .236925  # (10.53% per assignment (4) * 75
    final_assign = final_points * .1578  # (10.53% * 2 for the 2/1 weight per assignment) * 75

    total_points = final_participation + final_quizzes + final_ind_assign + final_rand_points + final_group_points + final_assign
    total_points = round(total_points * 100, 2)

    # if 100 <= total_points >= 93:
    #     print("As a/an {}, your final grade is an A, and you have passed the course.".format(hist))
    # elif 92.9 <= total_points >= 90:
    #     print("As a/an {}, your final grade is an A-, and you have passed the course.".format(hist))
    # elif 89.9 <= total_points >=87:
    #     print("As a/an {}, your final grade is a B+, and you have passed the course.".format(hist))
    # elif 86.9 <= total_points >= 83:
    #     print("As a/an {}, your final grade is a B, and you have passed the course.".format(hist))
    # elif 82.9 <= total_points >= 80:
    #     print("As a/an {}, your final grade is a B-, and you have passed the course.".format(hist))
    # elif 79.9 <= total_points >= 77:
    #     print("As a/an {}, your final grade is a C+, and you have passed the course.".format(hist))
    # elif 76.9 <= total_points >= 73:
    #     print("As a/an {}, your final grade is a C, and you have passed the course.".format(hist))
    # elif 72.9 <= total_points >= 70:
    #     print("As a/an {}, your final grade is a C-, and you have passed the course.".format(hist))
    # elif 69.9 <= total_points >= 65:
    #     print("As a/an {}, your final grade is a D, and you have NOT passed the course.".format(hist))
    # elif total_points <= 65:
    #     print("As a/an {}, your final grade is an F, and you have NOT passed the course.".format(hist))
    return total_points


def run_program(hist, grade_list):
    """Use this function to run all of the previous functions in the program.
    :param hist: A students prior history with coding
    :return stats: Statistics on each run that we are producing.
        # What is the student's final grade based on their history, do they pass the course?
    """
    first_score = int(quiz_range(hist))
    total_quiz = quizzes(8, first_score)
    total_part = participation(16)

    assign_range = assignment_range(hist)
    total_ind = ind_assign(4, assign_range)
    total_rand_group = random_partner(hist, assign_range)
    total_group = group_assign(hist, 3, assign_range)
    total_final = final_proj(hist, assign_range)

    grade_percent = float(grade(total_part, total_quiz, total_ind, total_rand_group, total_group, total_final))

    grade_list.append(grade_percent)
    return grade_list


def analyze_students(num_exp, num_adv, num_int, num_beg):
    """Run the program as many times as needed to get the desired results.
    :param num_exp: Total number of expert students
    :param num_adv: Total number of advanced students
    :param num_int: Total number of intermediate students
    :param num_beg: Total number of beginner students
    """
    grade_list = []

    for tests in range(num_exp):
        run_program('expert', grade_list)
    for tests in range(num_adv):
        run_program('advanced', grade_list)
    for tests in range(num_int):
        run_program('intermediate', grade_list)
    for tests in range(num_beg):
        run_program('beginner', grade_list)
    return grade_list


def dict(analyze_cat):
    analyze_dict = {}
    keys = range(100)
    for i in keys:
        analyze_dict[i] = analyze_cat[i]
    return analyze_dict


def graph(grade_dict):
    """Create a graph based on the number of times we analyze the students and their total grades.
    :param grade_dict: A dictionary filled with the grades and number of times the program is run.
    """
    dictionary = dict(grade_dict)
    lists = sorted(dictionary.items())
    x, y = zip(*lists)

    plt.plot(x, y)
    plt.show()


def dataframe(dictionary):
    df = pd.DataFrame.from_dict(dictionary, orient='index')
    return df


expert = analyze_students(100, 0, 0, 0)
advanced = analyze_students(0, 100, 0, 0)
intermediate = analyze_students(0, 0, 100, 0)
beginner = analyze_students(0, 0, 0, 100)

a = dict(expert)
b = dict(advanced)
c = dict(intermediate)
d = dict(beginner)

# exp_graph = graph(a)
# adv_graph = graph(b)
# int_graph = graph(c)
# beg_graph = graph(d)

exp_df = dataframe(a)
adv_df = dataframe(b)
int_df = dataframe(c)
beg_df = dataframe(d)

first_merge = pd.merge(exp_df, adv_df, left_index=True, right_index=True)
second_merge = pd.merge(first_merge, int_df, left_index=True, right_index=True)
last = pd.merge(second_merge, beg_df, left_index=True, right_index=True)
last.columns = ['expert', 'advanced', 'intermediate', 'beginner']
print(last.describe())

