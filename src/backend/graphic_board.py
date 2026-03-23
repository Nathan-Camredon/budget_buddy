import matplotlib.pyplot as plt

class GraphicBoard:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def draw_stackplot(self, x, y, labels=None, title="Revenus du compte", xlabel="Temps", ylabel="Montant", show=True):
        """
        Displays a stackplot-type graph.
        x: X-axis data (e.g., dates or indices).
        y: Y-axis data (can be a list of lists for stacking).
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