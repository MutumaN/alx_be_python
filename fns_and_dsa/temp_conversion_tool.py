# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature converted to Celsius
    """
    # No need for global keyword since we're only reading (not modifying) the global variable
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature converted to Fahrenheit
    """
    # No need for global keyword since we're only reading (not modifying) the global variable
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction and temperature conversion
    """
    try:
        # Get temperature input from user
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Get temperature unit from user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform conversion based on unit
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()