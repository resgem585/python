def voltear_texto(texto):
    texto_revertido = ''
    for i in range(len(texto) - 1, -1, -1):
        texto_revertido += texto[i]
    return texto_revertido

texto = ' Bienvenidos a python'
texto_revertido = voltear_texto(texto)
print(texto_revertido)