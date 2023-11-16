import math

def area_circulo(radio):
    return math.pi * radio**2

def perimetro_circulo(radio):
    return 2 * math.pi * radio

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def area_triangulo(base, altura):
    return 0.5 * base * altura

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3