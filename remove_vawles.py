vowles = ['A','E','I','O','U','a','e','i','o','u']
def rmvvls(word):
    vls = ""
    for i in word:
        if(i not in vowles):
            vls = vls + i
            return vls
        while True:
            user = input("Enter your text here: ")
            lenth = len(user)
            if(lenth<10):
                print()
            elif(lenth>20):
                print()
            else:
                print('great your text (",str,")is','text long')
                print('whithout vowles the text is:',rmvvls(user))
