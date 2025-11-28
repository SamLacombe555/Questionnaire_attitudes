def nombres_impairs_for(n):
    for i in range(n, 0, -1):
        if (i % 2) != 0:
            print(f"#{i}")

nombres_impairs_for(10)

def nombres_impairs_while(n):
    j = 10
    while j >= 0:
        if j % 2 !=0:
            print(f"#{j}")
        j -= 1

nombres_impairs_while(10)
