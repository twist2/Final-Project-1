# Title: Probability of Passing IS590PR

## Team Member(s):  Daria Orlowska & Michelle Twist

# Monte Carlo Simulation Scenario & Purpose:
Given several aspects of a student's history with programming as well as how the course work is graded, we will use this simulation to predict the grade outcome for a given student. We will be using the syllabus for this course, the randomness from group assignments, and the grader's scale to determine how well a student will do in this course. 

## Simulation's variables of uncertainty
* Familiarity with programming: On a scale of 50 to 100, where 50 to 64 is a beginner, 65 to 79 is intermediate, 80 to 94 is advanced, and 95 to 100 is expert. This assumes that since 590PR requires some prerequisite for entry, all students enter with some fundamental skills.
   
   - Beginner: between 0 and 100 for quizzes, and between 40 and 100 for assignments
   
   - Intermediate: between 30 and 100 for quizzes, and between 60 and 100 for assignments
   
   - Advanced: between 60 and 100 for quizzes, and between 75 and 100 for assignments
   
   - Expert: between 80 and 100 for quizzes, and between 85 and 100 for assignments

* Quizzes: There are 9 quizzes total. There are two attempts for each quiz. The second attempt will be greater than or equal to your first attempt. Both attempts are averaged into a single score.

* Reading advantage: Doing the assigned readings gives you between 0-20% advantage on quizzes

* Group assignments: In group assignments, your score range is adjusted by your group members' familiarity with programming.
  * 2 scenarios: either the ability to pick your partner, or being randomly assigned a partner

    **_Choose partner_**: match with someone of equal skill or within one level of you.
    
    * If matching in skill set, no advantage:
    
         - Expert matching with expert has a disadvantage of 0%
         - Advanced matching with advanced has a disadvantage of 2%
         - Intermediate matching with intermediate has a disadvantage of 5%
         - Beginner matching with beginner has a disadvantage of 10%
    
    * If partner has higher skills than you, you have an advantage of 5%
    
    * If you have higher skills than your partner, you have a disadvantage of 5%

    **_Randomly assigned partner_**: varying skillset. The idea here is that as a student with less familiarity with programming, you will have a greater change of receiving more points on your assingnment when your partner is at a higher skill than you are. However, if you have more familiarity with programming, you are the greatest disadvantage when you do not have a lot of programming experience and your partner has even less experience. If you have a lot more experience than your partner, this is only a minor disadvantage because you are capable of doing most of the work yourself. The total advantage or disadvantage is averaged based total group members. 
    
    * If 1 skillset above, advantage 5%; below, disadvantage 15%
    * If 2 skillsets above, advantage 10%; below, disadvantage 10%
    * If 3 skillsets above, advantage 15%; below, disadvantage 5%
        
  * Groups numbers (1-3)

* Assignments: There are 9 total assignments in the class. Four are individual, four are group projects, and one is a final assignment. Of the group projects, 3 allow for choosing a partner, and in one groups are randomly assigned.

* Student Participation: A completely random variable based on the total number of classes. 

## Hypothesis or hypotheses before running the simulation:
Students who have had prior experience coding in Python will me more likely to pass the course with a higher grade than those who came in with little experience. 

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:
