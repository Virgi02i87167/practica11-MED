import geometria

radio_circulo = 5
area_circulo = geometria.area_circulo(radio_circulo)
perimetro_circulo = geometria.perimetro_circulo(radio_circulo)

base_rectangulo = 4
altura_rectangulo = 6
area_rectangulo = geometria.area_rectangulo(base_rectangulo, altura_rectangulo)
perimetro_rectangulo = geometria.perimetro_rectangulo(base_rectangulo, altura_rectangulo)

base_triangulo = 3
altura_triangulo = 8
lado1_triangulo = 5
lado2_triangulo = 4
lado3_triangulo = 7

area_triangulo = geometria.area_triangulo(base_triangulo, altura_triangulo)
perimetro_triangulo = geometria.perimetro_triangulo(lado1_triangulo, lado2_triangulo, lado3_triangulo)

print(f'Área del círculo: {area_circulo}')
print(f'Perímetro del círculo: {perimetro_circulo}')

print(f'Área del rectángulo: {area_rectangulo}')
print(f'Perímetro del rectángulo: {perimetro_rectangulo}')

print(f'Área del triángulo: {area_triangulo}')
print(f'Perímetro del triángulo: {perimetro_triangulo}')