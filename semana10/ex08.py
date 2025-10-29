def converter_hora(hora, minuto):
    if hora == 0:
        return 12, minuto, "A.M."
    elif hora < 12:
        return hora, minuto, "A.M."
    elif hora == 12:
        return hora, minuto, "P.M."
    else:
        return hora - 12, minuto, "P.M."

def exibir_hora(h, m, periodo):
    print(f"{h}:{m:02d} {periodo}")

# Programa principal
hora = int(input("Digite a hora (0–23): "))
minuto = int(input("Digite os minutos (0–59): "))

h, m, p = converter_hora(hora, minuto)
exibir_hora(h, m, p)
