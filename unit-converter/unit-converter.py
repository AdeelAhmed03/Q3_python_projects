import streamlit as st

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000, # 1 kilometer = 1000 meter
        "gram_kilogram": 0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000, # 1 kilogram = 1000 gram
        "celsius_fahrenheit": 32, # 0 celsius = 32 fahrenheit
        "fahrenheit_celsius": 5/9, # 32 fahrenheit = 0 celsius
        "centimeter_meter": 0.01, # 1 centimeter = 0.01 meter
        "meter_centimeter": 100, # 1 meter = 100 centimeter
        "gram_milligram": 1000, # 1 gram = 1000 milligram
        "milligram_gram": 0.001, # 1 milligram = 0.001 gram      
    } 

    key = f"{unit_from}_{unit_to}" # Generate a key based on the input and output units

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported" # If the conversion is not supported, return a message

st.title("Unit Converter") # Title of the app

value = st.number_input("Enter the value", min_value=1.0, step=1.0) # Input field for the value to convert

# Dropdown for the input unit
unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram", "celsius", "fahrenheit", "centimeter", "milligram"])

# Dropdown for the output unit
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram", "celsius", "fahrenheit", "centimeter", "milligram"])

# Button to trigger the conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to) # Convert the value
    st.write(f"Converted value: {result}") # Display the result

# Add a footer with the author's name
st.write("Created by [@AdeelAhmed03](https://github.com/AdeelAhmed03)")
