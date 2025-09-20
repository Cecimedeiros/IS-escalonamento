from queue import PriorityQueue

filaBanco = PriorityQueue()

alta = 1
media = 2
baixa = 3

filaBanco.put((alta, "Cecília"))
filaBanco.put((media, "Júlia"))
filaBanco.put((media, "Conrad"))
filaBanco.put((baixa, "Eliza"))
filaBanco.put((media, "Belly"))
filaBanco.put((alta, "Jeremiah"))
filaBanco.put((baixa, "Izabel"))
filaBanco.put((baixa, "Bonnie"))
filaBanco.put((baixa, "Jacob"))
filaBanco.put((alta, "Ana"))
filaBanco.put((alta, "Estevão"))
filaBanco.put((media, "Felipe"))
filaBanco.put((alta, "Luciano"))
filaBanco.put((media, "Crislayne"))
filaBanco.put((baixa, "Carla"))

while not filaBanco.empty():
    prioridade, cliente = filaBanco.get()
    print(f"Prioridade: {prioridade} - {cliente}")

