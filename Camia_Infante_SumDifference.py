
# [GLOBAL VARIABLES]
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))


def calculate_sum():
    
    # [LOCAL VARIABLE]
    sum = num1 + num2
    sumdisplay = print("The sum is: ", sum)
    print(sumdisplay)

def calculate_difference():

    # [LOCAL VARIABLE]
    difference = num1 - num2
    differencedisplay = print("The difference is: ", difference)
    print(differencedisplay)

calculate_sum()
calculate_difference()