rom diseas import Disease
from parse import analyzing
from config import FILE_NAME
from random import randint

if __name__ == '__main__':
    """
    Main module that runs the program.
    """
    def working_with_user(disea):
        print('Choose what you want to know about that disease:\naverage_value(will return the average value\
of deaths for the certain period of time)\naverage_changing(will return the average annual changing for the death rate)\n\
graphic(will show you a plot for the death rates)\n\
predicting(will make a prediction for the year, that you type)\n\
min_value and max_value')
        new1_command = input()
        if new1_command in ['average_value', 'average_changing', 'max_value', 'min_value']:
            print(eval(f'Disease(disea).{new1_command}()'))
        elif new1_command == 'graphic':
            value1 = input("Do you want to have the prediction on your graphic?\
            Type 2018 in this case. Otherwise type nothing\n")
            Disease(disea).graphic(int(value1))
        elif new1_command == 'predicting':
            value1 = input("Type the year, which value have to be predicted(int bigger than 2018)")
            Disease(disea).graphic(value1)
        else:
            print('Something went wrong')


    while True:
        print('Hello, now you are using the program, that can acknowledge you with data about death rates')
        print('Here you can use following commands:\nshow - to show the list of the death causes\n\
leave - to go out of the program')
        command = input()
        if command == 'show':
            for index, illness in enumerate(analyzing(FILE_NAME).keys()):
                print(index, illness)
            new_command = input("Now, choose the number of the disease or type randomly\
if you don't want to read a lot\n")

            if new_command == 'randomly':
                value = randint(0, 55)
                for index1, illness1 in enumerate(analyzing(FILE_NAME).keys()):
                    if index1 == value:
                        print(illness1)
                        working_with_user(illness1)

            elif '0' <= new_command <= '55':
                for index2, illness2 in enumerate(analyzing(FILE_NAME).keys()):
                    if index2 == int(new_command):
                        working_with_user(illness2)

        elif command == 'leave':
            break
