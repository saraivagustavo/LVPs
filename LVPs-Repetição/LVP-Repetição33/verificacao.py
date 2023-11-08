def f_verificaLetra(letra, texto):
    for i in range(len(texto)):
        if(letra == texto[i]):
            return True
    return False