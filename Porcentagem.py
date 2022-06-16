listaLocais = [["São Paulo", 67836.43], ["Rio de Janeiro", 36678.66], ["Minas Gerais", 29229.88], ["Espírito Santo", 27165.48], ["Outros", 19849.53]]

somaTotal = 0

for i in range(5):
    somaTotal = somaTotal + listaLocais[i][1]

for j in range(5):
    porcentagem = (listaLocais[j][1] / somaTotal) * 100

    print(listaLocais[j][0] + ": " + str(porcentagem) + "%")