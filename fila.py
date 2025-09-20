from queue import Queue

fila = Queue()

fila.put("Cecília")
fila.put("Júlia")
fila.put("Eliza")
fila.put("Izabel")
fila.put("Luciano")

for i in fila.queue:
    print(i)

print(fila.queue)