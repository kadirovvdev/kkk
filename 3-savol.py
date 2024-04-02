with open("data.txt", "r") as file:
    a = int(input("Son kiriting"))
    s = [int(i.strip()) for i in file.readlines()[:a]]

    x1 = max(s)
    x2 = min(s)
    print(x1+x2)


