### 회고

---

#### 느낀점

> 전체적

하나씩 utv 순서대로 흐름을 이해하려고 복습겸 천천히 진행함.

시간이 엄청 오래 걸렸지만 그 전보다 확실히 이해하는 문법과 속도가 점점 빨라짐

> 기술적

form 내 label 의 for 와 input 의 id 를 연결하는 것 이해

create.html 과 update.html 이 없다는 것, 내부적으로 new와 edit에서 작업 후 redirect 로 페이지 다시 보여주는 것 이해

urls.py 에서 path 에 create.html 가 없음에도 create path 를 작성하는 것 이해

redirect 내 에서 movies:detail 문법이 movies 앱의 urls 에서 detail 을 찾아 views 로 이동해라 라고 이해

`edit.html`에서 release_date 의 저장 value 넘겨 줄때 `value='{{ movie.release_date|date:"Y-m-d" }}'` 으로 따옴표 분리로 작성해서 넘겨줘야 했음

