"""
hexcolor.py
A program that converts RGB values from decimal to hex.
Only uses native python functions.
Author: Anderson Hsiao
Date: 2021-08-09
"""

def main():
    result = ""
    
    # Only accept inputs from 0 to 255 for all 3 colors
    for color in ["Red", "Green", "Blue"]:
        num = -1
        while not 0 <= num <= 255:
            num = int(input(f"{color}: "))
        result += dec_to_hex(num)

    print(f"Result: {result}")

# Converts a number from decimal to hex
def dec_to_hex(n):
    result = ""

    # Determine first digit
    current_digit = n // 16
    result += determine_digit(current_digit)

    # Determine second digit
    current_digit = n % 16
    result += determine_digit(current_digit)
    
    return result

# Takes in a decimal number, returns the corresponding hexadecimal digit as a string
def determine_digit(n):
    if n < 10:
        return str(n)
    else:
        n -= 10
        return chr(65 + n) # 65 is the ASCII value for 'A'

if __name__ == '__main__':
    main()