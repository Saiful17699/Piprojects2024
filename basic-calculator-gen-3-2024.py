import math

def user_guide():
    print("\n--- User Guide ---")
    print("1. Distance Conversion: Convert kilometers to miles or vice versa.")
    print("2. Basic Calculations: Perform addition, subtraction, multiplication, and division.")
    print("3. Scientific Calculations: Trigonometric functions (sin, cos, tan), logarithms, square root, etc.")
    print("4. Unit Conversion: Convert between different units (temperature, length, etc.).")
    print("5. Type 'previous' to go back to the previous step.")
    print("6. Type 'quit' to exit the program.")
    print("--------------------\n")

# Distance conversion (km to miles and vice versa)
def distance_conversion():
    print("\n--- Distance Conversion ---")
    while True:
        choice = input("Type '1' to convert kilometers to miles, '2' for miles to kilometers (or 'previous' to go back): ").strip()
        if choice == 'previous':
            return
        try:
            if choice == '1':
                km = float(input("Enter distance in kilometers: "))
                miles = km * 0.621371
                print(f"{km} kilometers is {miles:.2f} miles")
            elif choice == '2':
                miles = float(input("Enter distance in miles: "))
                km = miles / 0.621371
                print(f"{miles} miles is {km:.2f} kilometers")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Basic calculations
def basic_calculations():
    print("\n--- Basic Calculations ---")
    while True:
        operation = input("Enter the operation (+, -, *, /) or 'previous' to go back: ").strip()
        if operation == 'previous':
            return
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    raise ZeroDivisionError("Cannot divide by zero!")
            else:
                raise ValueError("Invalid operation!")
            print(f"Result: {result}")
            break
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}. Please try again.")

# Scientific calculations
def scientific_calculations():
    print("\n--- Scientific Calculations ---")
    while True:
        print("Choose an option:")
        print("1. Sin\n2. Cos\n3. Tan\n4. Logarithm\n5. Square Root\nType 'previous' to go back.")
        choice = input("Your choice: ").strip()

        if choice == 'previous':
            return
        try:
            if choice in ['1', '2', '3']:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)
                if choice == '1':
                    result = math.sin(radians)
                    print(f"sin({angle}) = {result:.4f}")
                elif choice == '2':
                    result = math.cos(radians)
                    print(f"cos({angle}) = {result:.4f}")
                elif choice == '3':
                    result = math.tan(radians)
                    print(f"tan({angle}) = {result:.4f}")
            elif choice == '4':
                num = float(input("Enter number for logarithm: "))
                if num > 0:
                    result = math.log(num)
                    print(f"log({num}) = {result:.4f}")
                else:
                    raise ValueError("Logarithm undefined for non-positive numbers!")
            elif choice == '5':
                num = float(input("Enter number for square root: "))
                if num >= 0:
                    result = math.sqrt(num)
                    print(f"sqrt({num}) = {result:.4f}")
                else:
                    raise ValueError("Cannot take square root of negative numbers!")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Unit conversion (temperature conversion for this example)
# Unit conversion section
def unit_conversion():
    print("\n--- Unit Conversion ---")
    while True:
        print("Choose a conversion category:")
        print("1. Temperature Conversion")
        print("2. Length Conversion")
        print("3. Weight Conversion")
        print("4. Speed Conversion")
        print("5. Volume Conversion")
        print("6. Area Conversion")
        print("7. Energy Conversion")
        print("8. Pressure Conversion")
        print("Type 'previous' to go back.")

        category = input("Your choice: ").strip().lower()

        if category == 'previous':
            return
        elif category == '1':
            temperature_conversion()
        elif category == '2':
            length_conversion()
        elif category == '3':
            weight_conversion()
        elif category == '4':
            speed_conversion()
        elif category == '5':
            volume_conversion()
        elif category == '6':
            area_conversion()
        elif category == '7':
            energy_conversion()
        elif category == '8':
            pressure_conversion()
        else:
            print("Invalid option! Please try again.")

# Temperature conversion
def temperature_conversion():
    print("\n--- Temperature Conversion ---")
    while True:
        choice = input("Type '1' for Celsius to Fahrenheit, '2' for Fahrenheit to Celsius, '3' for Celsius to Kelvin (or 'previous' to go back): ").strip()
        if choice == 'previous':
            return
        try:
            if choice == '1':
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}°C is {fahrenheit:.2f}°F")
            elif choice == '2':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5/9
                print(f"{fahrenheit}°F is {celsius:.2f}°C")
            elif choice == '3':
                celsius = float(input("Enter temperature in Celsius: "))
                kelvin = celsius + 273.15
                print(f"{celsius}°C is {kelvin:.2f}K")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Length conversion
