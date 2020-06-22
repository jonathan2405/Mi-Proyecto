#codigo ejemplo git
#Autor:jonathan Adriano
anio_actual= 2020
mes_actual=7
nombre =input("cual es tu nombre?:")
anio_nacimiento= int(input("en que año naciste?:"))
mes_nacimiento= int(input("en que mes naciste"))
edad= anio_actual - anio_nacimiento
if mes_nacimiento > mes_actual:
    edad -=1
print("hola", nombre, "tu edad es", edad);

