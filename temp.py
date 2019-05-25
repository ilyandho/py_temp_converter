
print('\n\t\t\t***Welcome to my weight converter***\n')

cont = True
while cont:
    decision = input(
        "\nSelect what you would like to do:\n\t1. Celcius to Fahrenheit\n\t2. Fahrenheit to celcius\n\t3. Quit\n")

    if decision is '1':
        print('Okay, let\'s convert to Fahrenheit')

        celcius = float(input('Enter temperature in Celcius:'))
        fahrenheit = (celcius*5/9)+32
        print('Temperature in Fahrenheit is:', fahrenheit)
    elif decision is '2':
        print('Okay, let\'s convert to Celcius')

        fahrenheit = float(input('Enter temperature in Fahrenheit:'))
        celcius = (fahrenheit-32)*9/5
        print('Temperature in Fahrenheit is:', celcius)
    elif decision is '3':
        cont = False
        print('Quitting ...')
    else:
        print('Wrong input... Please select from the provided inputs')
