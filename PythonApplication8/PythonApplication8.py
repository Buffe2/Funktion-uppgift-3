a = int(input("Nummer a?"))
b = int(input("Nummer b?"))
def maximum(a,b):
    if (a<b):
        print("B ar det storsta talet")
    elif (a>b):
        print("A ar det storsta talet")
    else:
        print("Talen ar lika stora")
maximum(a,b)
