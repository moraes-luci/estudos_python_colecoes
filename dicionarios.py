def imprimePaises(sigla):
    paises = {"sigla": ["BRA", "EUA", "JPN", "CHN"],
              "nome": ["Brasil", "Estados Unidos", "Japão", "China"],
              "capital": ["Brasilia", "Whashington", "Tokyo", "Pequim"]}

    indice = paises["sigla"].index(sigla)
    return f"""País: {paises['nome'][indice]} 
Sigla: {sigla} 
Capital: {paises['capital'][indice]}"""


sigla = input("Informe a Sigla: ").upper()
print()

try:
    print(imprimePaises(sigla))
except ValueError:
    print(f"<< Não existe a sigla {sigla} na lista! >>")
