def percentage():
    Sub1 = int(input("Subject1= "))
    Sub2 = int(input("Subject2= "))
    Sub3 = int(input("Subject3= "))
    Sub4 = int(input("Subject4= "))
    Sub5 = int(input("Subject5= "))
    Total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
    print("Total: ", Total)
    percentage = (Total/500)*100
    print("Percentage: ", percentage)
percentage()

