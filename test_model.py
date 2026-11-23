
from model.model import Model

model = Model()
luoghi = model.get_luoghi()
for luogo in luoghi:
    print(luogo)
