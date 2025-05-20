# 🪢 Adam Asmaca Oyunu: Excel’den Rastgele Kelime Seçme

Bu Python projesi, bir Excel dosyasındaki kelimeler arasından rastgele seçilen bir kelime ile klasik **Adam Asmaca** oyununu oynatır.  
Oyuncu, seçilen kelimenin harflerini tahmin etmeye çalışır ve 6 yanlış tahminde oyun biter.

---

## 🎯 Projenin Amacı

- Excel dosyasından farklı sütunlardaki kelimeleri okuyup rastgele seçmek.
- Seçilen kelimenin harflerini kullanarak adam asmaca oyunu oynatmak.
- Python ve `pandas` kütüphanesiyle veri okuma ve işleme pratiği yapmak.
- Basit bir metin tabanlı oyun geliştirmek.

---

## 🧰 Gereksinimler

### 📦 Kullanılan Kütüphaneler

- `pandas`: Excel dosyasını okumak için.
- `random`: Rastgele seçim için.

### 🔧 Kurulum Komutu

```bash
pip install pandas
```
## ⚙️ Kullanım

Excel dosyanızı oluşturun veya aşağıdaki örneğe benzer bir dosya kullanın:

| renkler  | günler    | aylar   |
|----------|-----------|---------|
| Yeşil    | Cumartesi | Aralık  |
| Kırmızı  | Çarşamba  | Şubat   |
| Teal     | Salı      | Ağustos |
| ...      | ...       | ...     |

Python dosyasında `excel_dosyasi` değişkenine Excel dosyanızın tam yolunu yazın.

Kodu çalıştırın ve oyun başlayacaktır. Harf tahminlerinizi girerek kelimeyi bulmaya çalışın.

---

## 🧠 Proje Özeti

- Program, Excel dosyasından rastgele bir sütun seçer.
- O sütundaki boş olmayan değerler arasından rastgele bir kelime alır.
- Oyuncu bu kelimedeki harfleri tahmin eder.
- 6 yanlış tahminde oyun biter, kelime açıklanır.
- Doğru tahminlerde kelimedeki ilgili harfler açılır.

---

## ⚠️ Uyarılar

- Excel dosyasındaki verilerin sütunlarda düzgün ve boşsuz olması oyunun sağlıklı çalışması için önemlidir.
- Tahminler sadece tek harf olmalı, sayı veya sembol kabul edilmez.
- Aynı harf birden fazla tahmin edilirse uyarı verir.

---

## 📌 Notlar

- Bu proje, Python ve pandas kullanarak dosya okumayı ve basit oyun mantığını öğrenmek için idealdir.
- Excel dosyası yerine başka veri kaynaklarıyla da uyarlanabilir.
