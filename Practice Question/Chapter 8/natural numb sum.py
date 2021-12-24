def natural (n) :
    if n == 0 :
        return 0
    else :
        s = n + natural(n - 1)
    return s
print(natural(10))