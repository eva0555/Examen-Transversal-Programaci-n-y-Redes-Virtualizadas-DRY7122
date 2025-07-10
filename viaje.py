from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def obtener_coordenadas(ciudad):
    geo = Nominatim(user_agent="dry7122_app")
    loc = geo.geocode(ciudad + ", Chile" if "Chile" not in ciudad and "Argentina" not in ciudad else ciudad)
    if loc:
        return (loc.latitude, loc.longitude)
    else:
        return None

def calcular_distancia(origen, destino):
    coords1 = obtener_coordenadas(origen)
    coords2 = obtener_coordenadas(destino)
    if not coords1 or not coords2:
        print("Error: no se pudo encontrar una de las ciudades.")
        return None
    km = geodesic(coords1, coords2).kilometers
    millas = geodesic(coords1, coords2).miles
    return km, millas

def duracion_viaje(km, medio):
    velocidades = {
        "auto": 100,      # km/h
        "avión": 900,
        "bicicleta": 15,
        "caminando": 5
    }
    velocidad = velocidades.get(medio, None)
    if not velocidad:
        return None
    horas = km / velocidad
    h = int(horas)
    m = int((horas - h) * 60)
    return h, m

def narrativa(origen, destino, medio, km, millas, h, m):
    print(f"\n--- Resumen de tu viaje ---")
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"Medio de transporte: {medio}")
    print(f"Distancia: {km:.2f} km ({millas:.2f} millas)")
    print(f"Duración aproximada: {h} h {m} min")
    print(f"\nNarrativa:")
    print(f"Vas desde {origen} hasta {destino} en {medio}, recorriendo {km:.2f} km")
    print(f"({millas:.2f} millas) y tardarás alrededor de {h} horas y {m} minutos.\n")

def main():
    while True:
        origen = input("Ciudad de Origen (o 's' para salir): ")
        if origen.lower() == 's':
            break
        destino = input("Ciudad de Destino (o 's' para salir): ")
        if destino.lower() == 's':
            break

        resultado = calcular_distancia(origen, destino)
        if not resultado:
            continue
        km, millas = resultado

        print("Elige medio de transporte:")
        print("  1) auto")
        print("  2) avión")
        print("  3) bicicleta")
        print("  4) caminando")
        opcion = input("Opción [1–4]: ")

        medios = {'1': 'auto', '2': 'avión', '3': 'bicicleta', '4': 'caminando'}
        medio = medios.get(opcion, None)
        if not medio:
            print("Opción inválida, inténtalo de nuevo.\n")
            continue

        dur = duracion_viaje(km, medio)
        if not dur:
            print("No se puede calcular la duración para ese medio.\n")
            continue
        h, m = dur

        narrativa(origen, destino, medio, km, millas, h, m)

    print("¡Hasta luego!")

if __name__ == "__main__":
    main()
