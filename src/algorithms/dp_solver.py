def solve_dp(capacity, weights, values, n):
    """
    0/1 Knapsack problemi için Dinamik Programlama çözümü.
    Bellek tasarrufu için 1 Boyutlu (1D) array optimizasyonu kullanılmıştır.
    Buna rağmen N=10000 değerinde işlem süresi (Zaman Karmaşıklığı) devasa boyutlara ulaşacaktır.
    """
    # DP tablosunu sıfırlarla doldur
    dp = [0] * (capacity + 1)
    
    # Tüm eşyalar için dön
    for i in range(n):
        # Kapasiteden geriye doğru dönerek eşyanın sığıp sığmadığını kontrol et
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
            
    # Kapasitenin son elemanı maksimum değeri verir
    return dp[capacity]