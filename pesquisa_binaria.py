class Busca:
    '''Classe que implementa busca binária'''
    def binary_search(lista, item):
        '''
        Esta função realiza uma busca binária
        
        Args: 
        lista - Lista de itens
        item - item que deseja encontrar

        retorno:
        int:
        Indice do item

        '''
        baixo =0
        alto = len(lista) -1
        steps =0

        while baixo <= alto:
            print("steps", steps)
            meio = int((baixo + alto) / 2)
            print("Meio: ",meio)
            chute = lista[meio]
            if chute == item:
                return meio
            if chute > item:
                alto = meio -1
                print("alto: ", alto)
            else:
                baixo = meio +1
                print("baixo:", baixo)
            steps =steps+1
        return None
