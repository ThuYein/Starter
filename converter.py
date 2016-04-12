print('Temperature Conversion Program')

celsiusVlaue = float(input('Enter temperature in Celsius: '))
fahrenheitValue = celsiusVlaue * 9 / 5 + 32
kelvinValue = (fahrenheitValue + 459.67) * 5 / 9

print('Celsius Value: ', celsiusVlaue)
print('Fahrenheit Value: ', fahrenheitValue)
print('Kelvin Value: ', kelvinValue)
