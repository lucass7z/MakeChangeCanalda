from tabulate import tabulate
import time
m = 12.35
with open('L.txt', 'r') as file:
    L = [float(num) for line in file for num in line.strip().split(',')]

def calculate1(m, L):
    S_Fifo = []
    for coin in L:
        count = int(m // coin)
        S_Fifo.append((coin, count)) 
        m -= coin * count
        m = round(m, 2)
    return S_Fifo
solution = calculate1(m, L)
headers = ["Coin", "Quantity"]
print(tabulate(solution, headers, tablefmt="pretty"))



#2a


S_fifo = []
# Variable globale pour compter le nombre de solutions trouvées
solution_count = 0

def RestartCalculate(L, m, i, S_fifo):
    global solution_count
    
    # Arrondi m à 2 décimales pour éviter les erreurs de précision
    m = round(m, 2)
    
    if m == 0:
        print(f"Solution trouvée : {S_fifo}")
        solution_count += 1 
        return
    
    
    elif i >= len(L):
        return  # Pas de solution
    
    else:
        for j in range(int(m / L[i]) + 1):
            S_fifo.append(j)
            RestartCalculate(L, m - j * L[i], i + 1, S_fifo)
            S_fifo.pop() 

# Lancer l'algorithme et un timer
start_time = time.time()
RestartCalculate(L, m, 0, S_fifo)
end_time = time.time()
if(solution_count == 0):
    print("Aucune solution trouvée")
else:
    print(f"L'algorithme a trouvé {solution_count} combinaisons. Ceci en {round(end_time - start_time,2)} secondes.")