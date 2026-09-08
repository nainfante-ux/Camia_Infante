# NATE INIGO A. INFANTE
# 8 - CAMIA

print("This program is for calculating the average of the last 3 activities.")

# [INPUT STAGE]
a1 = int(input("enter activity 1's score: "))
a2 = int(input("enter activity 2's score: "))
a3 = int(input("enter activity 3's score: "))

# [CALCULATION]
totala = a1 + a2 + a3
average = float(totala) / 3

# [OUTPUT]
print(f"The average of all three of your activities is {average:.2f}")