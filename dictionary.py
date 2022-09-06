data = {
    "speak": "kotha bola",
    "school": "biddaloi",
    "book": "boi",
    "fruit": "fol",
    "watermelon": "tormuj",
    "watch": "ghori",
    "time": "somoi",
    "work": "kaj",
    "name": "nam",
    "study": "poralekha",
    "test": "porikkha",
    "exam": "porikkha",
    "do": "kora",
    "friend": "bondhu",
    "do word": "kaj kora",
    "job": "chakri",
    "face": "mukh",
    "tree": "gach",
    "house": "bari",
    "enemy": "shotru"
}
def search(word):
    items = data.items()

    result = []
    for x, y in items:
        if (word in x):
            result.append(y)
        elif (word in y):
            result.append(x)

    if (len(result) < 1):
        return "UNKNOWN ERROR!"
    else:
        return ", ".join(result)

print("please select one of this:")
print("1. English to Bengala")
print("2. Bengala to English")
while True:
    choice = int(input("enter your choice here(1/2): "))
    if (choice ==1):
        searchInput = str(input(("English : ")))
        print("Bangla: ", search(searchInput))
    elif (choice == 2):
        searchInput = str(input(("Bengali: ")))
        print("English: ", search(searchInput))
    else:
        print("sorry, you have entered the wrong option")
