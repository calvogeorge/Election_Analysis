
#Counties Practice from Module 3
counties = ["Arapahoe", "Denver","Jefferso"]
if counties[1] == "Denver":
    print(counties[1])

if "El Paso" in counties:
    print ("El Paso is in the list of counties.")
else:
    print ("El Paso is not in the list of counties.")


if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso are not in the list of counties.")
    

#Temperature practice from Module 3

temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the windows")

#Grade Practice from Module 3
    
grade = int(input("What is your Grade?"))

if grade > 100:
    print("Error, Grade cannot be over 100")
elif grade >= 90:
    print("Your Grade is an A")
elif grade >= 80:
    print("Your Grade is a B")
elif grade >= 70:
    print("Your Grade is a C")
elif grade >=60:
    print("Your Grade is a  D")
else:
    print("Your Grade is an F")
            


