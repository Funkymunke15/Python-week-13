# Davis Arita
# 11/21/22
# CS 131 Lecture 13A lab1
# Student driver file

from IC_student import Student

s1 = Student("Jon")

s1.addQuiz(90)
s1.addQuiz(100)

print("The total score for", s1.getName(), "is", s1.getTotalScore(), "and the average is",
      s1.getAverageScore())
