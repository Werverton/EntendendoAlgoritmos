from pesquisa_binaria import Busca

def gera_lista():
    inicio = 1
    diferenca = 2

# Criando a lista
    lista = [inicio]
    for _ in range(1, 300):
        inicio += diferenca
        lista.append(inicio)
    return lista

minhaBusca= Busca

lista =gera_lista()
resultado = minhaBusca.binary_search(lista, 299)

print(resultado)