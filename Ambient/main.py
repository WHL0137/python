import os
import subprocess
import sys

def create_dir_structure():
    os.makedirs("src", exist_ok=True)
    os.makedirs("tests", exist_ok=True)
    print("Estrutura de diretórios criada.")

def create_files():
    # .gitignore
    gitignore_content = """env/
__pycache__/
*.pyc
.pytest_cache/
"""
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)

    # README.md
    readme_content = "# Meu Projeto Python\n\nProjeto inicial com ambiente virtual, linting e testes unitários."
    with open("README.md", "w") as f:
        f.write(readme_content)

    # src/main.py
    main_py_content = '''"""
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
'''
    with open(os.path.join("src", "main.py"), "w") as f:
        f.write(main_py_content)

    # tests/test_main.py
    test_main_content = '''from src.main import saudacao

def test_saudacao():
    assert saudacao("Maria") == "Olá, Maria!"
    assert saudacao("João") == "Olá, João!"
'''
    with open(os.path.join("tests", "test_main.py"), "w") as f:
        f.write(test_main_content)

    # pyproject.toml para configuração do Black (opcional)
    pyproject_content = '''[tool.black]
line-length = 88
target-version = ['py38']
'''
    with open("pyproject.toml", "w") as f:
        f.write(pyproject_content)

    # .flake8 para configuração do Flake8 (opcional)
    flake8_content = '''[flake8]
max-line-length = 88
exclude = env, __pycache__
'''
    with open(".flake8", "w") as f:
        f.write(flake8_content)

    print("Arquivos iniciais criados.")

def initialize_git():
    try:
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit: projeto com ambiente virtual, linting e testes unitários"],
            check=True,
        )
        print("Repositório Git inicializado e commit realizado.")
    except subprocess.CalledProcessError:
        print("Erro ao inicializar o repositório Git.")
        sys.exit(1)

def create_virtualenv():
    try:
        subprocess.run([sys.executable, "-m", "venv", "env"], check=True)
        print("Ambiente virtual 'env' criado.")
    except subprocess.CalledProcessError:
        print("Erro ao criar o ambiente virtual.")
        sys.exit(1)

def install_dependencies():
    # Determina o caminho do pip dentro do ambiente virtual
    if os.name == "nt":  # Windows
        pip_executable = os.path.join("env", "Scripts", "pip")
    else:
        pip_executable = os.path.join("env", "bin", "pip")

    packages = ["pytest", "pylint", "flake8", "black"]
    try:
        subprocess.run([pip_executable, "install"] + packages, check=True)
        print("Dependências instaladas:", ", ".join(packages))
    except subprocess.CalledProcessError:
        print("Erro ao instalar as dependências.")
        sys.exit(1)

def add_git_remote_and_push():
    remote_url = input("Digite a URL do repositório remoto no GitHub (ou pressione Enter para ignorar): ").strip()
    if remote_url:
        try:
            subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
            # Tenta enviar para o branch 'master' ou 'main'
            branch = "master"
            result = subprocess.run(["git", "push", "-u", "origin", branch])
            if result.returncode != 0:
                branch = "main"
                subprocess.run(["git", "push", "-u", "origin", branch], check=True)
            print("Código enviado para o repositório remoto.")
        except subprocess.CalledProcessError:
            print("Erro ao configurar o repositório remoto ou ao enviar os commits.")

def main():
    print("Iniciando a configuração do projeto...")
    create_dir_structure()
    create_files()
    initialize_git()
    create_virtualenv()
    install_dependencies()
    add_git_remote_and_push()
    print("Projeto configurado com sucesso!")

if __name__ == "__main__":
    main()
