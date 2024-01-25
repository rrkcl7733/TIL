n = int(input())

bodovi_predsjednik = [0] * n
bodovi_clanovi = [0] * n

poredak_predsjednik = list(map(int, input().split()))

for i in range(n):
    bodovi_predsjednik[poredak_predsjednik[i] - 1] = n - i

glasovi_clanovi = list(map(int, input().split()))

glasovi_i_oznaka = []
for i in range(n):
    glasovi_i_oznaka.append([glasovi_clanovi[i], i])
glasovi_i_oznaka.sort()

for i in range(n):
    bodovi_clanovi[glasovi_i_oznaka[i][1]] = i + 1

ukupno = []
for i in range(n):
    ukupno.append([bodovi_predsjednik[i] + bodovi_clanovi[i], bodovi_clanovi[i], i + 1])
ukupno.sort(reverse=True)

mjesto = 1
for i in range(n):
    if (i > 0 and (ukupno[i][0] != ukupno[i - 1][0] or ukupno[i][1] != ukupno[i - 1][1])):
        mjesto = i + 1
    
    ispis = str(mjesto) + ". "
    ispis += "Kod"

    if (ukupno[i][2] < 10):
        ispis += "0"
    ispis += str(ukupno[i][2])

    ispis += " ("
    ispis += str(ukupno[i][0])
    ispis += ")"

    print(ispis)
