# unit_converter_assignment
A Unit Converter converts values between different measurement units using predefined formulas. 
🔄 Advanced Unit Converter

This is a Streamlit-based Unit Converter that allows users to convert between various physical, digital, and scientific units. It includes predefined conversion factors and formulas for accurate results.

🚀 Features

Convert between Physical Units (Length, Area, Mass, Speed, Time)

Convert between Digital & Scientific Units (Temperature, Data Rate, Storage, Energy, Pressure)

Predefined formulas for temperature conversion

User-friendly UI with dropdowns and input fields

Dynamic unit selection based on the category

Real-time conversion results

🛠️ Installation & Setup

Install Streamlit if you haven't already:

pip install streamlit

Save the Python script (unit_converter.py).

Run the script using:

streamlit run unit_converter.py

The app will open in your browser, allowing you to select categories and convert units.

📌 How to Use

Select a category (e.g., Physical Units, Digital & Scientific Units).

Choose a sub-category (e.g., Length, Temperature, Mass, etc.).

Select the units to convert from and to.

Enter the value to be converted.

Click 'Convert' to see the result.

Formula for conversion is displayed before conversion.

🔢 Supported Units & Conversion Logic

1️⃣ Physical Units

Length: Meter, Kilometer, Centimeter, Millimeter, Mile, Yard, Foot, Inch

Area: Square Meter, Square Kilometer, Square Centimeter, Hectare, Acre

Mass: Kilogram, Gram, Milligram, Pound, Ounce

Speed: Meter per second, Kilometer per hour, Miles per hour

Time: Second, Minute, Hour, Day

👉 Conversion: Value × Conversion Factor

2️⃣ Digital & Scientific Units

Data Transfer Rate: Bit per second, Kilobit per second, Megabit per second, Gigabit per second

Digital Storage: Byte, Kilobyte, Megabyte, Gigabyte

Energy: Joule, Kilojoule, Calorie

Pressure: Pascal, Bar, PSI

👉 Conversion: Value × Conversion Factor

3️⃣ Temperature Conversion Formulas

Celsius to Fahrenheit: F = (C × 9/5) + 32

Fahrenheit to Celsius: C = (F - 32) × 5/9

Celsius to Kelvin: K = C + 273.15

Kelvin to Celsius: C = K - 273.15

Fahrenheit to Kelvin: K = (F - 32) × 5/9 + 273.15

Kelvin to Fahrenheit: F = (K - 273.15) × 9/5 + 32

👉 Conversion: Uses conditional logic to apply the correct formula.

⚡ Example Usage

Convert Length (Meters to Feet)

Input: 5 meters

Conversion Factor: 1 meter = 3.28084 feet

Output: 5 × 3.28084 = 16.4042 feet

Convert Temperature (Celsius to Fahrenheit)

Input: 100°C

Formula: F = (100 × 9/5) + 32

Output: 212°F


👨‍💻 Author

Developed using Streamlit

Contributions & suggestions are welcome!

Reach out for any improvements or issues 🚀

Enjoy using the Advanced Unit Converter! 🎉

