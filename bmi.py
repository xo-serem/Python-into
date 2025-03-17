#BMI calc
weight=63
height= 1.75
bmi=weight/height**2
if bmi<18.5:
    print("Underweight")
elif    bmi>=18.5 and bmi<25:
    print("Normal")
elif     bmi>=25 and bmi<30:
    print("Overweight")
elif  bmi>=30 and bmi<35:
    print("Obese")
elif     bmi>=35 and bmi<40:
    print("Severly Obese")
else:
    print("Morbidly Obese")
print(bmi)