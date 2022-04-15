### accounts

accounts/forms.py 에서 UserCreationForm 을 바꿀 것이기 때문에 models.py 에서 AbstractUser 상속받는 User 를 작성하여 settings.py 에서  ```AUTH_USER_MODEL = 'accounts.User'``` 해주는 것을 이해했음.



```html
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
```

에서 비밀번호 변경 폼을 자동으로 도와주는 것을 알았음

```html
form = AuthenticationForm(request, request.POST)
form = CustomUserCreationForm(request.POST)
```

AutenticationForm 은 로그인할 때 비교하는 것으로서 일반 Form 이라 request 인자가 필요한 것이고 UserCreationForm 은 작성된 것을 DB에 반영할 것이니까 request 는 안써도 됨

```html
update_session_auth_hash(request, form.user)
```

이 부분이 생소했음 session 작성된 것을 변경 값으로 수정해주는 작업.

---

---

### movies

admin.py 에 등록을 해야지 /admin 에서 모델을 관리가능하다. 해서 `admin.site.register(모델, 모델어드민) 등록한다.

forms.py 에는 db에 입력받을 컬럼들을 선별하기 위하여 따로 작성해준다. `forms.ModelForm` 을 상속받아서.

models.py에는 각 모델을 설정해준다 ForeignKey 는 user 모델일 경우 순서상 늦게 참조되기 때문에 settings.AUTH_USER_MODEL 을 이용하여 accounts.User 임을 알려준다

##### views.py

ForeignKey 를 가지고 있는 모델폼 관련 작성할 경우 `save(commit=False)` 를 하고 ForeignKey 객체를 담아 주었다.

