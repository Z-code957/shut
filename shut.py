def shutd():
    a = input("Are the websites and aaps all closed(y/n):")
    if a == "y":
        print("SHUTING DOWN")
    elif a == "n":
        print("Sorry cannot shutdown")
    else:
        print("INVALID INPUT")
X = shutd()
print(X)