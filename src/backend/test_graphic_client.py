import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import matplotlib.pyplot as plt
from src.backend.graphic_board import GraphicBoard

def run_test():
    # Instanciation de la classe
    board = GraphicBoard()
    
    # Données de test
    indices = [1, 2, 3, 4, 5]
    revenus_sources = [
        [100, 150, 120, 180, 200], # Source A
        [50, 80, 60, 90, 110],     # Source B
        [30, 40, 35, 50, 60]       # Source C
    ]
    labels = ["Salaire", "Pot-de-vin", "Cadeaux"]
    
    print("Génération du graphique...")
    # Appel de la méthode draw_stackplot (show=True par défaut)
    board.draw_stackplot(indices, revenus_sources, labels=labels)

if __name__ == "__main__":
    run_test()
