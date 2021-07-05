# visualização de dados em python
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 250, 400, 330, 100]

#x1 = [1, 3, 5, 7, 9]
#y1 = [2, 3, 7, 1, 0]

#x2 = [2, 4, 6, 8, 10]
#y2 = [5, 1, 3, 7, 4]

titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="meus pontos", color="k", marker=".", s=z)
plt.plot(x, y, color="#000000", linestyle="--")
plt.legend()

#plt.bar(x1, y1, label = "Grupo 1")
#plt.bar(x2, y2, label = "Grupo 2")
#plt.legend()
#plt.show()
#plt.savefig("figura1.pdf")
plt.savefig("figure2.png", dpi=300)