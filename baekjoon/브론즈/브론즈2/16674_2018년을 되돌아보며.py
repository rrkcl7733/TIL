s = input()
allowed = set('2018')

if any(ch not in allowed for ch in s):
    print(0)
else:
    cnt = {d: 0 for d in '2018'}
    for ch in s:
        cnt[ch] += 1

    if any(cnt[d] == 0 for d in '2018'):
        print(1)
    else:
        values = [cnt[d] for d in '2018']
        if len(set(values)) == 1:
            print(8)
        else:
            print(2)
