def processa_valor(valor):
    # Estrutura condicional tradicional com if/elif/else
    if isinstance(valor, int):
        print("if/else: É um inteiro:", valor)
    elif isinstance(valor, str):
        print("if/else: É uma string:", valor)
    else:
        print("if/else: Tipo desconhecido:", valor)

    # Estrutura de pattern matching com match-case (Python 3.10+)
    match valor:
        case int():
            print("match-case: É um inteiro:", valor)
        case str():
            print("match-case: É uma string:", valor)
        case _:
            print("match-case: Tipo desconhecido:", valor)

# Exemplos de execução:
processa_valor(42)
processa_valor("Olá, mundo!")
processa_valor([1, 2, 3])
