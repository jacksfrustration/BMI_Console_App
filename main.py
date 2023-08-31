keep_going=True
data=[]
while keep_going:
    #asks for name and height
    name=input("What is the person's name?\n").title()
    height=input("What is the person's height in meters?\n")
    try:
        #tries to convert the height to float. if input is not a number execute the appropriate error message and restart the program

        height=float(height)
    except TypeError:
        print("Input is not a number. Restart the program")
        break
    except ValueError:
        print("Input is not a number. Restart the program")
        break
    if height>2.4:
        #if height is more than 2.4 restart the program
        print("Height is not correct. Restart the program\n")
        break
    weight=input("How much does the person weight in kilos?\n")
    try:
        #tries to convert the weight to float. if input is not a number execute the appropriate error message and restart the program

        weight=float(weight)
    except TypeError:
        print("Input is not a number. Restart the program")
        break
    except ValueError:
        print("Input is not a number. Restart the program")
        break
    #creates a list of dictionaries of all the data input by the user
    data.append({"name":name,"height":height,"weight":weight})
    #stops this loop in order to complete the applications first step if input is no or n
    going=input("Keep going?\nType 'no' to stop.\n").lower()
    if going=="no" or going=="n":
        keep_going=False
new_list=[]
for person in data:
    #calculates BMI value
    result=person["weight"]/(person["height"]**2)
    name=person["name"]
    if result<18.5:
        #based on the BMI value the category in which the person is in is generated
        bmi="Underweight"
    elif result<24.9:
        bmi="Normal Healthy Weight"
    elif result<29.9:
        bmi="Overweight"
    elif result<39.9:
        bmi="Obese"
    else:
        bmi="Morbidly Obese"


    #creates a new list of peoples names and BMI category classification
    new_list.append({"name":name,"bmi":bmi})
for person in new_list:
    #prints out peoples names and BMI category classification
    print(f"{person['name'].title()} is {person['bmi']}")