import matplotlib.pyplot as plt

class GenerateGraficoHelper:

    @staticmethod
    def generateGrafico(
        size=(8,4),
        x=None,
        y=None,
        color="skyblue",
        title="",
        labelX="",
        labelY="",
        labelMain="",
        width=0.6,

        # Extra bar (opcional)
        extra=False,
        x_extra=None,
        y_extra=None,
        labelExtra="",
        colorExtra="orange",

        # Ticks
        ticks=None,
        ticks_labels=None,

        showLegend=True
    ):
        plt.figure(figsize=size)

        # Barra principal
        plt.bar(x, y, width=width, color=color, label=labelMain)

        # Barra extra
        if extra and x_extra is not None and y_extra is not None:
            plt.bar(x_extra, y_extra, width=width, color=colorExtra, label=labelExtra)

        # Configuração dos ticks
        if ticks and ticks_labels:
            plt.xticks(ticks, ticks_labels)

        plt.title(title)
        plt.xlabel(labelX)
        plt.ylabel(labelY)

        # Legenda
        if showLegend and (labelMain or labelExtra):
            plt.legend()

        plt.tight_layout()
        plt.show()
