import matplotlib.pyplot as plt

class GraphicBoard:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def draw_stackplot(self, x, y, labels=None, title="Revenus du compte", xlabel="Temps", ylabel="Montant", show=True):
        """
        Affiche un graphique de type stackplot.
        x: Les données de l'axe X (ex: dates ou indices).
        y: Les données de l'axe Y (peut être une liste de listes pour empiler).
        """
        self.ax.clear()
        self.ax.stackplot(x, y, labels=labels)
        if labels:
            self.ax.legend(loc='upper left')
        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        if show:
            plt.show()