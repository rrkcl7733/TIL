data = {'CU': 'see you',
        ':-)': 'I’m happy',
        ':-(': 'I’m unhappy',
        ';-)': 'wink',
        ':-P': 'stick out my tongue',
        '(~.~)': 'sleepy',
        'TA': 'totally awesome',
        'CCC': 'Canadian Computing Competition',
        'CUZ': 'because',
        'TY': 'thank-you',
        'YW': "you’re welcome",
        'TTYL':	'talk to you later'}
while 1:
    a = input()
    print(data[a] if a in data.keys() else a)
    if a == 'TTYL':
        exit()
