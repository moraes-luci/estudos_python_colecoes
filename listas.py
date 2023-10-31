numeros = []
pares = []
impares = []

for num in range(101):
    numeros.append(num)

for item in numeros:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print(f"""Lista inicial {numeros}
números pares {pares}
números impares {impares}""")