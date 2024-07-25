class MyList(list):
    def __init__(self):
        super().__init__()

    def duplicate(self, number):
        return self + self


my_list = MyList()
my_list.duplicate([23, 67, 45])
print(my_list)
