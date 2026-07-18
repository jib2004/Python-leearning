def main():
    print("Hello World")
    print("Your BMI is:" ,bmi(100,180))
    print(celsius_to_fahrenheit(34))
    print(power_table(2,5))
    leapYear(1004)
    fileOpener()
    withdraw(100000, 5000000)

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

def leapYear(n):
    """
    divisible by 4
    Except centuries (100)
    unless that century is divisible by 400
    """
    if(n%4 == 0 and  n % 100 != 0 or n % 400 == 0):
        print("This is a leapYear")
    else:
        print("This is not a leapYear")


def grade(score):
    match score:
        case score if(score >= 90 and score <= 100) :
            print("A")
        case score if (score >= 80 and score < 90):
            print("B")
        case score if (score >= 70 and score < 80):
            print("C")
        case score if (score >= 60 and score < 70):
            print("D")
        case score if (60 > score and 0 <= score):
            print("F")
        case _:
            print("Invalid score")

def stringReverse(s):
    stringArr = list(s)
    stringArr.reverse()
    reverseStringFormat = "".join(stringArr)
    print(reverseStringFormat)

def stringReverseFor(s):
    stringArr = list(s)
    x = len(s)
    for i in range(len(stringArr)):
        print(f"{stringArr[x-1]}",end="")
        x-=1


def stringReverseFor2(s):
    reversed_text = ""
    for char in s:
        reversed_text = char + reversed_text

    print(reversed_text)

def fileOpener():
  try:
    open("data.txt","r")

  except FileNotFoundError:
    print("Cant find data.txt")
  else:
    print("Operation complete.")

def withdraw(balance,amount):
  try:
    if amount > balance:
      raise NameError("Insufficient Balance")
    print(f"Get your amount {amount}")
  except NameError:
    print("Inssuficient Balance")

if __name__ == '__main__':
    main()