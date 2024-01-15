def convert_base(number, base, base2):
    numberin10 = int(number, base)
    result = ''
    if base2 == 16:
        while numberin10 > 0:
            if numberin10 % base2 == 10:
                result = "A" + result
            elif numberin10 % base2 == 11:
                result = "B" + result
            elif numberin10 % base2 == 12:
                result = "C" + result
            elif numberin10 % base2 == 13:
                result = "D" + result
            elif numberin10 % base2 == 14:
                result = "E" + result
            elif numberin10 % base2 == 15:
                result = "F" + result
            else:
                result = str(numberin10 % base2) + result
            numberin10 //= base2
    while numberin10 > 0:
        result = str(numberin10 % base2) + result
        numberin10 //= base2
    return result


def choose():
    base = int(input("Choose a base: "))
    number1 = input("Choose a number: ")
    base2 = int(input("Choose a base to convert to: "))
    score = convert_base(number1, base, base2)
    print(score)
    print("Chcesz kontynuowac? y/n")
    if input() == "y":
        choose()
    else:
        print("Bye bye :D")
print("Hello there :D, program na matme be like")
choose()




