def classificar_problema(texto):
    """
    Classifica um problema técnico baseado em palavras-chave.
    
    Args:
        texto (str): Descrição do problema técnico
        
    Returns:
        dict: Dicionário com a categoria do problema identificado
    """
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
