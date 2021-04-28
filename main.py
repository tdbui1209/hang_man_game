from quiz import Quiz
import random
from data import data

quiz = Quiz(random.choice(data))

while quiz.gameover():
    print(''.join(quiz.dis))
    quiz.check(input('Nhập 1 chữ cái: '))
    quiz.display()