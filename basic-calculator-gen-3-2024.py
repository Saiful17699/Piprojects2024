import math

def user_guide():
    print("\n--- User Guide ---")
    print("1. Distance Conversion: Convert kilometers to miles or vice versa.")
    print("2. Basic Calculations: Perform addition, subtraction, multiplication, and division.")
    print("3. Scientific Calculations: Trigonometric functions (sin, cos, tan), logarithms, square root, etc.")
    print("4. Unit Conversion: Convert between different units (temperature, length, etc.).")
    print("5. Type 'quit' to exit the program.")
    print("--------------------\n")

# Distance conversion (km to miles and vice versa)
def distance_conversion():
    print("\n--- Distance Conversion ---")
    choice = input("Type '1' to convert kilometers to miles, '2' for miles to kilometers: ").strip()
    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is {miles:.2f} miles")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        km = miles / 0.621371
        print(f"{miles} miles is {km:.2f} kilometers")
    else:
        print("Invalid option!")

# Basic calculations
def basic_calculations():
    print("\n--- Basic Calculations ---")
    operation = input("Enter the operation (+, -, *, /): ").strip()
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
                result = "undefined (cannot divide by zero)"
        else:
            result = "Invalid operation!"
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input!")

# Scientific calculations
def scientific_calculations():
    print("\n--- Scientific Calculations ---")
    print("Choose an option:")
    print("1. Sin\n2. Cos\n3. Tan\n4. Logarithm\n5. Square Root")
    choice = input("Your choice: ").strip()

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
                print("Logarithm undefined for non-positive numbers!")
        elif choice == '5':
            num = float(input("Enter number for square root: "))
            if num >= 0:
                result = math.sqrt(num)
                print(f"sqrt({num}) = {result:.4f}")
            else:
                print("Cannot take square root of negative numbers!")
        else:
            print("Invalid option!")
    except ValueError:
        print("Invalid input!")

# Unit conversion (temperature conversion for this example)
def unit_conversion():
    print("\n--- Unit Conversion ---")
    choice = input("Type '1' for Celsius to Fahrenheit, '2' for Fahrenheit to Celsius: ").strip()
    try:
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        else:
            print("Invalid option!")
    except ValueError:
        print("Invalid input!")

def main():
    user_guide()
    while True:
        print("\n--- Main Menu ---")
        print("1. Distance Conversion")
        print("2. Basic Calculations")
        print("3. Scientific Calculations")
        print("4. Unit Conversion")
        print("Type 'guide' to see the User Guide")
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
        elif choice == 'quit':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
