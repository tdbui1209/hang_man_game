class Quiz:
    def __init__(self, question):
        self.question = question
        self.length = len(self.question)
        self.health = 5
        self.index = []
        self.dis = ['_'] * len(self.question)

    def check(self, user_input):
        '''
        If guess correct, take all index of this character store in self.index
        If not, self.health minus 1
        '''
        if user_input in self.question:
            for index in range(self.length):
                if self.question[index] == user_input:
                    self.index.append(index)
        else:
            self.health -= 1

    def display(self):
        '''
        Change elements in self.dis with each self.question[index]
        '''
        for index in range(len(self.question)):
            if index in self.index:
                self.dis[index] = self.question[index]

    def gameover(self):
        return self.health != 0
