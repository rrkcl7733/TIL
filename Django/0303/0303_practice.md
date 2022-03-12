### views.py

```python
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
```

---

### urls.py

```python
from pages import views

urlpatterns = [
    path('lotto/', views.lotto),
]
```

---

### lotto.html

```django
<h1>로또 당첨 횟수를 알아보자.</h1>
<hr> 
<h1>이번 회차 당첨 번호 : {{ nums }} + {{ last }}</h1>
<h3>
    {% for people in rich %}
    <li>{{ forloop.counter }}등 : {{people}}번</li>
    {% endfor %}
    <li>꽝 : {{ poor }}번</li>
</h3>
```

![image-20220303224816778](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20220303224816778.png)

