from src.main import saudacao

def test_saudacao():
    assert saudacao("Maria") == "Olá, Maria!"
    assert saudacao("João") == "Olá, João!"
