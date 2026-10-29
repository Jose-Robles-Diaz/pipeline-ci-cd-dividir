def dividir(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

try:
    num1 = int(input("Introduce el primer numero entero: "))
    num2 = int(input("Introduce el segundo numero entero: "))
    resultado = dividir(num1, num2)
    print(f"El resultado de la division es: {resultado}")
except ValueError as e:
    print(f"Error: {e}")