#BMI calculator
name1 = "Max"
height_m1 = 2
weight_kg1 = 120

name2 = "Violetka"
height_m2 = 1.70
weight_kg2 = 53

name3 = "Ivana"
height_m3 = 1.76
weight_kg3 = 46

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:   
        return name + " не е дебела"
    else:
        return name + " е мега дебел"

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

# const name1 = 'Max';
# const height_m1 = 2;
# const weight_kg1 = 120;
#
# const name2 = "Violetka"
# const height_m2 = 1.70
# const weight_kg2 = 53
#
# const name3 = "Ivana"
# const height_m3 = 1.76
# const weight_kg3 = 46
#
# function bmi_calculator(name, height_m, weight_kg) {
#
#     console.log(`bmi: ${bmi}`)
# }
