from encryption.encryption import decrypt_text
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')  # sadece ilk kullanımda gerekir

def analyze_journal_entry(encrypted_entry: str, password: str):
    print("🧠 [analyze_journal_entry] Başladı")

    # Şifreli metni çöz
    try:
        print("🔐 Şifre çözülüyor...")
        decrypted_text = decrypt_text(encrypted_entry, password)
        print("✅ Şifre çözümü başarılı.")
        print("📝 Günlük içeriği:", decrypted_text)
    except Exception as e:
        print("❌ Şifre çözümünde hata:", e)
        return {"status": "error", "message": "Şifre yanlış veya veri bozuk"}

    # Sentiment analizörü oluştur
    print("🔍 SentimentIntensityAnalyzer başlatılıyor...")
    sia = SentimentIntensityAnalyzer()

    # Analiz yap
    scores = sia.polarity_scores(decrypted_text)
    print("📊 Analiz Skorları:", scores)

    # Duyguyu belirle
    compound = scores['compound']
    if compound >= 0.05:
        mood = "Pozitif"
    elif compound <= -0.05:
        mood = "Negatif"
    else:
        mood = "Nötr"

    print(f"🧾 Belirlenen ruh hali: {mood}")
    print("✅ [analyze_journal_entry] Tamamlandı\n")

    return {
        "status": "success",
        "mood": mood,
        "scores": scores,
        "text": decrypted_text
    }