def length_conversion():
    print("\n--- Length Conversion ---")
    while True:
        print("1. Meters to Feet\n2. Feet to Meters\n3. Kilometers to Miles\n4. Miles to Kilometers")
        print("5. Centimeters to Inches\n6. Inches to Centimeters\nType 'previous' to go back.")
        choice = input("Your choice: ").strip()

        if choice == 'previous':
            return
        try:
            if choice == '1':
                meters = float(input("Enter distance in meters: "))
                feet = meters * 3.28084
                print(f"{meters} meters is {feet:.2f} feet")
            elif choice == '2':
                feet = float(input("Enter distance in feet: "))
                meters = feet / 3.28084
                print(f"{feet} feet is {meters:.2f} meters")
            elif choice == '3':
                km = float(input("Enter distance in kilometers: "))
                miles = km * 0.621371
                print(f"{km} kilometers is {miles:.2f} miles")
            elif choice == '4':
                miles = float(input("Enter distance in miles: "))
                km = miles / 0.621371
                print(f"{miles} miles is {km:.2f} kilometers")
            elif choice == '5':
                cm = float(input("Enter length in centimeters: "))
                inches = cm / 2.54
                print(f"{cm} cm is {inches:.2f} inches")
            elif choice == '6':
                inches = float(input("Enter length in inches: "))
                cm = inches * 2.54
                print(f"{inches} inches is {cm:.2f} cm")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Weight conversion
def weight_conversion():
    print("\n--- Weight Conversion ---")
    while True:
        print("1. Kilograms to Pounds\n2. Pounds to Kilograms\n3. Grams to Ounces\n4. Ounces to Grams")
        print("Type 'previous' to go back.")
        choice = input("Your choice: ").strip()

        if choice == 'previous':
            return
        try:
            if choice == '1':
                kg = float(input("Enter weight in kilograms: "))
                pounds = kg * 2.20462
                print(f"{kg} kilograms is {pounds:.2f} pounds")
            elif choice == '2':
                pounds = float(input("Enter weight in pounds: "))
                kg = pounds / 2.20462
                print(f"{pounds} pounds is {kg:.2f} kilograms")
            elif choice == '3':
                grams = float(input("Enter weight in grams: "))
                ounces = grams / 28.3495
                print(f"{grams} grams is {ounces:.2f} ounces")
            elif choice == '4':
                ounces = float(input("Enter weight in ounces: "))
                grams = ounces * 28.3495
                print(f"{ounces} ounces is {grams:.2f} grams")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Speed conversion
def speed_conversion():
    print("\n--- Speed Conversion ---")
    while True:
        print("1. Kilometers per hour to Miles per hour\n2. Miles per hour to Kilometers per hour")
        print("Type 'previous' to go back.")
        choice = input("Your choice: ").strip()

        if choice == 'previous':
            return
        try:
            if choice == '1':
                kmph = float(input("Enter speed in kilometers per hour: "))
                mph = kmph * 0.621371
                print(f"{kmph} km/h is {mph:.2f} mph")
            elif choice == '2':
                mph = float(input("Enter speed in miles per hour: "))
                kmph = mph / 0.621371
                print(f"{mph} mph is {kmph:.2f} km/h")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Volume conversion
def volume_conversion():
    print("\n--- Volume Conversion ---")
    while True:
        print("1. Liters to Gallons\n2. Gallons to Liters\n3. Milliliters to Fluid Ounces\n4. Fluid Ounces to Milliliters")
        print("Type 'previous' to go back.")
        choice = input("Your choice: ").strip()

        if choice == 'previous':
            return
        try:
            if choice == '1':
                liters = float(input("Enter volume in liters: "))
                gallons = liters * 0.264172
                print(f"{liters} liters is {gallons:.2f} gallons")
            elif choice == '2':
                gallons = float(input("Enter volume in gallons: "))
                liters = gallons / 0.264172
                print(f"{gallons} gallons is {liters:.2f} liters")
            elif choice == '3':
                ml = float(input("Enter volume in milliliters: "))
                ounces = ml / 29.5735
                print(f"{ml} milliliters is {ounces:.2f} fluid ounces")
            elif choice == '4':
                ounces = float(input("Enter volume in fluid ounces: "))
                ml = ounces * 29.5735
                print(f"{ounces} fluid ounces is {ml:.2f} milliliters")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Area conversion
