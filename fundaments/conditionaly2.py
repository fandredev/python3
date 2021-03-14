# elif = else if

times = 7

if times == 0:
    tech = input('What is your favorite technology? ')
    if tech == 'Javascript':
        techs = []
        techs.append(tech)
        print(f'{tech} is amazing')
        print(f'{techs}')
    else:
        print(f'{tech} a very good!')
elif times == 10:
    animal = input('What is your favorite animal? ')
    if animal == 'Raposa': 
        animals = []
        animals.append(animal)
        print(f'{animal} is amazing')
        print(f'{animals}')
    else:
        print(f'{animal} is cool')
else:
    if times != 10 or times != 0:
        print('Times is not a number 0 or 10')
