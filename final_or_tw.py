import math
import random
import numpy as np


class IS590PR:

    def __init__(self, student_exp, particiaption, quizzes, group_assign, ind_assign, final_proj, grade): # list our functions once they are created
        # declare self."functions"
        self.student_exp     = student_exp
        self.participation   = participation
        self.quizzes         = quizzes
        self.group_assign    = group_assign
        self.ind_assign      = ind_assign
        self.final_proj      = final_proj
        self.grade           = grade

    # Create a function that reads in a students prior experience with coding
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
        return first_score, hist


    # Create a function that randomly predicts the participation points received
    def participation(self, num_classes):
        """Predict the grade for the students total participation in class
        :param num_classes: Total number of classes to participate in
        """



    # Create a function that randomly predicts the total grade for the class Quizzes
    def quizzes(self, num_quiz):
        """Predict the grade for the students total quiz scores throughout the course
        :param num_quiz: Total number of quizzes in the course
        """
        for quizzes in range(1,num_quiz):
            quiz_grade = random.randint(1,100)
        final_quiz_grade = quiz_grade * .15
        # We could try to see if the participation factors into this?
        # So far, there are a total of 8 quizzes


    # Create a function that randomly determines the outcome of group assignments
    def group_assign(self, num_g_assign, first_score):
        """Predict the grade for the student's grades on the group assignments
        :param num_g_assign: Total number of group assignments
        """

        # They should have an advantage based on their prior experience and the other students will be completely random


    # Create a function that randomly determines the outcome of indiviudal assignments
    def ind_assign(self, num_i_assign):
        """Predict the grade for the student's individual assignments
        :param num_i_assign: Total number of individual assignments
        """
        # They should have an advantage if they have had prior experience


    # Create a function that randomly determines the final project grade
    def final_proj(self):
        """Predict the grade for the student's final project

        """
        # This could be completely random since we are working on it now?

    # Create a function that adds all the grades up into one for a final probability
    def grade(self):
        """Use all of the following information and the weight of each grade to determine the final grade
            for the student in this course. Will they pass the course?

        """

# if __name__ == "__main__":
#     IS590PR()
