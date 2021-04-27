from quiz import Quiz


quiz = Quiz()
while True:
    print(''.join(quiz.dis))
    quiz.check(input('Nhập 1 chữ cái: '))
    quiz.display()