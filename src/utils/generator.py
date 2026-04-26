import json
import random
import os

def generate_and_save_data(n_values=[100, 1000, 10000], output_dir="data"):
    # Eğer data klasörü yoksa oluştur
    os.makedirs(output_dir, exist_ok=True)
    
    for n in n_values:
        # Ağırlıklar 1-50, değerler 1-100 arası rastgele
        weights = [random.randint(1, 50) for _ in range(n)]
        values = [random.randint(1, 100) for _ in range(n)]
        
        # Çanta kapasitesi, toplam ağırlığın yaklaşık yarısı olsun
        capacity = sum(weights) // 2
        
        data_dict = {
            "n": n,
            "capacity": capacity,
            "weights": weights,
            "values": values
        }
        
        # Dosyayı JSON olarak kaydet
        file_path = os.path.join(output_dir, f"dataset_{n}.json")
        with open(file_path, 'w') as f:
            json.dump(data_dict, f)
            
        print(f"Başarılı: {file_path} oluşturuldu. (Kapasite: {capacity})")

if __name__ == "__main__":
    # Bu dosyayı direkt çalıştırırsak verileri üretsin
    generate_and_save_data()