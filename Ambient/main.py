"""
Módulo de Calculadora
=====================

Este módulo oferece funções básicas para operações matemáticas.
"""

def soma(a: int, b: int) -> int:
    """
    Soma dois números inteiros.

    Args:
        a (int): O primeiro número.
        b (int): O segundo número.

    Returns:
        int: A soma de 'a' e 'b'.
    """
    return a + b

if __name__ == "__main__":
    resultado = soma(2, 3)
    print(f"A soma de 2 e 3 é: {resultado}")
