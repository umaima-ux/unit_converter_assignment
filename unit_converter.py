import streamlit as st

# Unit Conversion Data
unit_categories = {
    "Physical Units": {
        "Length": {
            "Meter": 1,
            "Kilometer": 0.001,
            "Centimeter": 100,
            "Millimeter": 1000,
            "Mile": 0.000621371,
            "Yard": 1.09361,
            "Foot": 3.28084,
            "Inch": 39.3701
        },
        "Area": {
            "Square Meter": 1,
            "Square Kilometer": 0.000001,
            "Square Centimeter": 10000,
            "Hectare": 0.0001,
            "Acre": 0.000247105
        },
        "Mass": {
            "Kilogram": 1,
            "Gram": 1000,
            "Milligram": 1000000,
            "Pound": 2.20462,
            "Ounce": 35.274
        },
        "Speed": {
            "Meter per second": 1,
            "Kilometer per hour": 3.6,
            "Miles per hour": 2.23694
        },
        "Time": {
            "Second": 1,
            "Minute": 1/60,
            "Hour": 1/3600,
            "Day": 1/86400
        }
    },
    "Digital & Scientific Units": {
        "Data Transfer Rate": {
            "Bit per second": 1,
            "Kilobit per second": 0.001,
            "Megabit per second": 0.000001,
            "Gigabit per second": 0.000000001
        },
        "Digital Storage": {
            "Byte": 1,
            "Kilobyte": 0.001,
            "Megabyte": 0.000001,
            "Gigabyte": 0.000000001
        },
        "Temperature": {
            "Celsius": "C",
            "Fahrenheit": "F",
            "Kelvin": "K"
        },
        "Energy": {
            "Joule": 1,
            "Kilojoule": 0.001,
            "Calorie": 0.239006
        },
        "Pressure": {
            "Pascal": 1,
            "Bar": 0.00001,
            "PSI": 0.000145038
        }
    }
}

# Predefined Formulas
conversion_formulas = {
    "Length": "Multiply the length value by the conversion factor",
    "Area": "Multiply the area value by the conversion factor",
    "Mass": "Multiply the mass value by the conversion factor",
    "Speed": "Multiply the speed value by the conversion factor",
    "Time": "Multiply the time value by the conversion factor",
    "Data Transfer Rate": "Multiply the data transfer rate value by the conversion factor",
    "Digital Storage": "Multiply the storage value by the conversion factor",
    "Energy": "Multiply the energy value by the conversion factor",
    "Pressure": "Multiply the pressure value by the conversion factor",
    "Temperature": {
        "Celsius to Fahrenheit": "F = (C × 9/5) + 32",
        "Fahrenheit to Celsius": "C = (F - 32) × 5/9",
        "Celsius to Kelvin": "K = C + 273.15",
        "Kelvin to Celsius": "C = K - 273.15",
        "Fahrenheit to Kelvin": "K = (F - 32) × 5/9 + 273.15",
        "Kelvin to Fahrenheit": "F = (K - 273.15) × 9/5 + 32"
    }
}

# Streamlit UI
st.title("🔄 Advanced Unit Converter")

category = st.selectbox("📌 Select a Category", list(unit_categories.keys()))
sub_category = st.selectbox("🔍 Select a Unit Type", list(unit_categories[category].keys()))

# Default Units
units = list(unit_categories[category][sub_category].keys())
default_from_unit = units[0]
default_to_unit = units[1] if len(units) > 1 else units[0]

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("Convert from", units, index=0)
with col2:
    to_unit = st.selectbox("Convert to", units, index=units.index(default_to_unit))

# User Input
value = st.number_input(f"Enter value in {from_unit}:", min_value=0.0, format="%.4f")

# Display Formula
if sub_category in conversion_formulas:
    if sub_category == "Temperature":
        formula_key = f"{from_unit} to {to_unit}"
        formula_text = conversion_formulas["Temperature"].get(formula_key, "Select valid units")
    else:
        formula_text = conversion_formulas[sub_category]
    st.info(f"📌 Formula: {formula_text}")

# Conversion Logic
if st.button("Convert"):
    if sub_category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
    else:
        result = value * (unit_categories[category][sub_category][to_unit] / unit_categories[category][sub_category][from_unit])
    
    st.success(f"🔄 Converted Value: {result:.4f} {to_unit}")
