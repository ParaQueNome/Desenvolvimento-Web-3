"Estrutura de dados em Python"

"Listas: "
lista = ['Notebook','mouse', 'teclado','Mousepad',12,['nobreak','projetor'],'teste']


for i in range(len(lista)):
    if isinstance(lista[i],str):
        print(lista[i])

"Conjuntos: "
conjunto = {1,2,3,4,5,6}
conjunto1 = {1,2,3,4,5,6,7,8,9,10}
conjunto2 = set(range(1,11))

conjunto.add(7)

conjunto.remove(7)

conjunto.discard(7)

conjunto.pop()

conjunto.clear()

conjunto.union(conjunto1)

conjunto.intersection(conjunto1)

conjunto.difference(conjunto1)

conjunto.symmetric_difference(conjunto1)

"Dicionários: "

dicionario = {"nome":"Gabriel" , "idade":20}

dicionario["nome"] = "Gabriel"

dicionario["idade"] = 20

dicionario["idade"] = 20

dicionario["sexo"] = "M"

dicionario["peso"] = 85.5

