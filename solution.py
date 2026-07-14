def main():
    print("Hello World")
    print("Your BMI is:" ,bmi(100,180))
    print(celsius_to_fahrenheit(34))
    print(power_table(2,5))

def bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def celsius_to_fahrenheit(c):
    return round((c * 1.8) + 32,2)

def power_table(base, limit):
    b = []
    for i  in range(limit):
        t = base ** (i + 1)
        b.append(t)
    result = ", ".join(str(num) for num in b) # if a number
    return result


if __name__ == '__main__':
    main()