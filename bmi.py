"""height = input("Enter your height in m: ")
weight = input ("Enter your weight in kg: ")
height = float(height)
weight = int(weight)
body_mass_index = int(weight / height ** 2)
print("Your bmi is : " + str(body_mass_index))"""

"""if body_mass_index < 18.5:
    print("You're underwight")
elif body_mass_index < 25:
    print("You're weight is normal")
elif body_mass_index < 30:
    print("You're overweight")
elif body_mass_index < 35:
    print("You're obese!")
else:
    print("Clinically obese")"""

year = int(input("Enter a year: "))
leap_year = year % 4 == 0
not_leap = year % 100 == 0
leap_year2 = year % 400 == 0

if leap_year != 0:
    print("leap year")
elif leap_year == 0:
    print("not leap year")
elif not_leap == 0:
    print("leap")
elif not_leap != 0:
    print("leap year")
elif leap_year2 == 0:
    print("not leap year")
elif leap_year2 != 0:
    print("leap year")

   


 
  



