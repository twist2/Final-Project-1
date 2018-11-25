# Title: Probability of Passing IS590PR

## Team Member(s):  Daria Orlowska & Michelle Twist

# Monte Carlo Simulation Scenario & Purpose:
Given several aspects of a student's history with programming as well as how the course work is graded, we will use this simulation to predict the grade outcome for a given student. We will be using the syllabus for this course, the randomness from group assignments, and the grader's scale to determine how well a student will do in this course. 

## Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?

Familiarity with programming: On a scale of 50 to 100, where 50 to 64 is a beginner, 65 to 79 is intermediate, 80 to 94 is advanced, and 95 to 100 is expert. This assumes that since 590PR requires some prerequisite for entry, all students enter with some fundamental skills.
Group assignments: In group assignments, the familiarity your group members have with programming.
2 scenarios: either the ability to pick your partner, or being randomly assigned a partner - Choose partner: match with someone of equal skill - Randomly assigned partner: varying skillset. The idea here is that as a student with less familiarity with programming, you will have a greater change of receiving more points on your assingnment when your partner(s) is at a higher skill than you are. However, if you have more familiarity with programming, you are the greatest disadvantage when you do not have a lot of programming experience and your partner has even less experience. If you have a lot more experience than your partner, this is only a minor disadvantage because you are capable of doing most of the work yourself. The total advantage or disadvantage is averaged based total group members. - If matching in skill set, no advantage, disadvantage 10% - If 1 skillset above, advantage 5%; below, disadvantage 15% - If 2 skillsets above, advantage 10%; below, disadvantage 15% - If 3 skillsets above, advantage 15%; ; below, disadvantage 10% - If 4 skillsets above, advantage 20%; ; below, disadvantage 5%
Groups numbers (2-4)
Grader variation: All graders employ varying levels of leniancy when assessing an assignment - Easy grader: Grades between 80% and 100% - Medium grader: Grades between 70% and 90% - Hard grader: Grades between 60% and 80%

## Hypothesis or hypotheses before running the simulation:
Students who have had prior experience coding in Python will me more likely to pass the course with a higher grade than those who came in with little experience. 

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:
