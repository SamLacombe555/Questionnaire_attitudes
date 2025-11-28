def nombres_pairs_for(n):
    for i in range(2, n+1):
        if i % 2 == 0:
            print(f"#{i}")

nombres_pairs_for(10)

def nombres_pairs_while(n):
    j = 2
    while (j <= n):
        if j % 2 == 0:
            print(f"#{j}")
        j +=1
nombres_pairs_while(10)