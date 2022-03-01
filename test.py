
class User1:
    def __init__(self, name):
        self.name = name
        # self.city = city
        # self.state = state
    


# class User2:
#     def __init__(self, name):
#         self.name = name
#         self.city = city
#         self.state = state

    def __str__(self):
        return f"<User1 name = {self.name}>"


alex = User1("Alex")
jeff = User1 ("Jeff")


