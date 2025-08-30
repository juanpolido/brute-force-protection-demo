import hashlib
import os
import hmac

salt = os.urandom(16)
senha_secreta = "bruteforce31"
hash_correta = hashlib.sha256(salt + senha_secreta.encode()).hexdigest()
tentativas = ["Fm0Czb6U693R","eMe7syl1dN5v","P@ssw0rd!","123456789",
"qwertyuiop","admin123","senha123","bruteforce31","letmein","password",
"111111","abc123","teste321","seguranca","python123"]

def verificar_lista():
    contador = 0

    for tentativa in tentativas:
        contador += 1
        hash_tentativa = hashlib.sha256(salt + tentativa.encode()).hexdigest()

        if hmac.compare_digest(hash_correta, hash_tentativa):
            print(f"Senha encontrada! Tentativas: {contador} ")
            print(f"Hash correspondente: {hash_tentativa}")
            return

    print("Senha nao encontrada no banco")


verificar_lista()
