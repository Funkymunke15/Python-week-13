# Davis Arita
# 11/21/22
# CS 131 Lecture 13A lab 2
# student class file

class Student:
    def __init__(self, name):
        self._name = name
        self._q_score = 0

        self._numQuiz = 0

    def getName(self):
        return self._name

    def addQuiz(self, score):
        self._q_score += score
        self._numQuiz += 1

    def getTotalScore(self):
        return self._q_score

    def getAverageScore(self):
        return self._q_score/self._numQuiz