def area_conversion():
    print("\n--- Area Conversion ---")
    while True:
        print("1. Square meters to Square feet\n2. Square feet to Square meters\n3. Hectares to Acres\n4. Acres to Hectares")
        print("Type 'previous' to go back.")
        choice = input("Your choice: ").strip()

        if choice == 'previous':
            return
        try:
            if choice == '1':
                sqm = float(input("Enter area in square meters: "))
                sqft = sqm * 10.7639
                print(f"{sqm} square meters is {sqft:.2f} square feet")
            elif choice == '2':
                sqft = float(input("Enter area in square feet: "))
                sqm = sqft / 10.7639
                print(f"{sqft} square feet is {sqm:.2f} square meters")
            elif choice == '3':
                hectares = float(input("Enter area in hectares: "))
                acres = hectares * 2.47105
                print(f"{hectares} hectares is {acres:.2f} acres")
            elif choice == '4':
                acres = float(input("Enter area in acres: "))
                hectares = acres / 2.47105
                print(f"{acres} acres is {hectares:.2f} hectares")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Energy conversion
def energy_conversion():
    print("\n--- Energy Conversion ---")
    while True:
        print("1. Joules to Calories\n2. Calories to Joules\n3. Kilowatt-hours to Joules\n4. Joules to Kilowatt-hours")
        print("Type 'previous' to go back.")
        choice = input("Your choice: ").strip()

        if choice == 'previous':
            return
        try:
            if choice == '1':
                joules = float(input("Enter energy in joules: "))
                calories = joules / 4.184
                print(f"{joules} joules is {calories:.2f} calories")
            elif choice == '2':
                calories = float(input("Enter energy in calories: "))
                joules = calories * 4.184
                print(f"{calories} calories is {joules:.2f} joules")
            elif choice == '3':
                kwh = float(input("Enter energy in kilowatt-hours: "))
                joules = kwh * 3.6e6
                print(f"{kwh} kWh is {joules:.2f} joules")
            elif choice == '4':
                joules = float(input("Enter energy in joules: "))
                kwh = joules / 3.6e6
                print(f"{joules} joules is {kwh:.8f} kWh")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Pressure conversion
def pressure_conversion():
    print("\n--- Pressure Conversion ---")
    while True:
        print("1. Pascals to Atmospheres\n2. Atmospheres to Pascals\n3. Pascals to Bar\n4. Bar to Pascals")
        print("Type 'previous' to go back.")
        choice = input("Your choice: ").strip()

        if choice == 'previous':
            return
        try:
            if choice == '1':
                pascals = float(input("Enter pressure in pascals: "))
                atm = pascals / 101325
                print(f"{pascals} pascals is {atm:.6f} atmospheres")
            elif choice == '2':
                atm = float(input("Enter pressure in atmospheres: "))
                pascals = atm * 101325
                print(f"{atm} atmospheres is {pascals:.2f} pascals")
            elif choice == '3':
                pascals = float(input("Enter pressure in pascals: "))
                bar = pascals / 100000
                print(f"{pascals} pascals is {bar:.6f} bar")
            elif choice == '4':
                bar = float(input("Enter pressure in bar: "))
                pascals = bar * 100000
                print(f"{bar} bar is {pascals:.2f} pascals")
            else:
                raise ValueError("Invalid option!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


def main():
    user_guide()
    while True:
        print("\n--- Main Menu ---")
        print("1. Distance Conversion")
        print("2. Basic Calculations")
        print("3. Scientific Calculations")
        print("4. Unit Conversion")
        print("Type 'guide' to see the User Guide")
        print("Type 'previous' to go back")
        print("Type 'quit' to exit.")
        
        choice = input("Please select an option: ").strip().lower()
        if choice == '1':
            distance_conversion()
        elif choice == '2':
            basic_calculations()
        elif choice == '3':
            scientific_calculations()
        elif choice == '4':
            unit_conversion()
        elif choice == 'guide':
            user_guide()
        elif choice == 'previous':
            continue  # Let the user go back to the previous menu
        elif choice == 'quit':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
