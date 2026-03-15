class EligibilityForMarriage():
    def Eligible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if(gender == "Male" and age < 21):
            print("Not Eligible")
        elif(gender == "Female" and age < 18):
            print("Not Eligible")
        else:
            print("Eligible")
EligibilityForMarriage.Eligible()
