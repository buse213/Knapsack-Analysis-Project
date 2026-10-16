def solve_dp(cache_limit, token_sizes, retrieval_scores, n):
    """
    RAG Önbellek (Cache) Optimizasyonu için Dinamik Programlama çözümü.
    Bellek tasarrufu için 1 Boyutlu (1D) array optimizasyonu kullanılmıştır.
    Buna rağmen bilgi parçası (chunk) sayısı N=10000 değerine ulaştığında, 
    işlem süresi (TTFT - İlk Kelimeyi Üretme Süresi hesabı) devasa boyutlara ulaşacaktır.
    """
    # DP tablosunu sıfırlarla doldur
    dp = [0] * (cache_limit + 1)
    
    # Tüm bilgi parçaları (chunk'lar) için dön
    for i in range(n):
        # Önbellek sınırından geriye doğru dönerek chunk'ın sığıp sığmadığını kontrol et
        for w in range(cache_limit, token_sizes[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - token_sizes[i]] + retrieval_scores[i])
            
    # Önbelleğin son elemanı elde edilebilecek maksimum uygunluk (retrieval) skorunu verir
    return dp[cache_limit]