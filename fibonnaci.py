# Classe de sequencia em fibonnaci
def fibonnaci(quantidade_num):
    pass

    total = list(range(quantidade_num))
    novo_array = []

    dados_array = total[0:3]

    for num in dados_array:

        if num == 0:
            novo_array.append(0)
        if num == 1:
                novo_array.append(1)
        if num == 2:
                novo_array.append(1)
    
    while len(novo_array) < quantidade_num:
        proximo = novo_array[-1] + novo_array[-2]
        novo_array.append(proximo)

    return novo_array

quantidade_num = 10

result = fibonnaci(quantidade_num)
print(result)

#comentarios referentes a lista de fibonnaci: 
#novo_array[-1], e novo_array[-2]: Pega os números anteriores da sequencia e soma os dois. Último número depois o antepenúltimo
