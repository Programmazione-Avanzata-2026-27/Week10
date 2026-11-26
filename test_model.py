from model.model import Model

model = Model()
luoghi = model.get_luoghi()
for luogo in luoghi:
    print(luogo)


model.crea_grafo() # Crea il grafo in model.grafo
print(model.grafo)


