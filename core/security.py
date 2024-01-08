from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_senha(senha: str, hash: str) -> bool:
    return CRIPTO.verify(senha, hash)

def gerar_hash(senha: str) -> str:
    return CRIPTO.hash(senha)