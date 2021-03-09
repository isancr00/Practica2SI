import fractions
import math


def ejercicio1(decimal, longitud, alfabeto, probabilidades):
    resultado = "El mensaje resultante es: "
    fraccion = fractions.Fraction(decimal)
    pos = 0

    for i in range(longitud):
        for j in range(alfabeto.__len__()):
            if j == 0:
                fraccion1 = fractions.Fraction(0, sum(probabilidades))
            else:
                fraccion1 = fraccion2
            fraccion2 = fraccion1 + fractions.Fraction(probabilidades[j], sum(probabilidades))

            if fraccion1 < fraccion < fraccion2:
                pos = j
                resultado += alfabeto[pos]
                fraccion = cambiarValor(fraccion, fraccion1, fraccion2)
                break

    return resultado


def cambiarValor(fraccion, fraccion1, fraccion2):
    numerador = fraccion - fraccion1
    denominador = fraccion2 - fraccion1

    return fractions.Fraction(numerador, denominador)


def sumatorio(probabilidades):
    suma = 0
    for i in range(probabilidades.__len__()):
        suma += probabilidades[i] * math.log(probabilidades[i], 2)

    return suma


def calcularEntropia(probabilidades):
    entropia = 0
    sumaProbabilidades = sum(probabilidades)
    logaritmoTotal = math.log(sumaProbabilidades, 2)

    entropia = logaritmoTotal - ((1 / sumaProbabilidades) * sumatorio(probabilidades))

    return entropia


def ejercicio2(texto, decimal, longitud):
    entropia = 0
    alfabeto = extraerCaracteres(texto)
    probabilidades = prob(texto, alfabeto)
    entropia = calcularEntropia(probabilidades)
    print("La entropía de la fuente resultante es: ", entropia)
    print(ejercicio1(decimal, longitud, alfabeto, probabilidades))


def buscarPosicion(caracter, alfabeto):
    for i in range(alfabeto.__len__()):
        if caracter.__eq__(alfabeto[i]):
            return i


def prob(texto, alfabeto):
    probabilidades = []
    for i in range(alfabeto.__len__()):
        probabilidades.append(0)

    for i in range(texto.__len__()):
        caracter = texto[i]
        posicion = buscarPosicion(caracter, alfabeto)
        probabilidades[posicion] += 1

    return probabilidades


def extraerCaracteres(texto):
    caracteres = []

    for i in range(texto.__len__()):
        if caracteres.__contains__(texto[i]) == 0:
            caracteres += texto[i]

    return caracteres


# Press the green button in the gutter to run the script.
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z", " ", "."]
probabilidades = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print("Ejercicio 1:\n")
print(ejercicio1("0.1613657607216723798346110583", 19, alfabeto, probabilidades), "\n")

print("Ejercicio 2:\n")
decimal = fractions.Fraction("0.247276109705412160222")
texto = "Existe una cosa muy misteriosa, pero muy cotidiana. Todo el mundo participa de ella,  todo el mundo la conoce, pero muy pocos se paran a pensar en ella.  Casi todos se limitan a tomarla como viene, sin hacer preguntas.  Esta cosa es el tiempo.  (Momo, Michael Ende)"
ejercicio2(texto, decimal, 17)

print("Ejercicio 3:\n")

texto = "Un aire marino, pesado y fresco, entró en mis pulmones con la primera  sensación confusa de la ciudad: una masa de casas dormidas; de establecimientos  cerrados; de faroles como centinelas borrachos de soledad. Una respiración  grande, dificultosa, venía con el cuchicheo de la madrugada. Muy cerca, a mi  espalda, enfrente de las callejuelas misteriosas que conducen al Borne, sobre mi  corazón excitado, estaba el mar.  (NADA, Carmen Laforet, 1921-2004)"
decimal = fractions.Fraction("0.96402816270036736770957975564255630564009")
ejercicio2(texto, decimal, 27)
