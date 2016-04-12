print('Body Mass Index Calculator')

weight = float(input('Please enter your weight in Kgs: '))
height = float(input('Please enter your height in m: '))

bmi =  weight / height ** 2

print('Your BMI is: ', bmi)
