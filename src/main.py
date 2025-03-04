"""
Módulo principal do projeto.
"""

def saudacao(nome: str) -> str:
    """
    Retorna uma saudação personalizada.

    Args:
        nome (str): Nome da pessoa a ser saudada.

    Returns:
        str: Saudação formatada.
    """
    return f"Olá, {nome}!"

if __name__ == "__main__":
    print(saudacao("Mundo"))
