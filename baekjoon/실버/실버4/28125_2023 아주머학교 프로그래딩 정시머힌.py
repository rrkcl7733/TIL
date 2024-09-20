dic = {
    '@': 'a', '[': 'c', '!': 'i', ';': 'j', '^': 'n',
    '0': 'o', '7': 't', "\\'": 'v', "\\\\'": 'w'
}

for _ in range(int(input())):
    cnt, result, tmp, flag = 0, '', '', 1
    s = input()
    for i, v in enumerate(s):
        if v.isalpha():
            result += v
        elif v in dic:
            result += dic[v]
            cnt += 1
        elif v not in ('\\', '\''):
            flag = 0
            break
        else:
            tmp += v
            if tmp in dic:
                result += dic[tmp]
                cnt += 1
                tmp = ''
    if len(result) / 2 > cnt and flag:
        print(result)
    else:
        print("I don't understand")
