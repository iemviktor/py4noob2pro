import json

number = 0
filename = "number.json"
inp = input("Input your favourite number: ")
try:
    number = int(inp)
except:
    print("Invaliad input. Nothing written to number.json")
else:
    with open(filename, "w") as f:
        json.dump(number, f)

    with open(filename, "r") as f:
        read = json.load(f)
        print(f"Json: {read}")
    print(f"Your favourite number is {inp}. Written to number.json")
