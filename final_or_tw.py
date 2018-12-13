import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def mod_pert_random(low, likely, high, confidence=4, samples=1):
    """Produce random numbers according to the 'Modified PERT'
        distribution.
        :param low: The lowest value expected as possible.
        :param likely: The 'most likely' value, statistically, the mode.
        :param high: The highest value expected as possible.
        :param confidence: This is typically called 'lambda' in literature
                            about the Modified PERT distribution. The value
                            4 here matches the standard PERT curve. Higher
                            values indicate higher confidence in the mode.
                            Currently allows values 1-18
        Formulas from "Modified Pert Simulation" by Paulo Buchsbaum.
        """
    # Check minimum & maximum confidence levels to allow:
    if confidence < 1 or confidence > 18:
        raise ValueError('confidence value must be in range 1-18.')

    mean = (low + confidence * likely + high) / (confidence + 2)

    a = (mean - low) / (high - low) * (confidence + 2)
    b = ((confidence + 1) * high - low - confidence * likely) / (high - low)

    beta = np.random.beta(a, b, samples)
    beta = beta * (high - low) + low
    return float(beta)


def likely_range(hist):
    """Determine the advantage a student has for the success in the course
    :param hist: A students prior history with coding
    :return first_score: The lower bounded score for assignments based on a student's history
    """
    if hist == 'beginner':
        likely = 80
    if hist == 'intermediate':
        likely = 85
    if hist == 'advanced':
        likely = 90
    if hist == 'expert':
        likely = 95
    return likely


def quiz_range(hist, effort):
    """Determine the advantage a student has for the success in the course
    :param hist: A students prior history with coding
    :return first_score: The lower bounded score for assignments based on a student's history
    """
    if hist == 'beginner':
        if effort == 0:
            first_score = 30
        elif effort == 1:
            first_score = 50
        elif effort == 2:
            first_score = 70
    if hist == 'intermediate':
        if effort == 0:
            first_score = 55
        elif effort == 1:
            first_score = 65
        elif effort == 2:
            first_score = 75
    if hist == 'advanced':
        if effort == 0:
            first_score = 70
        elif effort == 1:
            first_score = 80
        elif effort == 2:
            first_score = 90
    if hist == 'expert':
        if effort == 0:
            first_score = 85
        elif effort == 1:
            first_score = 90
        elif effort == 2:
            first_score = 95
    return first_score


def assignment_range(hist, effort):
    """Determine the advantage a student has for the success in the course
        :param hist: A students prior history with coding
        :return lower_score: The lower bounded score for assignments based on a student's history
        """
    if hist == 'beginner':
        if effort == 0:
            lower_score = 60
        elif effort == 1:
            lower_score = 70
        elif effort == 2:
            lower_score = 80
    if hist == 'intermediate':
        if effort == 0:
            lower_score = 65
        elif effort == 1:
            lower_score = 75
        elif effort == 2:
            lower_score = 85
    if hist == 'advanced':
        if effort == 0:
            lower_score = 70
        elif effort == 1:
            lower_score = 80
        elif effort == 2:
            lower_score = 90
    if hist == 'expert':
        if effort == 0:
            lower_score = 75
        elif effort == 1:
            lower_score = 85
        elif effort == 2:
            lower_score = 95
    return lower_score


def quizzes(num_quiz, first_score, likely):
    """Predict the grade for the students total quiz scores throughout the course
    :param num_quiz: Total number of quizzes in the course
    :param first_score: Given the history of the student, the first_score predicts a lower bound for quiz grades
    :param likely: The likely variable for our PERT distribution calculation
    :return final_quiz_grade: Returns the final quiz grade total as a decimal
    """
    quiz_list = []
    for quizzes in range(num_quiz):
        complete_quiz = random.randint(0, 10)
        reading_adv = random.uniform(.2, .5)
        if complete_quiz == 0:
            quiz_list.append(0)
        elif complete_quiz > 0:
            quiz_raw = mod_pert_random(first_score, likely, 100, 4, 1)
            quiz_1 = (quiz_raw * reading_adv) + quiz_raw
            if quiz_1 >= 100:
                quiz_grade = 100
            elif quiz_1 < 100:
                quiz_2 = random.uniform(quiz_1, 100)
                quiz_grade = (quiz_1 + quiz_2) / 2
            quiz_list.append(quiz_grade)
    final_quiz_grade = (sum(quiz_list)/num_quiz)/100
    return final_quiz_grade


