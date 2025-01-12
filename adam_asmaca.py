import pandas as pd
import random

df=pd.read_excel("excel dosyasının yolunu yapıstırın ornegın sag taraftakı yorum satırı gıbı") #(r"C:\Users\koseb\OneDrive\Masaüstü\kelime_listesi.xlsx")
sütun_adı=random.choice(df.columns.tolist())
kelimeler=df[sütun_adı].dropna().tolist()
kelime=random.choice(kelimeler).lower()
harfler=list(kelime)
seçilen_kelime=["_"]*len(kelime)
can=6
tahminler=[]
print("adam asmaca oyununa hosgeldınız")
while can>0:
    print(f"\nsecilen kelime: {' '.join(seçilen_kelime)}")
    print(f"kalan can : {can}")
    tahmin=input("harf tahmininizi giriniz : ").lower()
    if len(tahmin) !=1 or not tahmin.isalpha():
        print("lütfen harf gir sayı veya alfabetık olmayan metın gırme ve yalnızca 1 harf gir")
        continue
    if tahmin in tahminler:
        print(f"{tahmin} harfini daha önceden girdin baska harf gir")
        continue
    tahminler.append(tahmin)
    if tahmin in harfler:
        for i in range(len(harfler)):
            if harfler[i] ==tahmin:
                seçilen_kelime[i]=tahmin
        print(f"bravo sectıgın {tahmin} harfi secilen kelımenın ıcınde var")
    else:
        can-=1
        print(f"üzgünüm {tahmin} harfi secılen kelımenın ıcınde yok")
    if "_" not in seçilen_kelime:
        print(f"\n tebrikler kelimeyi buldun kelıme {kelime} idi ")
        break
if can==0:
    print(f"uzgunum canınız kalmadı dogru kelıme {kelime} idi")