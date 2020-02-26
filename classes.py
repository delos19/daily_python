class Cat:
    kind = 'feline'
    def __init__(self, name):
        self.name = name
        self.toys = []
    def add_toy(self, toy):
        self.toys.append(toy)
    def age(self, year):
        self.age = (2020 - (int(year) - 2)) * 4 


a = Cat('Fina')     #Creates cat class with feline named Fina
b = Cat('Halo')     #Creates cat class with feline named Halo
a.add_toy('ball')
b.add_toy('yarn')

print('What toys does Fina have? \n')
print(a.toys)
print('What toys does Halo have? \n')
print(b.toys)

a.add_toy(input('What toy did you give fina for christmas? \n'))
print('Fina how has these toys: \n')
print(a.toys)

a.age = input('What year was Fina born? \n')
print('Finas age is: \n')
print(a.age)

    
