def tipo_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "VLAN de rango NORMAL"
    elif 1006 <= vlan <= 4094:
        return "VLAN de rango EXTENDIDO"
    else:
        return "Número fuera de rango válido (1–4094)"

def main():
    try:
        numero = int(input("Ingresa el número de VLAN: "))
        resultado = tipo_vlan(numero)
        print(resultado)
    except ValueError:
        print("Entrada inválida: por favor ingresa un número entero.")

if __name__ == "__main__":
    main()
