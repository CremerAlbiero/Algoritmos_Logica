matriz = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        elemento = int(input(f"Digite o numero {i+1},{j+1}: "))
        matriz[i][j] = elemento


print(f"1,1 = {matriz[0][0]}")
print(f"1,2 = {matriz[0][1]}")
print(f"2,1 = {matriz[1][0]}")
print(f"2,2 = {matriz[1][1]}")