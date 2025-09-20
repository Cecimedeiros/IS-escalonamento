from collections import deque

fila = deque([("P1", 5), ("P2", 7), ("P3", 3)])
quantum = 2

while fila:
    
    identificador, tempo = fila.popleft()
    tempo_executado = min(quantum, tempo)
    tempo -= tempo_executado
    
    print(f"{identificador} executou {tempo_executado} unidades (restam {tempo})")
    
    if tempo > 0:
        fila.append((identificador, tempo))
    
print(f"Todos os processos foram concluídos!")