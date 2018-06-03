name = input('What is your name? ')
while name != "":
    for i in range(100):
        print(name,end=' ')
    print('')
    name = input('please enter another name,or just hit [ENTER] to quit:')
print("Thanks for playing!")
