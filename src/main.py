"""
M�dulo principal do projeto.
"""

def saudacao(nome: str) -> str:
    """
    Retorna uma sauda��o personalizada.

    Args:
        nome (str): Nome da pessoa a ser saudada.

    Returns:
        str: Sauda��o formatada.
    """
    return f"Ol�, {nome}!"

if __name__ == "__main__":
    print(saudacao("Mundo"))
