''''private Access
    only depend on the result rest hide the process done'''

# class person:
#     def __init__(self,name, age):
#         self.__name = name
#         self.__age = age

#     def display(self):
#         print(f"The person name is {self.__name} is {self.__age} years old")


# if __name__ == "__main__":
#     person_test = person(name= "Ram", age= 22)
#     person_test.display()



'''protected access '''
class person:
    def __init__(self,name, age):
        self._name = name
        self._age = age

    def display(self):
        return f"The person name is {self._name} is {self._age} years old"

class Ram(person):
    def __init__(self, name, age):
        super().__init__(name, age)




if __name__ == "__main__":
    person_test = person(name= "Ram", age= 22)
    print(person_test.display())

    ram_01 = Ram(name='rammma',age=24) #Access of protected modifier from the parent class.
    print(ram_01.display())