"""
Calculadora básica - Práctica de Git y GitHub
ULACIT - Control de versiones con Git
"""
def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b
def restar(a, b):
    """Retorna la resta de dos números."""
    return a - b
def main():
    print("=== Calculadora ULACIT ===")
    x = float(input("Ingrese el primer número: "))
    y = float(input("Ingrese el segundo número: "))
    print(f"Suma: {sumar(x, y)}")
    print(f"Resta: {restar(x, y)}")
if __name__ == "__main__":
    main()