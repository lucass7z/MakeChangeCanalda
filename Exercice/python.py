from tabulate import tabulate
import time
import math
m = 12.35

#On utilise le fichier L.txt pour lire les valeurs de L [coins1, coins2, ...]
with open('Exercice/L.txt', 'r') as file:
    L = [float(num) for line in file for num in line.strip().split(',')]

#1 GreedyOrdered
def calculate1(m, L):
    S_Fifo = []
    for coin in L:
        count = int(m // coin)
        S_Fifo.append((coin, count)) 
        m -= coin * count
        m = round(m, 2)
    return S_Fifo
def greedyOrdered():
    solution = calculate1(m, L)
    headers = ["Coin", "Quantity"]
    print(tabulate(solution, headers, tablefmt="pretty"))


#2a Recursive dynamic programming


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


def recursiveAll():
    # Lancer l'algorithme et un timer
    start_time = time.time()
    RestartCalculate(L, m, 0, S_fifo)
    end_time = time.time()
    if(solution_count == 0):
        print("Aucune solution trouvée")
    else:
        print(f"L'algorithme a trouvé {solution_count} combinaisons. Ceci en {round(end_time - start_time,2)} secondes.")
    

#2b Recursive dynamic programming Best solution only

S_fifo = []
solution_count = 0
bestSolution = ""
bestSolutionCoinsCount = math.inf
def RestartCalculate2b(L, m, i, S_fifo):
    global solution_count
    global bestSolution
    global bestSolutionCoinsCount
    
    # Arrondi m à 2 décimales pour éviter les erreurs de précision
    m = round(m, 2)
    
    if m == 0:
        #Compter le nombre de coins
        coinsCount = 0
        for coin in S_fifo:
            coinsCount += coin
        if(coinsCount < bestSolutionCoinsCount):
            bestSolutionCoinsCount = coinsCount
            bestSolution = S_fifo.copy()
        solution_count += 1 
        return
    
    
    elif i >= len(L):
        return  # Pas de solution
    
    else:
        for j in range(int(m / L[i]) + 1):
            S_fifo.append(j)
            RestartCalculate2b(L, m - j * L[i], i + 1, S_fifo)
            S_fifo.pop() 

def recursiveBest():
    # Lancer l'algorithme et un timer
    start_time = time.time()
    RestartCalculate2b(L, m, 0, S_fifo)
    end_time = time.time()
    if(solution_count == 0):
        print("Aucune solution trouvée")
    else:
        print(f"L'algorithme a trouvé {solution_count} combinaisons. Ceci en {round(end_time - start_time,2)} secondes. La meilleure solution est :")
        solutions = []
        for i in range(len(bestSolution)):
            solutions.append((L[i], bestSolution[i]))
        headers = ["Coin", "Quantity"]
        print(tabulate(solutions, headers, tablefmt="pretty"))
        
# 3 Recursive dynamic programming at new Best solution 
S_fifo = []
solution_count = 0
bestSolution = ""
bestSolutionCoinsCount = math.inf
def RestartCalculate3(L, m, i, S_fifo):
    global solution_count
    global bestSolution
    global bestSolutionCoinsCount
    
    # Arrondi m à 2 décimales pour éviter les erreurs de précision
    m = round(m, 2)
    
    if m == 0:
        #Compter le nombre de coins
        coinsCount = 0
        for coin in S_fifo:
            coinsCount += coin
        if(coinsCount < bestSolutionCoinsCount):
            bestSolutionCoinsCount = coinsCount
            bestSolution = S_fifo.copy()
            print(f"Nouvelle meilleure solution : {bestSolution}")
        solution_count += 1 
        return
    
    
    elif i >= len(L):
        return  # Pas de solution
    
    else:
        for j in range(int(m / L[i]) + 1):
            S_fifo.append(j)
            RestartCalculate3(L, m - j * L[i], i + 1, S_fifo)
            S_fifo.pop() 

def cutAndPriceAndShare():
    # Lancer l'algorithme et un timer
    start_time = time.time()
    RestartCalculate3(L, m, 0, S_fifo)
    end_time = time.time()
    if(solution_count == 0):
        print("Aucune solution trouvée")
    else:
        print(f"L'algorithme a trouvé {solution_count} combinaisons. Ceci en {round(end_time - start_time,2)} secondes. La meilleure solution est :")
        solutions = []
        for i in range(len(bestSolution)):
            solutions.append((L[i], bestSolution[i]))
        headers = ["Coin", "Quantity"]
        print(tabulate(solutions, headers, tablefmt="pretty"))



def main():
    choice = input("Choisissez l'algorithme à utiliser :")
    try:
        choice = int(choice)
        if(choice < 1 or choice > 4):
            print("Veuillez entrer un nombre entre 1 et 4")
            main()
        if(choice == 1):
            greedyOrdered()
        elif(choice == 2):
            recursiveAll()
        elif(choice == 3):
            recursiveBest()
        elif(choice == 4):
            cutAndPriceAndShare()
    except:
        print("Veuillez entrer un nombre valide")
        main()

if __name__ == "__main__":
    #recupérer le choix de l'utilisateur
    print("1. GreedyOrdered")
    print("2. Recursive dynamic programming print All solutions")
    print("3. Recursive dynamic programming print Best solution only")
    print("4. Recursive dynamic programming print at new Best solution")
    main()