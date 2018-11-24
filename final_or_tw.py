import math
import random
import numpy as np


class IS590PR:

    def __init__(self, student_exp): # list our functions once they are created
        # declare self."functions"
        self.student_exp     = student_exp
        self.grader_scale    = grader_scale
        self.participation   = participation
        self.quizzes         = quizzes
        self.group_assign    = group_assign
        self.ind_assign      = ind_assign
        self.final_proj      = final_proj
        self.grade           = grade

    # Create a function that reads in a students prior experience with coding
    def student_exp(self):
        """Determine the advantage a student has for the success in the course
        :param  :
        :return :
        """
        name = input("Please enter your name: ")
        hist = input("Describe your level of experience with Python (beginner, amateur, advanced): ")
        if hist == 'beginner':
            first_score = 1
        if hist == 'amateur':
            first_score = 2
        if hist == 'advanced':
            first_score = 3

    # Create a function that predicts the grades's grading scale
    def grader_scale(self):
        """Determine whether the grader will grade harder or more lenient

        """



    # Create a function that randomly predicts the participation points received
    def participation(self):
        """Predict the grade for the students total participation in class

        """



    # Create a function that randomly predicts the total grade for the class Quizzes
    def quizzes(self):
        """Predict the grade for the students total quiz scores throughout the course

        """
        # We could try to see if the participation factors into this?


    # Create a function that randomly determines the outcome of group assignments
    def group_assign(self):
        """Predict the grade for the student's grades on the group assignments

        """
        # They should have an advantage based on their prior experience and the other students will be completely random


    # Create a function that randomly determines the outcome of indiviudal assignments
    def ind_assign(self):
        """Predict the grade for the student's individual assignments

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
