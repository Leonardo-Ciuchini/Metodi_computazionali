nn = input('Dammi un numero naturale: ')
nnn = input('Dammi un altro numero naturale per la somma: ')
aa = input('Dammi un numero naturale per la potenza degli argomenti della sommatoria: ')
a = int (aa)
n = int (nn)
nn = int (nnn)

def somma_prodotto(n):
    somma_n = 0
    prodotto_n = 1
    i = 1
    while i <= n:
        somma_n = somma_n + i
        prodotto_n = prodotto_n * i
        i = i + 1
    return(somma_n, prodotto_n)

def radici_quadrate(n):
    i = 0
    radici = 0
    while i <= n:
        radici = radici + i ** 0.5
        i = i + 1
    return(radici)

def sommatoria(nn, a = 1):
    sommatoria_n = 0
    i = 0
    while i <= nn :
        sommatoria_n = sommatoria_n + i ** a
        i = i + 1
    return(sommatoria_n)

print('-------------------------------------------------------------------------------------')
print('La somma dei numeri naturali da 0 a ', n, 'è: ', somma_prodotto(n)[0])
print('Il prodotto dei numeri naturali da 0 a ', n, 'è: ', somma_prodotto(n)[1])
print('La somma delle radici quadrate dei numeri naturali da 0 a ', n, 'è: ', radici_quadrate(n))
print('La sommatoria dei numeri naturali da 0 a ', nn, 'elevati alla potenza di ', a, 'è: ', sommatoria(nn, a))