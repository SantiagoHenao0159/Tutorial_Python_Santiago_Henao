# modulo.py

# Función para sumar dos números
def sumar(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b

# Función para restar dos números
def restar(a, b):
    """Resta el segundo número del primero y retorna el resultado."""
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    """Multiplica dos números y retorna el resultado."""
    return a * b

# Función para dividir dos números
def dividir(a, b):
    """Divide el primer número por el segundo y retorna el resultado.
    Si el divisor es cero, lanza un error.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
