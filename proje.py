import re

# İçinde her türlü karakter olan karışık bir metin
veri = "Bize ulaşın: destek@firma.com veya satis.temsilcisi@kurum.org.tr. Eski mailimiz eski@yandex.net artık aktif değil."

# Deseni değişkene atayalım
email_deseni = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# re.findall kullanarak tüm eşleşmeleri çekelim
sonuclar = re.findall(email_deseni, veri)

print("Bulunan E-postalar:", sonuclar)

# 2. Örnek

telefonlar = "Ali: 5321234567, Veli: 0533 987 65 43, Ayşe: 544-111-22-33"

# Kural: Başta 0 olsa da olmasa da, boşlukları ve tireleri temizle
# Sadece sayıları koru ve başına tek bir '0' ekle
temiz_liste = re.sub(r"[^0-9]", "", telefonlar) # Rakam dışındaki her şeyi sil

print("Temizlenmiş Veri:", temiz_liste)

# 3. Örnek

sifre = "Emirhan123"

buyuk_harf = re.search(r"[A-Z]", sifre)
rakam = re.search(r"[0-9]", sifre)

if buyuk_harf and rakam:
    print("Şifre Güvenli! ✅")
else:
    print("Şifre Geçersiz: En az bir büyük harf ve rakam olmalı! ❌")