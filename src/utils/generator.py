import json
import random
import os

def generate_and_save_data(n_values=[100, 1000, 10000], output_dir="data"):
    # Eğer data klasörü yoksa oluştur
    os.makedirs(output_dir, exist_ok=True)
    
    for n in n_values:
        # LLM Senaryosu: Token boyutları 10-500 arası, uygunluk (retrieval) skorları 1-100 arası rastgele
        weights = [random.randint(10, 500) for _ in range(n)]
        values = [random.randint(1, 100) for _ in range(n)]
        
        # Qwen 7B Edge PC Önbellek (Cache) kapasitesi, toplam token'ın yaklaşık yarısı olsun
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
            
        print(f"Başarılı: {file_path} oluşturuldu. (Önbellek Cache Limiti: {capacity} token)")

if __name__ == "__main__":
  
    generate_and_save_data()