# Django 처음 시작하기

## 1. 가상환경

> 프로젝트별로 pip로 설치되는 패키지를 독립적으로 관리하기 위하여 

### 가상환경 생성

```bash
$ python -m venv venv
```

### 가상환경 실행

* `venv` 폴더 내의 스크립트를 실행 시키는 것

```bash
$ source venv/Scripts/activate
(venv)
```

### 가상환경 종료

```bash
$ deactivate
```

## 2. Django 설치

```bash
$ pip install django==3.2.12
```

* 혹시라도 4.x 버전을 설치한 경우 삭제 후 재설치 

```bash
$ pip uninstall django
```

## 3. Django 서버 실행

* 서버 종료는 `ctrl + c` 로 한다.

```bash
$ python manage.py runserver
```

![image-20220302130917374](README.assets/image-20220302130917374.png)

## 4. Django 개발하기

> 각 App에 MTV에 해당하는 기능을 구현한다.

### app 생성

```bash
$ python manage.py startapp 앱이름
```

* app  생성을 하면, 바로 등록을 진행한다.

```python
# firstpjt/settings.py
INSTALLED_APPS = [
    '앱이름',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```

### 기본 개발 흐름

![image-20220302134411476](README.assets/image-20220302134411476.png)

![img](README.assets/basic-django.png)

#### 1) URL 설정

* URL과 해당 URL로 요청오면 실행시킬 view의 함수를 지정한다.

```python
from django.contrib import admin
from django.urls import path
# aritlces 앱의 views.py
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL을 index/ 들어오면, 
    # index 함수를 실행시킬 것이다.
    path('index/', views.index),
    path('bts/', views.bts),
]

```

#### 2) views.py

* 함수를 정의할 때 반드시 첫번째는 `request`

  * request 객체 정보 : https://docs.djangoproject.com/en/3.2/ref/request-response/

  * 출력 예시

      ```
        ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
        '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', 
        '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'headers', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']
      ```

* 함수 return은 `render` 함수 활용

  * https://docs.djangoproject.com/ko/3.2/topics/http/shortcuts/#render
  * 필수 인자
    * request
    * template 이름

```python
# index 함수는
# 어떠한 작업을 하고 (아직 쓰지 않음)
# index.html을 랜더링할 것이다.
def index(request):
    # 작업
    return render(request, 'index.html')
```

#### 3) templates

* templates 폴더는 반드시 app 폴더 내부에 생성한다.

```html
<!-- articles/templates/index.html -->
<h1>안녕</h1>
```



















