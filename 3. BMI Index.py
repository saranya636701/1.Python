#Underweight (<18.5), Healthy (18.5–24.9), Overweight (25–29.9), and Very Overweight (>=30)
#Enter the BMI Index:34
BMI = int(input("Enter the BMI Index: "))
if(BMI < 18.5):
    print("Underweight")
elif(BMI < 24.9):
    print("Healthy")
elif(BMI < 29.9):
    print("Overweight")
else:
    print("Very Overweight")
