import random
import time

done = False

def rolld20():
    d20output = random.randint(1,20)
    if d20output == 20:
        print('Rolling...')
        time.sleep(1)
        print("You rolled a 20! A critical hit!")
    elif d20output == 1:
        print('Rolling...')
        time.sleep(1)
        print("You rolled a 1. A critical failure.")
    else:
        print('Rolling...')
        time.sleep(1)
        print('You rolled a ' + str(d20output))

def rolld12():
    d12output = random.randint(1,12)
    if d12output == 12:
        print('Rolling...')
        time.sleep(1)
        print("12! A critical hit!")
    elif d12output == 1:
        print('Rolling...')
        time.sleep(1)
        print("1. A critical failure.")
    else:
        print('Rolling...')
        time.sleep(1)
        print(d12output)

def rolld10():
    d10output = random.randint(1,10)
    if d10output == 10:
        print('Rolling...')
        time.sleep(1)
        print("10! A critical hit!")
    elif d10output == 1:
        print('Rolling...')
        time.sleep(1)
        print("1. A critical failure.")
    else:
        print('Rolling...')
        time.sleep(1)
        print(d10output)

def rolld8():
    d8output = random.randint(1,8)
    if d8output == 8:
        print('Rolling...')
        time.sleep(1)
        print("8! A critical hit!")
    elif d8output == 1:
        print('Rolling...')
        time.sleep(1)
        print("1. A critical failure.")
    else:
        print('Rolling...')
        time.sleep(1)
        print(d8output)

def rolld6():
    d6output = random.randint(1,6)
    if d6output == 6:
        print('Rolling...')
        time.sleep(1)
        print("6! A critical hit!")
    elif d6output == 1:
        print('Rolling...')
        time.sleep(1)
        print("1. A critical failure.")
    else:
        print('Rolling...')
        time.sleep(1)
        print(d6output)

def rolld4():
    d4output = random.randint(1,4)
    if d4output == 4:
        print('Rolling...')
        time.sleep(1)
        print("4! A critical hit!")
    elif d4output == 1:
        print('Rolling...')
        time.sleep(1)
        print("1. A critical failure.")
    else:
        print('Rolling...')
        time.sleep(1)
        print(d4output)

def rolld100():
    d100output = random.randint(1,100)
    if d100output == 100:
        print('Rolling...')
        time.sleep(1)
        print("100! A critical hit!")
    elif d100output == 1:
        print('Rolling...')
        time.sleep(1)
        print("1. A critical failure.")
    else:
        print('Rolling...')
        time.sleep(1)
        print(d100output)

def custom():
    customnumber = input('How many sides does your custom die have? Enter a number:')
    customoutput = random.randint(1,int(customnumber))
    if customoutput == customnumber:
        print('Rolling...')
        time.sleep(1)
        print(str(customnumber) + "! A critical hit!")
    elif customoutput == 1:
        print('Rolling...')
        time.sleep(1)
        print("1. A critical failure.")
    else:
        print('Rolling...')
        time.sleep(1)
        print(customoutput)


while not done:
    diceroll = input("Roll the Dice! You can enter d4, d6, d8, d10, d12, d20, d100, or custom. q to exit:")
    print('You entered ' + str(diceroll) + ':')
    if diceroll == 'd20':
        rolld20()
    elif diceroll == 'd12':
        rolld12()
    elif diceroll == 'd100':
        rolld100()
    elif diceroll == 'd10':
        rolld10()
    elif diceroll == 'd8':
        rolld8()
    elif diceroll == 'd6':
        rolld6()
    elif diceroll == 'd4':
        rolld4()
    elif diceroll == 'q':
        quit()
    elif diceroll == 'custom':
        custom()
    else:
        print('Incorrect input.')