# Büyük Ölçekli Sırt Çantası (Knapsack) Problemi: Performans Analizi

Bu proje, kombinatoryal optimizasyon problemlerinin temel taşlarından biri olan **0/1 Sırt Çantası (Knapsack) Problemi**'nin çözümünde kullanılan iki farklı metodolojinin; **Dinamik Programlama (Deterministik)** ve **Genetik Algoritma (Sezgisel)** yaklaşımlarının performans kıyaslamasını içermektedir.

## 📌 Proje Özeti
Proje kapsamında, eleman sayısı $N=100$, $N=1000$ ve $N=10000$ olan farklı veri setleri üzerinde deneyler yapılmıştır. Temel odak noktası, veri boyutu büyüdükçe kesin çözüm sunan algoritmaların (DP) zaman maliyeti ile yaklaşık çözüm sunan sezgisel algoritmaların (GA) ölçeklenebilirliği arasındaki dengeyi (trade-off) analiz etmektir.

## 🚀 Kullanılan Algoritmalar

### 1. Dinamik Programlama (DP)
- **Yaklaşım:** Tablolama (Bottom-up) mantığı ile kesin sonucu garanti eder.
- **Optimizasyon:** Bellek maliyetini düşürmek için 1-Boyutlu dizi optimizasyonu kullanılmıştır.
- **Karmaşıklık:** $O(N \times W)$ zaman karmaşıklığına sahiptir.

### 2. Genetik Algoritma (GA)
- **Yaklaşım:** Doğal seçilim, çaprazlama ve mutasyon mekanizmalarını kullanan evrimsel arama.
- **Parametreler:** - Popülasyon: 100
  - Seçilim: Turnuva (k=3)
  - Mutasyon Oranı: %1
- **Avantaj:** Devasa arama uzaylarında makul sürede "yeterince iyi" sonuçlar üretir.

## 📊 Deneysel Bulgular
Yapılan testlerde, $N=10000$ seviyesinde Dinamik Programlama'nın hesaplama süresi logaritmik olmayan bir hızla artarak **143 saniyeye** ulaşmış, Genetik Algoritma ise aynı veri setini yaklaşık **20 saniyede** analiz etmiştir.

### Zaman Karmaşıklığı Analizi
![Zaman Karşılaştırması](results/time_comparison.png)

### Doğruluk Sapma Oranı (Accuracy Gap)
![Doğruluk Sapması](results/accuracy_gap.png)

## 📁 Proje Yapısı
```text
├── src/
│   └── knapsack_analysis.py    # Algoritma implementasyonları ve testler
├── results/
│   ├── time_comparison.png     # Performans grafiği
│   └── accuracy_gap.png        # Sapma oranı grafiği
├── report/
│   ├── Metin_Serinkaya_Knapsack_Report.pdf  # Detaylı akademik rapor (IEEE)
│   └── main.tex                # Raporun LaTeX kaynak kodları
└── README.md                   # Proje dokümantasyonu