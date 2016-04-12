def bmi(w,h):
    return  (weight / height ** 2)

print('Body Mass Index Calculator')

weight = float(input('Please enter your weight in Kgs: '))
height = float(input('Please enter your height in m: '))


print('Your BMI is: ', bmi(weight,height))
