def roman_to_integer(roman: str) -> int:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    length = len(roman)

    for i in range(length):
        current_value = roman_values[roman[i]]
        
        if i < length - 1 and current_value < roman_values[roman[i + 1]]:
            total -= current_value
        else:
            total += current_value

    return total

print(roman_to_integer("MCMXCIV"))  
print(roman_to_integer("LVIII"))    
print(roman_to_integer("IX"))       