def participation(num_classes):
    """Predict the grade for the students total participation in class
    :param num_classes: Total number of classes to participate in
    :return total_part_grade: Returns the final participation grade as a decimal
    """
    part_total = []
    for classes in range(num_classes):
        attendance = random.randint(0, 10)
        if attendance == 0:
            part_total.append(attendance)
        else:
            points = 10
            part = random.uniform(0, 5)  # I'm thinking this should stay the same, otherwise we could have a PERT with a low likely value
            points = points + part
            part_total.append(points)
    total_part_grade = sum(part_total)/(num_classes * 15)
    return total_part_grade


def participation_boost(grade):
    """Predict the grade for the students total participation in class
    :param grade: Current total of all assignments, before participation boost
    :return total_with_part: Returns the total, including the participation boost
    """
    participation_effort = random.randint(0, 2)
    if participation_effort == 0:
        total_with_part = grade
    if participation_effort == 1:
        diff = 100 - grade
        if 0 < diff <= 7:  # if at 93-100
            total_with_part = grade
        elif 7 < diff <= 10:  # if at 90-92.9
            total_with_part = 93
        elif 10 < diff <= 13:  # if at 87-89.9
            total_with_part = 90
        elif 13 < diff <= 17:  # if at 80-82.9
            total_with_part = 87
        elif 17 < diff <= 20:  # if at 77-79.9
            total_with_part = 84
        elif 20 < diff <= 23:  # if at 73-76.9
            total_with_part = 80
        elif 23 < diff <= 27:  # if at 70-72.9
            total_with_part = 77
        elif 27 < diff <= 30:  # if at 65-69.9
            total_with_part = 73
        elif 30 < diff <= 35:  # if at 60-64.9
            total_with_part = 70
    if participation_effort == 2:
        diff = 100 - grade
        if 0 < diff <= 7:  # if at 90-92.9
            total_with_part = grade
        elif 7 < diff <= 10:  # if at 87-89.9
            total_with_part = 93
        elif 10 < diff <= 13:  # if at 83-86.9
            total_with_part = 90
        elif 13 < diff <= 17:  # if at 80-82.9
            total_with_part = 87
        elif 17 < diff <= 20:  # if at 77-79.9
            total_with_part = 83
        elif 20 < diff <= 23:  # if at 73-76.9
            total_with_part = 80
        elif 23 < diff <= 27:  # if at 70-72.9
            total_with_part = 77
        elif 27 < diff <= 30:  # if at 65-69.9
            total_with_part = 73
        elif 33 < diff <= 35:  # if at 60-64.9
            total_with_part = 70
    return total_with_part


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


def group_assign(hist, num_g_assign, lower_score, likely):
    """Predict the grade for the student's assessment on the group assignments
    :param num_g_assign: Total number of group assignments
    :param lower_score: Given the history of the student, the lower_score predicts a lower bound for quiz grades
    :param likely: The likely variable for our PERT distribution calculation
    :return final_group_grade: Returns the final group assignments grade as a decimal
    """
    percent_counter = 0
    total_points = 0
    for hw in range(num_g_assign):
        percent_counter += choose_partner(hist)
        raw_score = mod_pert_random(lower_score, likely, 100, 4, 1)
        total_points += ((raw_score * percent_counter) + raw_score)
    final_group_grade = (total_points/num_g_assign)/100
    return final_group_grade


def ind_assign(num_i_assign, lower_score, likely):
    """Predict the grade for the student's individual assignments
    :param num_i_assign: Total number of individual assignments
    :param lower_score: Given the history of the student, the lower_score predicts a lower bound for quiz grades
    :param likely: The likely variable for our PERT distribution calculation
    :return final_ind_grade: Return the final individual assignments grade as a decimal
    """
    # They should have an advantage if they have had prior experience
    num_assign = num_i_assign + 1
    ind_score = 0
    for hw in range(1, num_assign):
        hw_raw = mod_pert_random(lower_score, likely, 100, 4, 1)
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


def random_partner(hist, lower_score, likely):
    """Determine the advantage or disadvantage a student has when randomly paired with other students
        :param hist: A students prior history with coding
        :param lower_score: The lower bounded score for assignments based on a student's history
        :param likely: The likely variable for our PERT distribution calculation
        :return final_rand_part_grade: Returns the final grade for the randomly assigned partner group project in decimal
        """
    # generate the total number of partners in your group
    number_partners = random.randint(1, 3)
    percent_counter = 0
    for num in range(number_partners):
        percent_counter += partner_generator(hist)
    adjustment = percent_counter / number_partners
    raw_score = mod_pert_random(lower_score, likely, 100, 4, 1)
    final_rand_part_grade = ((raw_score * adjustment) + raw_score) / 100
    return final_rand_part_grade


