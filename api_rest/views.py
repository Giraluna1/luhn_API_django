from django.http.request import HttpHeaders
from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.

def hello(request):
    """ This is the home view """
    message = """
    HELLO WHALE & JAGUARS
    Please put your credit card number into the browser bellow "/".
    EXAMPLE:
    http://0.0.0.0:8000/4444 4444 4444 4444
    and you will check if is valid and what type of franchise credit card is
    """
    return HttpResponse(message)

def checkLuhn(credit_card_number):
    """ This functyion check if a credit card is valid using the Luhn Algorithm
    ARGS: credit_card_number(str): the number to verify
    """

    #delte the spaces
    number_clean = credit_card_number.replace(" ", "")

    # set the digits of the number and auxiliar flag
    digits = len(number_clean)
    addition = 0
    flag = False

    # we run trhoug the string of numbers from the
    # penultim number to the first number and 
    for i in range(digits-1, -1, -1):
        digit = ord(number_clean[i]) - ord('0')

        if flag == True:
            digit = digit * 2

        # add two digits
        addition += digit // 10
        addition += digit % 10

        flag = not flag

    if addition % 10 == 0:
        return True
    else:
        return False



def franchise(request, number):
    check = checkLuhn(number)
    print(check)
    if check == True:

        franchises = {
            "visa": '^4[0-9]{12}(?:[0-9]{3})?$',
            "electron": '^(4026|417500|4405|4508|4844|4913|4917)\d+$',
            "maestro": '^(5018|5020|5038|5612|5893|6304|6759|6761|6762|6763|0604|6390)\d+$',
            "american express": '^3[47][0-9]{13}$',
            "diners club": '^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
            "mastercard": '^5[1-5][0-9]{5,}|222[1-9][0-9]{3,}|22[3-9][0-9]{4,}|2[3-6][0-9]{5,}|27[01][0-9]{4,}|2720[0-9]{3,}$',
            "discover": '^6(?:011|5[0-9]{2})[0-9]{12}$',
            "jcb": '^(?:2131|1800|35\d{3})\d{11}$'
        }
        PAN = number.replace(" ", "")
        for key, value in franchises.items():
            if re.match(value, PAN):
                return HttpResponse("<h1> El numero de tarjeta es valido y la franquicia es: {}<h1>".format(key.upper()))
    else:
        return HttpResponse("NO ES UNA TARJETA VALIDA")