def convert(Fahrenheit):
    f = float(Fahrenheit)
    celsius = (f - 32) * 5/9
    return celsius

# Enter temperature in Fahrenheit
print(f"The temperature is {convert(30)}\xb0 celsius")