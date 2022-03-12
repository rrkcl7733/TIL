from django.shortcuts import render
import random
import json, requests
# Create your views here.
def lotto(request):
    response = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1').json()
    nums = [response.get('drwtNo1'), response.get('drwtNo2'), response.get('drwtNo3'), response.get('drwtNo4'), response.get('drwtNo5'), response.get('drwtNo6'), response.get('bnusNo')]
    # nums = list(random.sample(range(1, 46), 7))
    non_bonus = nums[:6]
    bonus = nums[-1]
    head = [0, 0, 0, 0, 0, 0]
    for _ in range(1000):
        test = list(random.sample(range(1, 46), 7))
        if len(set(non_bonus) - set(test)) == 0:
            head[0] += 1
        elif len(set(non_bonus) - set(test)) == 1 and bonus in test:
            head[1] += 1
        elif len(set(non_bonus) - set(test)) == 1:
            head[2] += 1
        elif len(set(non_bonus) - set(test)) == 2:
            head[3] += 1
        elif len(set(non_bonus) - set(test)) == 3:
            head[4] += 1
        else:
            head[5] += 1
    context = {
        'nums': non_bonus,
        'last': bonus,
        'rich': head[:5],
        'poor': head[-1]
    }
    return render(request, 'lotto.html', context)