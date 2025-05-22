from encryption import encrypt_text, decrypt_text
if __name__ == "__main__":
    password = "benimAnahtar123"
    text = "Bugün hava çok güzeldi ve çok çalıştım."

    print("🎯 ORİJİNAL METİN:", text)

    encrypted = encrypt_text(text, password)
    decrypted = decrypt_text(encrypted, password)

    print("🎯 SONUÇ BAŞARILI MI?", decrypted == text)