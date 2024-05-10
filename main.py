from similarity import Similarity
from beautiful import Beautiful

# Funcion debe aceptar 1 url + etiqueta x2                              (Puede ser la misma funcion para poner 2 veces valores o 2 diferentes funciones)
# Debe de ser comparar primer titulo con el resto y indicar el mayor    (Y asi con el segundo, tercero, etc...)


class ComparacionWeb:
    @staticmethod
    def comparar(url1:str, url2:str, etiqueta:str):
        beautiful = Beautiful()
        argumento1 = beautiful.obtenerInformacion(url1, etiqueta)
        argumento2 = beautiful.obtenerInformacion(url2, etiqueta)

        similarity = Similarity()
        return similarity.string_similarity(argumento1, argumento2)


def main():
    prueba = ComparacionWeb()
    resultado = prueba.comparar("https://www.elmundo.es/", "https://www.laprovincia.es/", "h2")
    print(resultado)
    


if __name__ == "__main__":
    main()