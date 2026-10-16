import random

def fitness(chromosome, token_sizes, retrieval_scores, cache_limit):
    """Kromozomun (seçilen bilgi parçalarının) kalitesini ölçer."""
    total_tokens = sum(t * c for t, c in zip(token_sizes, chromosome))
    total_score = sum(s * c for s, c in zip(retrieval_scores, chromosome))
    
    # Eğer toplam token boyutu RAM'deki boş önbelleği (cache_limit) aşarsa, bu çözüm çöp olur (0 puan)
    if total_tokens > cache_limit:
        return 0 
    return total_score

def create_population(pop_size, n):
    """Rastgele 1 ve 0'lardan oluşan başlangıç popülasyonu (Aday Cache Durumları)."""
    return [[random.choice([0, 1]) for _ in range(n)] for _ in range(pop_size)]

def select(population, fitnesses):
    """Turnuva seçilimi: Rastgele 3 tanesini al, en iyisini ebeveyn yap."""
    tournament = random.sample(list(zip(population, fitnesses)), 3)
    tournament.sort(key=lambda x: x[1], reverse=True)
    return tournament[0][0]

def crossover(parent1, parent2, crossover_rate=0.8):
    """İki ebeveyni birleştirip yeni çocuklar üretir."""
    if random.random() < crossover_rate:
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    
    # KRİTİK DÜZELTME: Referans problemi olmaması için listelerin kopyasını döndürüyoruz
    return parent1[:], parent2[:]

def mutate(chromosome, mutation_rate=0.01):
    """Genlerde (bitlerde) ufak mutasyonlar yapar."""
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # 0'sa 1, 1'se 0 yap
    return chromosome

def solve_ga(cache_limit, token_sizes, retrieval_scores, n, pop_size=100, generations=200):
    """RAG Önbellek Optimizasyonu için Ana Genetik Algoritma Döngüsü"""
    population = create_population(pop_size, n)
    best_overall_score = 0
    
    for _ in range(generations):
        fitnesses = [fitness(chrom, token_sizes, retrieval_scores, cache_limit) for chrom in population]
        
        # En iyi çözümü takip et
        max_fit = max(fitnesses)
        if max_fit > best_overall_score:
            best_overall_score = max_fit
            
        # Yeni jenerasyonu oluştur
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
            
        population = new_population
        
    return best_overall_score