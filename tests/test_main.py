from src.main import saudacao

def test_saudacao():
    assert saudacao("Maria") == "Ol�, Maria!"
    assert saudacao("Jo�o") == "Ol�, Jo�o!"
