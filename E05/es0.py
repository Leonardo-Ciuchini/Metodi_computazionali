nn = input('Dammi un numero naturale: ')
nnn = input('Dammi un altro numero naturale per la somma: ')
aa = input('Dammi un numero naturale per la potenza degli argomenti della sommatoria: ')
a = int (aa)
n = int (nn)
nn = int (nnn)

def somma(n):
    somma_n = 0
    i = 0
    while i <= n:
        somma_n = somma_n + i 
        i = i + 1
    return(somma_n)

def sommatoria(nn, a = 1):
    sommatoria_n = 0
    i = 0
    while i <= nn :
        sommatoria_n = sommatoria_n + i ** a
        i = i + 1
    return(sommatoria_n)

print('-------------------------------------------------------------------------------------')
print('La somma dei numeri naturali da 0 a ', n, 'è: ', somma(n))
print('La sommatoria dei numeri naturali da 0 a ', nn, 'elevati alla potenza di ', a, 'è: ', sommatoria(nn, a))