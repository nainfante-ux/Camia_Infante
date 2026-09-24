# NATE INIGO A. INFANTE
# 8 - CAMIA

print("This program is for calculating the average of the last 3 activities.")

# [INPUT STAGE]
a1 = int(input("enter activity 1's score: ")) #inputs score for activity 1
a2 = int(input("enter activity 2's score: ")) #inputs score for activity 2
a3 = int(input("enter activity 3's score: ")) #inputs score for activity 3

# [CALCULATION]
totala = a1 + a2 + a3 #calculates the sum of the activity scores for the numerator
average = float(totala) / 3 #calculates the average by dividing the sum of the activity scores by the number of activities

# [OUTPUT]
print(f"The average of all three of your activities is {average:.2f}") #f-string streamlines adding variable values to output; :.2f rounds average to 2 decimal points
