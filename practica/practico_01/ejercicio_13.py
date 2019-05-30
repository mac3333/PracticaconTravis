def es_primo(m):
    if m <= 2:
        return True
    
    limit = int(m ** 0.5 + 1)

    return not any(m % i == 0 for i in range(3, limit, 2))

