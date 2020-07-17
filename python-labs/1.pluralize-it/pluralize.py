''' level1
num = int(input("Plz input number: "))
animal = input("Plz input animal: ")

if num < 2:
    print("in: %d" % num)
    print("in: %s" % animal)
    print("out: %d %s" % (num, animal))
else:
    print("in: %d" % num)
    print("in: %s" % animal)
    print("out: %d %ss" % (num, animal))
'''
while True:
    word = input("Plz input word: ")
    if word != "the end":
        if word[-3:] == "ife":
            print(word[:-3] + "ives")

        elif word[-2:] == "sh":
            print(word[:-2] + "shes")

        elif word[-2:] == "ch":
            print(word[:-2] + "ches")

        elif word[-2:] == "us":
            print(word[:-2] + "i")

        elif word[-2:] == "ay":
            print(word[:-2] + "ays")

        elif word[-2:] == "ay":
            print(word[:-2] + "ays")

        elif word[-2:] == "oy":
            print(word[:-2] + "oys")

        elif word[-2:] == "ey":
            print(word[:-2] + "eys")

        elif word[-2:] == "uy":
            print(word[:-2] + "uys")

        elif word[-1:] == "y":
            print(word[:-1] + "ies")

        else:
            print(word + "s")

    if word == "the end":
        break