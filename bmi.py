# BMI calculator
# Intro
print ("Welkom bij deze BMI calculator")
print ("Door Joep Verboven")
print ("Versie 1.0")

# Lengte en gewicht vraag
lengte = float(input("Vul je lengte in meters in: "))
gewicht = int(input("Vul je gewicht in kilogram: "))

# Berekenen BMI waarde + Output
bmi = gewicht / (lengte * lengte)
print ("Je BMI is: ", round(bmi, 1))

# Advies na BMI output
if bmi < 18.5:
	print ("Je bent te licht voor je lengte")

elif bmi > 18.5 and bmi < 25:
	print ("Je BMI is in orde")

elif bmi > 25 and bmi < 30:
	print ("Je bent iets te zwaar voor je lengte")

elif bmi > 30:
	print ("Je bent obese")



# Oude code (niet meer in gebruik)
# print (bmi)
# print("Je BMI is: ", round(gewicht / (lengte * lengte), 2))
