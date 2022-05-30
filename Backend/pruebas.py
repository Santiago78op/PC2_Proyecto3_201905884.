import matplotlib.pyplot as plt
import numpy as np 

def imageRango():
    x = np.arange(5) 
    y1 = [34, 56, 12, 89, 67] 
    y2 = [12, 56, 78, 45, 90] 
    y3 = [14, 23, 45, 25, 89] 
    width = 0.2
    
    plt.title('Reporte de Ventas')
    plt.bar(x-0.2, y1, width, color='skyblue') 
    plt.bar(x, y2, width, color='brown') 
    plt.bar(x+0.2, y3, width, color='green') 
    plt.xticks(x, ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']) 
    plt.xlabel("Teams") 
    plt.ylabel("Scores") 
    plt.legend(["Round 1", "Round 2", "Round 3"]) 
    plt.savefig('Backend/saved_figure.png')

grafica = imageRango()
