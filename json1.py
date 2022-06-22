import json
import random

#data = {"crack coca":10, "amphe":12, "lsd":14}
data = [random.randint(1,100) for i in range(20)]
with open("data.json", "w") as file:
    json.dump(data, file)

read_data = []
with open("data.json") as file:
    read_data = json.load(file)
print(read_data)
