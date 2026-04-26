import matplotlib.pyplot as plt

def create_academic_plots():
    # Deney verileri
    n_values = [100, 1000, 10000]
    dp_times = [0.0143, 1.3564, 143.1840]
    ga_times = [0.2723, 2.0803, 19.6569]
    gaps = [1.00, 20.61, 32.42]

    # IEEE Standart Ayarları: Küçük boyut, serif font, yüksek netlik
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 9,
        'axes.labelsize': 9,
        'axes.titlesize': 10,
        'legend.fontsize': 8,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'axes.grid': True,
        'grid.alpha': 0.3
    })

    # --- Grafik 1: Zaman Karmaşıklığı (Daha Dar) ---
    # Figsize (3.5, 2.8) inç -> Tam bir IEEE sütun genişliği
    plt.figure(figsize=(3.5, 2.8), dpi=300)
    
    plt.plot(n_values, dp_times, 'ro-', lw=1.5, ms=5, label='DP (Kesin)')
    plt.plot(n_values, ga_times, 'bs--', lw=1.5, ms=5, label='GA (Sezgisel)')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Veri Boyutu (N)")
    plt.ylabel("Süre (sn)")
    plt.title("Zaman Karmaşıklığı Analizi")
    plt.legend(loc='upper left')
    plt.tight_layout()
    
    # Dosyayı direkt kaydediyoruz (results/ olmadan, karışıklık çıkmasın)
    plt.savefig("time_comparison.png", bbox_inches='tight')
    plt.close()

    # --- Grafik 2: Accuracy Gap (Daha Dar) ---
    plt.figure(figsize=(3.5, 2.8), dpi=300)
    
    colors = ['#4A90E2', '#50E3C2', '#F5A623']
    bars = plt.bar([str(n) for n in n_values], gaps, color=colors, edgecolor='black', width=0.6)

    plt.xlabel("Veri Boyutu (N)")
    plt.ylabel("Sapma (%)")
    plt.title("GA Optimumdan Sapma Oranı")
    plt.ylim(0, 40)

    for bar, gap in zip(bars, gaps):
        plt.text(bar.get_x() + bar.get_width()/2, gap + 0.5, f"%{gap:.1f}", 
                 ha='center', va='bottom', fontsize=8, fontweight='bold')

    plt.tight_layout()
    plt.savefig("accuracy_gap.png", bbox_inches='tight')
    plt.close()

    print("[+] Görseller 'time_comparison.png' ve 'accuracy_gap.png' olarak akademik boyutta oluşturuldu.")

if __name__ == "__main__":
    create_academic_plots()