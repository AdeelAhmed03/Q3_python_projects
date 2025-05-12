class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")

temp_f = 98.6
temp_c = TemperatureConverter.fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F is {temp_c}°C")