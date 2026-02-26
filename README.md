def classificar_problema(texto): 
    texto = texto.lower()
if "valvula" in texto:
   return {"categoria": "Falha em válvula"}
        elif "pressao" in texto:
        return {"categoria": "Problema de pressão"}
else:
        return {"categoria": "Não identificado"}


if __name__ == "__main__":
    entrada = input("Descreva o problema técnico: ")
    resultado = classificar_problema(entrada)
    print("Resultado:", resultado)
