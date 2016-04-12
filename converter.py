def fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9

print('Temperature Conversion Program')

celsiusVlaue = float(input('Enter temperature in Celsius: '))

print('Celsius Value: ', celsiusVlaue)
print('Fahrenheit Value: ', fahrenheit(celsiusVlaue))
print('Kelvin Value: ', kelvin(celsiusVlaue))
