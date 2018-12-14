# Title: Probability of Passing IS590PR

## Team Member(s):  Daria Orlowska & Michelle Twist

# Monte Carlo Simulation Scenario & Purpose:
Given several aspects of a student's history with programming as well as how the course work is graded, we will use this simulation to predict the grade outcome for a given student. We will be using the syllabus for this course, the randomness from group assignments, and the grader's scale to determine how well a student will do in this course. 

## Simulation's variables of uncertainty
* Familiarity with programming: expert, advanced, intermediate and beginner. This assumes that since 590PR requires some prerequisite 
for entry, all students enter with some fundamental skills. The program uses a pert distribution to skew participation grades towards a 
"most likely" average, the distribution peak, which has been assigned as follows:

   - Beginner: 80
   - Intermediate: 85
   - Advanced: 90
   - Expert: 95
   
* The lower range of the pert distribution is determined by the amount of effort a student exhibits during the course. The upper range 
is always 100. The determined lower ranges are as follows:
   
   |     Experience      |   Effort Level  |  Lower Bounds Quiz  |  Lower Bounds Assignment  |
   -------------------------------------------------------------------------------------------
   |      Beginnner      |        0        |         30          |            60             |
   |      Beginnner      |        1        |         50          |            70             |        
   |      Beginnner      |        2        |         70          |            80             |
   |     Intermediate    |        0        |         55          |            65             |
   |     Intermediate    |        1        |         65          |            75             |
   |     Intermediate    |        2        |         75          |            85             |
   |       Advanced      |        0        |         70          |            70             |
   |       Advanced      |        1        |         80          |            80             |
   |       Advanced      |        2        |         90          |            90             |
   |        Expert       |        0        |         85          |            75             |
   |        Expert       |        1        |         90          |            85             |
   |        Expert       |        2        |         95          |            95             |
    
* Quizzes: There are 8 quizzes total. There are two attempts for each quiz. The second attempt will be greater than or equal to your 
first attempt. Both attempts are averaged into a single score. The probability of completing the quiz on time is 9 out of 10. Quizzes 
account for 15% of the final grade. 

* Reading advantage: Doing the assigned readings gives you between 20-50% advantage on quizzes. This is determined randomly.

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
   * The assignments weights are split as follows, .5 for one individual assignment, 1 each for the 3 additional individual assignments,     1 for the randomized group assignment, 1 each for the chosen group assignments and 2 for the final project. Assignments are worth       75% of the overall final grade. 

* Student Participation: A completely random variable based on the total number of classes. The probability of showing up to lecture is 9 out of 10. Particiaption counts for 10% of the final grade.

* Final Boost: A final boost is also implemented based on overall effort demonstrated. Students who did not show any effort during the semester do not receive a boost. Students who are at a 93% or above (A) also do not receive a boost. Students who have demonstrated some effort (1) will receive a quarter step up in grade (B+ to A-). Students who have demonstrated a lot of effort (2) will receive a half step up in grade (B+ to A).

## Hypothesis or hypotheses before running the simulation:
Students who have had prior experience coding in Python will be more likely to pass the course with a higher grade than those who came in with little experience. Those who also put in more effort in the course, will recieve a higher grade. 

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
__Adjusting__: This simulation was strongly influenced by discussions with John Weible about mirroring the course outcomes. Initially, all of our uncertainty variables were determined by using random.int, which resulted in uniform distribution instead of the skewed one that is a better representation of reality. Since our outputs were still lower than what we wanted, we ended up adding a final boost, similar to the one the instructor uses when determining final grades. Finally, we also incorporated effort into our simulation, because only including experience level to differentiate students did not accurately represent the situation.
__Management decisions__: The final outputs suggest that the class is designed so that everyone does well so long as they attempt assignments. A possible application of this scenario would be the instructor modifying his grading procedure if he wanted to achieve a wider spread of grades. Another possibility would be changing the grade weights for each course components to test out distribution changes before implementing new procedures.

## Instructions on how to use the program:
To run this simulation, open up the final_or_tw.py file in a Python compatable system. Next, run the program and you will be prompted to insert a number of students that you would like to analyze/how many times you want to run the program for. The program will save each graph for an expert, advanced, intermediate and beginner programmer to a separate file as well as the overall analysis to a separate csv file. 

## All Sources Used:
IS590PR Syllabus - https://courses.ischool.illinois.edu/pluginfile.php/369122/mod_resource/content/1/Syllabus.%20IS590PR%20Fall%202018.pdf
