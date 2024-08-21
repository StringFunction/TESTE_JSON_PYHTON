import json
pessoa = {
    "nome" : "conde",
    "senha"  : "12331"
}
with open("teste.json", "r") as file:
    dados = json.load(file)


for tes in dados["Dados"] :
    print(tes)

dados["Dados"].append(pessoa)
with open("teste.json", "w") as conde:
    json.dump(dados, conde,indent=4)
