# μ μ²΄μ μΈ README

# **πΌ#1 Get Started**

> μλ² μ€μΉ λ° μ€ν
> 

```bash
$ git clone (repoμ£Όμ)
---- νμ ν΄λ μ΄λ
$ python -m venv venv (κ°μ νκ²½ μμ±)
$ source venv/Scripts/activate (ν΄λΉ ν°λ―Έλ μ­μ  λ° λ€μ μμ±μΌλ‘ λμ²΄ κ°λ₯)
$ pip install -r requirements (μ₯κ³  λ° μ€μΉν¨ν€μ§)
$ python manage.py makemigrations
$ python manage.py migrate (λ°μ΄ν°λ² μ΄μ€μ λͺ¨λΈ λ°μ)
$ python manage.py loaddata accounts.json movies.json community.json
$ python manage.py loaddata movies/genre.json movies/movie_data.json(λ°μ΄ν° λΆλ¬μ€κΈ°)

$ python manage.py runserver (μλ² μ€ν)

git clone λ°μλ€
F12 κ°λ°μ λ€μ΄κ°μ local storageμμλ ν ν° μ§μ°κΈ°
```

# **π³#2 κ°μ**

### **π±#2-1 Vue**

```

βββ README.md
βββ dist
βββ node_modules
βββ public
β   βββ favicon.io
β   βββ index.html
βββ src
β   βββ api
|	|	βββ drf.js
β   βββ assets
|	|	βββ Hotel.png
|	|	βββ imdb_logo.svg
|	βββ components
|	|	βββ ArticleCommentListItem.vue
|	|	βββ ArticleList.vue
|	|	βββ ArticleListItem.vue
|	|	βββ FollowingLikeMovieList.vue
|	|	βββ MovieActorItem.vue
|	|	βββ MovieGenreList.vue
|	|	βββ MovieList.vue
|	|	βββ MovieListItem.vue
|	|	βββ MovieReviewListItem.vue
|	|	βββ MovieSimilarListItem.vue
|	|	βββ ProfileUserLikeMovie.vue
|	|	βββ ProfileUserReviewMovie.vue
|	|	βββ TimelineItems.vue
|	|	βββ UserPostedArticles.vue
|	βββ plugins
| β	βββ vuetify.js
| βββ router
| |	βββ index.js
| βββ store
| |	βββ index.js
|	βββ views
|	|	βββ ArticleDetailView.vue
|	|	βββ CommunirtView.vue
|	|	βββ CreateView.vue
|	|	βββ DetailView.vue
|	|	βββ LoginView.vue
|	|	βββ MainView.vue
|	|	βββ ProgileView.vue
|	|	βββ SeratchView.vue
|	|	βββ TimelineView.vue
β   βββ App.vue
|	βββ main.js
βββ .gitignore
βββ babel.config.js
βββ jsconfig.json
βββ package.json
βββ vue.config.js
```

### **π±#2-2 Template & Components**

![Untitled](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/Untitled.png)

### **π±#2-3 E-R Diagram**

![Untitled](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/Untitled%201.png)

### **π±#2-4 λͺ©ν**

- μ¬μ©μκ° νλμ λ³΄κΈ° νΈν DB relation λ° UI κ΅¬μ‘° μΈλΆ μ€κ³
- μ μ κ° μ νν μ’μμ κΈ°λ°  μν μΆμ² μκ³ λ¦¬μ¦λ€  κ΅¬ν
- μ μ κ° νλ‘μ°ν μ¬λμ μν μ»¬λ μ λ¦¬μ€νΈ , μλ¦Ό
- νλ‘ νΈμλμ λ°±μλ μ§μ λλ€ ν€μ°κΈ°μν μ²΄μΈμ§ νλ‘μ νΈ
- λ΄κ° μ νΈνλ μ₯λ₯΄λ₯Ό νλμ νμ ν μμλ μ΄λ―Έμ§
- μΈλΆλΌμ΄λΈλ¬λ¦¬,CSS μ λλ©μ΄μμ μ΄μ©ν νλμ μ΄κ³  μΈλ ¨λ UI,UX κ΅¬ν

[μ λͺ© μμ](https://www.notion.so/37e073271c964f6ca5bc8509e972572d)

# **π³#3 ν΅μ¬ κΈ°λ₯ & λμμΈ**

**π±#3-1 λ‘κ·ΈμΈ/νμκ°μ νμ΄μ§**

![Untitled](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/Untitled%202.png)

![Untitled](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/Untitled%203.png)

- λ‘κ·ΈμΈ/νμκ°μ ν κΈμ°½μ λλ₯΄λ©΄ μλ‘ μλ ₯μ°½μ΄ μ νλλ€
- μμ΄λ : νκΈμΉλ©΄μ€λ₯
- λΉλ°λ²νΈ : μ«μ,νΉμλ¬Έμ.μλ¬Έμ ν¬ν¨ν΄μΌνλ€
- λΉλ°λ²νΈκ° κ°μ§μμΌλ©΄ μ€λ₯κ°λ¬λ€

**π±#3- λ©μΈ νμ΄μ§**

![screencapture-localhost-8080-home-2022-11-24-16_23_15.png](%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%20README%2084d8541cb8184c33aa8730de1883fd37/screencapture-localhost-8080-home-2022-11-24-16_23_15.png)