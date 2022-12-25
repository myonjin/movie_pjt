# 전체적인 README

# **🗼#1 Get Started**

> 서버 설치 및 실행
> 

```bash
$ git clone (repo주소)
---- 하위 폴더 이동
$ python -m venv venv (가상 환경 생성)
$ source venv/Scripts/activate (해당 터미널 삭제 및 다시 생성으로 대체 가능)
$ pip install -r requirements (장고 및 설치패키지)
$ python manage.py makemigrations
$ python manage.py migrate (데이터베이스에 모델 반영)
$ python manage.py loaddata accounts.json movies.json community.json
$ python manage.py loaddata movies/genre.json movies/movie_data.json(데이터 불러오기)

$ python manage.py runserver (서버 실행)

git clone 받은뒤
F12 개발자 들어가서 local storage에있는 토큰 지우기
```

# **🌳#2 개요**

### **🌱#2-1 Vue**

```

├── README.md
├── dist
├── node_modules
├── public
│   ├── favicon.io
│   └── index.html
├── src
│   ├── api
|	|	└── drf.js
│   ├── assets
|	|	├── Hotel.png
|	|	└── imdb_logo.svg
|	├── components
|	|	├── ArticleCommentListItem.vue
|	|	├── ArticleList.vue
|	|	├── ArticleListItem.vue
|	|	├── FollowingLikeMovieList.vue
|	|	├── MovieActorItem.vue
|	|	├── MovieGenreList.vue
|	|	├── MovieList.vue
|	|	├── MovieListItem.vue
|	|	├── MovieReviewListItem.vue
|	|	├── MovieSimilarListItem.vue
|	|	├── ProfileUserLikeMovie.vue
|	|	├── ProfileUserReviewMovie.vue
|	|	├── TimelineItems.vue
|	|	└── UserPostedArticles.vue
|	├── plugins
| │	└── vuetify.js
| ├── router
| |	└── index.js
| ├── store
| |	└── index.js
|	├── views
|	|	├── ArticleDetailView.vue
|	|	├── CommunirtView.vue
|	|	├── CreateView.vue
|	|	├── DetailView.vue
|	|	├── LoginView.vue
|	|	├── MainView.vue
|	|	├── ProgileView.vue
|	|	├── SeratchView.vue
|	|	├── TimelineView.vue
│   ├── App.vue
|	└── main.js
├── .gitignore
├── babel.config.js
├── jsconfig.json
├── package.json
└── vue.config.js
```

### **🌱#2-2 Template & Components**

![Untitled](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/Untitled.png)

### **🌱#2-3 E-R Diagram**

![Untitled](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/Untitled%201.png)

### **🌱#2-4 목표**

- 사용자가 한눈에 보기 편한 DB relation 및 UI 구조 세부 설계
- 유저가 선택한 좋아요 기반  영화 추천 알고리즘들  구현
- 유저가 팔로우한 사람의 영화 컬렉션 리스트 , 알림
- 프론트엔드와 백엔드 지식 둘다 키우기위한 체인지 프로젝트
- 내가 선호하는 장르를 한눈에 파악 할수있는 이미지
- 외부라이브러리,CSS 애니메이션을 이용한 현대적이고 세련된 UI,UX 구현

[제목 없음](https://www.notion.so/37e073271c964f6ca5bc8509e972572d)

# **🌳#3 핵심 기능 & 디자인**

**🌱#3-1 로그인/회원가입 페이지**

![Untitled](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/Untitled%202.png)

![Untitled](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/Untitled%203.png)

- 로그인/회원가입 토글창을 누르면 서로 입력창이 전환된다
- 아이디 : 한글치면오류
- 비밀번호 : 숫자,특수문자.영문자 포함해야한다
- 비밀번호가 같지않으면 오류가뜬다

**🌱#3- 메인 페이지**

![screencapture-localhost-8080-home-2022-11-24-16_23_15.png](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/screencapture-localhost-8080-home-2022-11-24-16_23_15.png)