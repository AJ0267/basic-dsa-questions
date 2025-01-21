# Convert digits/numbers to words. 

def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n == 0:
        return "Zero"
    
    if n < 20:
        return ones[n]
    
    if n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        else:
            return tens[n // 10] + ' ' + ones[n % 10]

    else:  # n < 1000
        if n % 100 == 0:
            return ones[n // 100] + " Hundred"
        else:
            return ones[n // 100] + " Hundred and " + number_to_words(n % 100)


print(number_to_words(123))