# Create a function that randomly determines the final project grade
def final_proj(hist, lower_score, likely):
    """Predict the grade for the student's final project
    :param hist: A students prior history with coding
    :param lower_score: Given the history of the student, the lower_score predicts a lower bound for quiz grades
    :param likely: The likely variable for our PERT distribution calculation
    :return final_proj_grade: Returns the final project grade in a decimal
    """
    odds = random.randint(1, 2)
    if odds == 1:  # You have decided to choose a partner
        percent = choose_partner(hist)
        raw_score = mod_pert_random(lower_score, likely, 100, 4, 1)
        final_proj_grade = ((raw_score * percent) + raw_score) / 100
        if final_proj_grade > 100:
            final_proj_grade = 100
    elif odds == 2:  # You have decided to work alone
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
    :param rand_group_points: The total points from random group assignment
    :param group_points: The total points from chosen group assignments
    :param final_points: The total points from the final assignment
    :return total_points: The total points for the entire course out of 100
    """
    final_participation = part_points * .10
    final_quizzes = quiz_points * .15
    final_ind_assign = ind_points * .2763  # (10.53% per assignment (3) and 5.25% for the first ind assignment) * 75
    final_rand_points = rand_group_points * .078975
    final_group_points = group_points * .236925  # (10.53% per assignment (4) * 75
    final_assign = final_points * .1578  # (10.53% * 2 for the 2/1 weight per assignment) * 75

    points = final_quizzes + final_ind_assign + final_rand_points + final_group_points + final_assign + final_participation
    points = round(points * 100, 2)
    total_points = participation_boost(points)
    return total_points


def run_program(hist, grade_list, effort):
    """Use this function to run all of the previous functions in the program.
    :param hist: A students prior history with coding
    :param grade_list: The list of grades for the number of students ran in the program
    :return stats: Statistics on each run that we are producing.
    """
    first_score = quiz_range(hist, effort)
    likely = likely_range(hist)
    total_quiz = quizzes(8, first_score, likely)
    total_part = participation(14)

    assign_range = assignment_range(hist, effort)
    total_ind = ind_assign(4, assign_range, likely)
    total_rand_group = random_partner(hist, assign_range, likely)
    total_group = group_assign(hist, 3, assign_range, likely)
    total_final = final_proj(hist, assign_range, likely)

    grade_percent = float(grade(total_part, total_quiz, total_ind, total_rand_group, total_group, total_final))
    grade_list.append(grade_percent)
    return grade_list


def analyze_students(num_exp, num_adv, num_int, num_beg, effort):
    """Run the program as many times as needed to get the desired results.
    :param num_exp: Total number of expert students
    :param num_adv: Total number of advanced students
    :param num_int: Total number of intermediate students
    :param num_beg: Total number of beginner students
    """
    grade_list = []

    for tests in range(num_exp):
        run_program('expert', grade_list, effort)
    for tests in range(num_adv):
        run_program('advanced', grade_list, effort)
    for tests in range(num_int):
        run_program('intermediate', grade_list, effort)
    for tests in range(num_beg):
        run_program('beginner', grade_list, effort)
    return grade_list


def dict(analyze_cat, num_students):
    """Create a dictionary out of the list of grades and student programming experience
    :param analyze_cat: The category of analyzed students based on experience
    :param num_students: The total number of students that were ran in the program
    """
    analyze_dict = {}
    keys = range(num_students)
    for i in keys:
        analyze_dict[i] = analyze_cat[i]
    return analyze_dict


def graph(grade_dict, num_students, hist, effort):
    """Create a graph based on the number of times we analyze the students and their total grades.
    :param grade_dict: A dictionary filled with the grades and number of times the program is run
    :param num_students: The total number of students than were ran in the program
    :param hist: The prior programming experience category of the analyzed students
    """
    dictionary = dict(grade_dict, num_students)
    lists = sorted(dictionary.items())
    x, y = zip(*lists)

    plt.plot(x, y)
    plt.xlabel("Count")
    plt.ylabel("Grade %")
    plt.title(hist)
    plt.savefig('{}_{}.pdf'.format(hist, num_students))  # save the figure to file
    plt.close()


def dataframe(dictionary):
    """Create a dataframe from the student analysis dictionary.
    :param dictionary: Dictionary from the student analysis data.
    """
    df = pd.DataFrame.from_dict(dictionary, orient='index')
    return df


num_students = 100

expert_0 = analyze_students(num_students, 0, 0, 0, effort=0)
expert_1 = analyze_students(num_students, 0, 0, 0, effort=1)
expert_2 = analyze_students(num_students, 0, 0, 0, effort=2)

advanced_0 = analyze_students(0, num_students, 0, 0, effort=0)
advanced_1 = analyze_students(0, num_students, 0, 0, effort=1)
advanced_2 = analyze_students(0, num_students, 0, 0, effort=2)

intermediate_0 = analyze_students(0, 0, num_students, 0, effort=0)
intermediate_1 = analyze_students(0, 0, num_students, 0, effort=1)
intermediate_2 = analyze_students(0, 0, num_students, 0, effort=2)

beginner_0 = analyze_students(0, 0, 0, num_students, effort=0)
beginner_1 = analyze_students(0, 0, 0, num_students, effort=1)
beginner_2 = analyze_students(0, 0, 0, num_students, effort=2)

a_0 = dict(expert_0, num_students)
a_1 = dict(expert_1, num_students)
a_2 = dict(expert_2, num_students)
b_0 = dict(advanced_0, num_students)
b_1 = dict(advanced_1, num_students)
b_2 = dict(advanced_2, num_students)
c_0 = dict(intermediate_0, num_students)
c_1 = dict(intermediate_1, num_students)
c_2 = dict(intermediate_2, num_students)
d_0 = dict(beginner_0, num_students)
d_1 = dict(beginner_1, num_students)
d_2 = dict(beginner_2, num_students)

exp_graph_0 = graph(a_0, num_students, 'Expert Programmer with 0 Effort', 0)
exp_graph_1 = graph(a_1, num_students, 'Expert Programmer with 1 Effort', 1)
exp_graph_2 = graph(a_2, num_students, 'Expert Programmer with 1 Effort', 2)

adv_graph_0 = graph(b_0, num_students, 'Advanced Programmer with 0 Effort', 0)
adv_graph_1 = graph(b_1, num_students, 'Advanced Programmer with 1 Effort', 1)
adv_graph_2 = graph(b_2, num_students, 'Advanced Programmer with 2 Effort', 2)

int_graph_0 = graph(c_0, num_students, 'Intermediate Programmer with 0 Effort', 0)
int_graph_1 = graph(c_1, num_students, 'Intermediate Programmer with 1 Effort', 1)
int_graph_2 = graph(c_2, num_students, 'Intermediate Programmer with 2 Effort', 2)

beg_graph_0 = graph(d_0, num_students, 'Beginner Programmer with 0 Effort', 0)
beg_graph_1 = graph(d_1, num_students, 'Beginner Programmer with 1 Effort', 1)
beg_graph_2 = graph(d_2, num_students, 'Beginner Programmer with 2 Effort', 2)


exp_df_0 = dataframe(a_0)
exp_df_1 = dataframe(a_1)
exp_df_2 = dataframe(a_2)

adv_df_0 = dataframe(b_0)
adv_df_1 = dataframe(b_1)
adv_df_2 = dataframe(b_2)

int_df_0 = dataframe(c_0)
int_df_1 = dataframe(c_1)
int_df_2 = dataframe(c_2)

beg_df_0 = dataframe(d_0)
beg_df_1 = dataframe(d_1)
beg_df_2 = dataframe(d_2)

m0 = pd.merge(exp_df_0, exp_df_1, left_index=True, right_index=True)
m1 = pd.merge(m0, exp_df_2, left_index=True, right_index=True)
m2 = pd.merge(m1, adv_df_0, left_index=True, right_index=True)
m3 = pd.merge(m2, adv_df_1, left_index=True, right_index=True)
m4 = pd.merge(m3, adv_df_2, left_index=True, right_index=True)
m5 = pd.merge(m4, int_df_0, left_index=True, right_index=True)
m6 = pd.merge(m5, int_df_1, left_index=True, right_index=True)
m7 = pd.merge(m6, int_df_2, left_index=True, right_index=True)
m8 = pd.merge(m7, beg_df_0, left_index=True, right_index=True)
m9 = pd.merge(m8, beg_df_1, left_index=True, right_index=True)
m10 = pd.merge(m9, beg_df_2, left_index=True, right_index=True)

frames = [exp_df_0, exp_df_1, exp_df_2, adv_df_0, adv_df_1, adv_df_2, int_df_0 ,int_df_1, int_df_2,
          beg_df_0, beg_df_1, beg_df_2]
total = pd.concat(frames)

m11 = pd.merge(m10, total, left_index=True, right_index=True)

m11.columns = ['expert_effort_0', 'expert_effort_1', 'expert_effort_2',  'advanced_effort_0', 'advanced_effort_1',
               'advanced_effort_2', 'intermediate_effort_0', 'intermediate_effort_1', 'intermediate_effort_2',
               'beginner_effort_0', 'beginner_effort_1', 'beginner_effort_2', 'overall_distribution']


m11.describe().to_csv('results_{}.csv'.format(num_students))



