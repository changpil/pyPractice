def digits(num):
    d = 1
    while num > 10:
        num = num // 10
        d *= 10
    return d

DigitToWord = { 0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                17: "seventeen", 18:"eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
                70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand", 1000000: "million",
                1000000000: "billion"}

def underThrousandsWords(num):
    w = ""
    while num:
        if 100 <= num < 1000:
            d, r = divmod(num, 100)
            w += DigitToWord[d] + " " + DigitToWord[100]
            num = r
        elif 20 <= num < 100:
            d, r = divmod(num, 10)
            w += " " + DigitToWord[d * 10] + " " + DigitToWord[r]
            break
        elif num < 20:
            w += " " + DigitToWord[num]
            break
    return " ".join(w.split())

def numberToWords(num):

    w = ""
    while num:
        if 1000000000 <= num < 1000000000000:
            d, r = divmod(num, 1000000000)
            w += underThrousandsWords(d) + " " + DigitToWord[1000000000]
            num = r

        elif 1000000 <= num < 1000000000:
            d, r = divmod(num, 1000000)
            w += underThrousandsWords(d) + " " + DigitToWord[1000000]
            num = r
        elif 1000 <= num < 1000000:
            d, r = divmod(num, 1000)
            w += " " + underThrousandsWords(d) + " " + DigitToWord[1000]
            num = r
        elif 1 <= num < 1000:
            w += " " + underThrousandsWords(num)
            break
    return w.strip()

print(numberToWords(21))
print(numberToWords(320))
print(numberToWords(1000))
print(numberToWords(1111))
print(numberToWords(11111111118))