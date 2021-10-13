class Person:
    arms_count = 2

    def greet(self):
        print(f'HI {self.name}!')


    def __eq__(self, other):

    def _init_(self):
        self.name = self

me = Person("nick")
you = Person("vova")
    me.greet()
    you.greet()



print(me.arms_count, you.arms_count)

Person.arms_count = 5
print(me.arms_count, you.arms_count)



print(me.name, you.name)
me.greet()
you.greet()