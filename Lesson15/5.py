class Test(str):
    def __init__(self,word):
        super().__init__()
        # self.word = word

    def __len__(self):
        return 25

a = Test('hello')
print(len(a))