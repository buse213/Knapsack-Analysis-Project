import json
import time
import os
from algorithms.dp_solver import solve_dp
from algorithms.ga_solver import solve_ga

def load_data(n):
    """Ürettiğimiz veri setlerini JSON'dan okur."""
    file_path = f"data/dataset_{n}.json"
    with open(file_path, 'r') as f:
        return json.load(f)

def run_experiments():
    n_values = [100, 1000, 10000]
    
    for n in n_values:
        print(f"\n{'='*50}")
        print(f" DENEY BAŞLIYOR: N = {n} EŞYA")
        print(f"{'='*50}")
        
        try:
            data = load_data(n)
        except FileNotFoundError:
            print(f"Hata: N={n} verisi yok. Önce generator.py çalıştır!")
            continue
            
        capacity = data["capacity"]
        weights = data["weights"]
        values = data["values"]
        
        # ---------------------------------------------------------
        # 1. DİNAMİK PROGRAMLAMA (KESİN ÇÖZÜM)
        # ---------------------------------------------------------
        print("-> 1. Dinamik Programlama (Kesin Çözüm) koşturuluyor...")
        start_time = time.time()
        try:
            # N=10000 değerinde kapasite çok büyük olacağı için MemoryError verecektir.
            dp_result = solve_dp(capacity, weights, values, n)
            dp_time = time.time() - start_time
            print(f"   [+] DP Sonucu : {dp_result}")
            print(f"   [+] DP Süresi : {dp_time:.4f} saniye")
        except Exception as e:
            # İşte LaTeX makalesinde bahsedeceğin çöküş anı!
            print(f"   [-] DP ÇÖKTÜ  : Sistem sınırları aşıldı! ({type(e).__name__})")
            dp_result = "N/A"
            
        # ---------------------------------------------------------
        # 2. GENETİK ALGORİTMA (SEZGİSEL ÇÖZÜM)
        # ---------------------------------------------------------
        print("\n-> 2. Genetik Algoritma (Sezgisel Çözüm) koşturuluyor...")
        start_time = time.time()
        ga_result = solve_ga(capacity, weights, values, n, pop_size=100, generations=200)
        ga_time = time.time() - start_time
        print(f"   [+] GA Sonucu : {ga_result}")
        print(f"   [+] GA Süresi : {ga_time:.4f} saniye")
        
        # ---------------------------------------------------------
        # 3. KARŞILAŞTIRMA VE ANALİZ
        # ---------------------------------------------------------
        if dp_result != "N/A":
            gap = ((dp_result - ga_result) / dp_result) * 100
            print(f"\n[ANALİZ] N={n} için Genetik Algoritma, kesin çözümden sadece %{gap:.2f} saptı.")
        else:
            print(f"\n[ANALİZ] N={n} için DP patladı. Sezgisel algoritma (GA) bu devasa veride tek çaremiz oldu!")

if __name__ == "__main__":
    run_experiments()