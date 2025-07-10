def main():
    integrantes = [
        "Nicolas Nunez",
        "Jose Catalan",  # ← Comilla bien cerrada (sin " extra)
    ]
    print("Lista de integrantes:")
    for idx, nombre in enumerate(integrantes, 1):
        print(f"{idx}. {nombre}")

if __name__ == "__main__":
    main()
