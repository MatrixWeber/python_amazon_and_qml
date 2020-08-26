from passlib.context import CryptContext



def get_crypt_context(rounds):
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=rounds
    )
    return pwd_context


def encrypt_password(password):
    pwd_context = get_crypt_context(30000)
    hashed =  pwd_context.encrypt(password)
    verified = check_encrypted_password(pwd_context, password, hashed)
    return hashed, verified


def decrypt_password(hash):
    pwd_context = get_crypt_context(30000)
    return pwd_context.decrypt(hash)


def check_encrypted_password(pwd_context, password, hashed):
    return pwd_context.verify(password, hashed)
