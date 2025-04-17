import time
from datetime import datetime

loop_variable = True

OPTIONS = {
    'ramen':(6, 30),
    'salad':(15, 0),
    'dippy':(4, 30)
}
# dictionary ^ (anything with a 'key': value is a dictionary)

while loop_variable:

    egg_validator = True
    while egg_validator:

        result = input('what TASTEY egg would you like...')
        if result not in OPTIONS:
            print("Don't ever speak to me again.")
            exit()
        else:
            print(f'mmmmm i love {result} egg')
            egg_validator = False

    NUM_MINS, NUM_SECS = OPTIONS[result]

    print(f'you will have to wait {NUM_MINS} minutes and {NUM_SECS} seconds for this tastey tastey egg...')

    proceed = input('are you ready for your EGG? (yes or no...)')

    if proceed == 'yes':
        loop_variable = False



TIME_PERIOD = 10

total_seconds = 60 * NUM_MINS + NUM_SECS 

t = datetime.now()

print("current time is...")
print(t)

number_statements = total_seconds // TIME_PERIOD
# // is for integers only !

for i in range (number_statements):
    # for loop needs a colon
    
    time.sleep(TIME_PERIOD)
    total_seconds = total_seconds - TIME_PERIOD
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    print (f'{minutes}mins {seconds}secs')

    if minutes == 0:
        print (f'{seconds}secs')
    else:
        print (f'{minutes}mins {seconds}secs')

print ('get that egg outta the water')
print ('i hope you have an eggcellent meal hahahahahaha do you get it egg like the food')