from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import base64
import os

def derive_key(password: str, salt:bytes, iterations=100000) -> bytes:
    return PBKDF2(password, salt, dkLen=32, count=iterations)

def encrypt_text(text: str, password: str) -> str:
    print("🔐 [encrypt_text] Başladı")
    print("🔸 Gelen metin:", text)
    print("🔸 Kullanıcı şifresi:", password)

    # 1. Salt oluştur
    salt = get_random_bytes(16)
    print("🔹 Salt (hex):", salt.hex())

    # 2. Key türet
    key = derive_key(password, salt)
    print("🔹 Türetilen Key (hex):", key.hex())

    # 3. AES motorunu oluştur
    cipher = AES.new(key, AES.MODE_GCM)
    print("🔹 AES Nonce (hex):", cipher.nonce.hex())

    # 4. Veriyi şifrele
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    print("🔹 Şifrelenmiş veri (hex):", ciphertext.hex())
    print("🔹 Doğrulama etiketi (tag, hex):", tag.hex())

    # 5. Verileri birleştir (salt + nonce + tag + ciphertext)
    data = salt + cipher.nonce + tag + ciphertext
    encoded_data = base64.b64encode(data).decode()

    print("🔸 Final Base64 Kod:", encoded_data)
    print("✅ [encrypt_text] Tamamlandı\n")

    return encoded_data

def decrypt_text(encoded: str, password: str) -> str:
    print("🔓 [decrypt_text] Başladı")
    print("🔸 Gelen Base64 Kod:", encoded)
    print("🔸 Kullanıcı şifresi:", password)

    # 1. Base64 çöz
    data = base64.b64decode(encoded)

    # 2. Bileşenleri ayır
    salt = data[:16]
    nonce = data[16:32]
    tag = data[32:48]
    ciphertext = data[48:]

    print("🔹 Salt (hex):", salt.hex())
    print("🔹 Nonce (hex):", nonce.hex())
    print("🔹 Tag (hex):", tag.hex())
    print("🔹 Ciphertext (hex):", ciphertext.hex())

    # 3. Key'i yeniden türet
    key = derive_key(password, salt)
    print("🔹 Türetilen Key (hex):", key.hex())

    # 4. AES motoru başlat
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    # 5. Veriyi çöz ve doğrula
    decrypted = cipher.decrypt_and_verify(ciphertext, tag).decode()
    print("🔸 Çözülmüş Metin:", decrypted)
    print("✅ [decrypt_text] Tamamlandı\n")

    return decrypted