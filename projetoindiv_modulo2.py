# lista para armazenar os resultados
resultado=[]
# Dicionário 
candidatos = {
"Candidato 1": {
"Entrevista":("e",5),
"Técnica":("t",10),
"Prática":("p",8),
"Soft Skill":("s",8)
},
"Candidato 2": {
"Entrevista":("e",10),
"Técnica":("t",7),
"Prática":("p",7),
"Soft Skill":("s",8)
},
"Candidato 3": {
"Entrevista":("e",8),
"Técnica":("t",5),
"Prática":("p",4),
"Soft Skill":("s",9)
},
"Candidato 4": {
"Entrevista":("e",2),
"Técnica":("t",2),
"Prática":("p",2),
"Soft Skill":("s",1)
},
"Candidato 5": {
"Entrevista":("e",10),
"Técnica":("t",10),
"Prática":("p",8),
"Soft Skill":("s",9)
}
}

# Função que busca o candidato 
def requisito_vaga():
    print("Insira os requisitos mínimos que você está buscando:")
    requisitos = [int(input("Entrevista: ")),int(input("Técnica: ")), int(input("Prática: ")), int(input("Soft Skill: "))]
    resultado.append(requisitos)
    return requisitos

def buscar_candidatos(requisitos):
    candidatos_compativeis = []

    for candidato, habilidades in candidatos.items():
        atende_requisitos = all(habilidades[chave][1] >= requisito for chave, requisito in zip(habilidades.keys(), requisitos))

        if atende_requisitos:
            candidatos_compativeis.append(candidato)

    return candidatos_compativeis

requisitos = requisito_vaga()
candidatos_compativeis = buscar_candidatos(requisitos)

print("Candidatos compatíveis com os requisitos mínimos solicitados:")
for candidato in candidatos_compativeis:
    print(candidato)