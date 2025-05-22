from encryption.encryption import encrypt_text
from analysis.analysis import analyze_journal_entry

text = "Bugün biraz stresliydim ama sonunda başardım ve mutlu hissediyorum."
password = "benimanahtar123"

# 1. Günlüğü şifrele
encrypted = encrypt_text(text, password)

# 2. AI ile analiz et
result = analyze_journal_entry(encrypted, password)

print("\n🎯 Sonuç:")
print(result)