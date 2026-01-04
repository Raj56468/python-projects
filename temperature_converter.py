def temperature_converter():
    ask = input("Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F)? ").strip().upper()
    if ask == "C":
        celsius_input = float(input("Enter temperature in Celsius: "))
        fahrenheit_output = (celsius_input * 9/5) + 32
        print(f"{celsius_input}°C is {fahrenheit_output}°F")
    elif ask == "F":
        fahrenheit_input = float(input("enter temperature in Fahrenheit: "))
        celsius_output = (fahrenheit_input - 32) * 5/9
        print(f"{fahrenheit_input}°F is {celsius_output}°C")
    else:
        print("Invalid option! Please enter 'C' or 'F'.")


if __name__ == "__main__":
    temperature_converter()
