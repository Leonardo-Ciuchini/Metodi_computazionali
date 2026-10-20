l1 = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']
l2 = ['giovedì', 'venerdì', 'sabato', 'domenica','lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica','lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica','lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato']
day = []
i = 1
while i <= 31:
        day.append(i)
        i = i + 1
for n,s in zip(day,l2):
    print(n,s)