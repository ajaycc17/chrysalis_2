from django.shortcuts import render
import random


def projectHome(request):
    return render(request, 'project/index.html')


def passGen(request):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                 'Z']
    special = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']
    collection = digits + uppercase + lowercase + special

    userInput = request.GET.get('strength')
    try:
        strn = int(userInput)
        if strn < 12:
            strn = 12

        elif strn > 100:
            strn = 100

        dig = random.choice(digits)
        low = random.choice(lowercase)
        up = random.choice(uppercase)
        sym = random.choice(special)

        rnd_char = []
        rnd_char.append(dig)
        rnd_char.append(low)
        rnd_char.append(up)
        rnd_char.append(sym)

        for i in range(strn-4):
            rnd_char.append(random.choice(collection))

        random.shuffle(rnd_char)
        password = ""
        for j in rnd_char:
            password = password + j

    except:
        password = ""

    context = {'password': password}
    return render(request, 'project/passwordGenerator.html', context)
