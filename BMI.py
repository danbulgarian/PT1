#BMI calculator
name1 = "Max"
height_m1 = 2
weight_kg1 = 120
gender1 = 0

name2 = "Violetka"
height_m2 = 1.70
weight_kg2 = 53
gender2 = 1

name3 = "Ivana"
height_m3 = 1.76
weight_kg3 = 46
gender3 = 1

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / pow(height_m, 2)
    print("bmi:{:,}".format(bmi))
    if bmi < 25:
        return name + " не е дебела"
    if bmi == 25:
        return name + "бива"
    else:
        return name + " е мега дебел"
bmi_calculator(name1, height_m1, weight_kg1)
bmi_calculator(name2, height_m2, weight_kg2)
bmi_calculator(name3, height_m3, weight_kg3)

