<template>
  <div class="d-flex flex-column" style="position: relative; height:100%;">
    <div>
      <p class="genre_text">어떤 장르를 좋아하세요?</p>
    </div>
    <div class="btn-box">
      <button
        v-for="genre in genreList"
        :key="genre.id"
        @click="addGenreFilter($event, genre.id)"
        class="grayBtn"
        :id="genre.name"
      >
      {{genre.name}}</button>
    </div>
    <!-- <div class="d-flex" style="position: relative; height:100%;"> -->
    <select v-model="filterList" style="top:53px;">
      <option value="default" selected disabled hidden>FILTERS</option>
      <option value="random">랜덤</option>
      <!-- <option value="default">default</option> -->
      <option value="vote">평점순</option>
      <option value="popularity">인기순</option>
      <option value="new">신작순</option>
      <option value="old">구작순</option>
    </select>
    <div id="slideShow">
      <ul class="slides" id="slides-genre">
        <li v-for="movie in genreMovieList" :key="movie.id">
          <MovieListItem 
            :movie="movie"
          />
        </li>  
      </ul>
    </div>
    <p class="controller">
      <!-- &lang: 왼쪽 방향 화살표
      &rang: 오른쪽 방향 화살표 -->
      <span class="prev" @click="prevBtn">&lang;</span>  
      <span class="next" @click="nextBtn">&rang;</span>
    </p>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieGenreList',
  components: {
    MovieListItem,
  },
  data() {
    return {
      genreMovieList : null,
      filterList: null,
      genreFilter: [],
      genreList: [
        {
          id: '12',
          name: '모험',
        },
        {
          id: '14',
          name: '판타지',
        },
        {
          id: '16',
          name: '애니메이션',
        },
        {
          id: '18',
          name: '드라마',
        },
        {
          id: '27',
          name: '공포',
        },
        {
          id: '28',
          name: '액션',
        },
        {
          id: '35',
          name: '코미디',
        },
        {
          id: '80',
          name: '범죄',
        },
        {
          id: '878',
          name: 'SF',
        },
      ],
      currentIdx: 0,
    }
  },
  methods: {
    getGenreMovieList() {
      if (this.genreFilter.length > 0) {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/genremovielist/${this.filterList}`,
          params: {
            id: this.genreFilter.join(',')
          }
          })
            .then((res) => {
              this.genreMovieList = res.data
              const slides = document.querySelector('#slides-genre')
              slides.style.left = 0 + 'px';
              this.currentIdx = 0
            })
            .catch((err) => {
              console.log(err)
            })
      }
    },
    addGenreFilter(event, add) {
      if (!this.genreFilter.includes(add)) {
        this.genreFilter.push(add)
        event.target.classList = 'pinkBtn'
      } else {
        this.genreFilter = this.genreFilter.filter((exist) => exist!==add )
        event.target.classList = 'grayBtn'
      }
    },
    prevBtn() {
      if (this.currentIdx !== 0) {
        this.moveSlide(this.currentIdx - 1)
      }
    },
    nextBtn() {
      const slideImg = document.querySelectorAll('#slides-genre li')
      const slideCount = slideImg.length
      if (this.currentIdx !== slideCount - 1) {
        this.moveSlide(this.currentIdx + 1);
      }
    },
    moveSlide(num) {
      const slides = document.querySelector('#slides-genre')
      slides.style.left = -num * 800 + 'px';
      this.currentIdx = num;
    }

  },
  watch: {
    filterList: function () {
      this.getGenreMovieList()
    },
    genreFilter: function () {
      this.getGenreMovieList()
    },
  },
  created() {
    this.filterList = 'default'
    this.genreFilter.push('12')
  },
  mounted() {
    const defaultBtn = document.querySelector('#모험')
    defaultBtn.classList = 'pinkBtn'
  }
}
</script>

<style>
.btn-box {
  display: flex;
  justify-content: left;
  margin: 20px;
  margin-top: 0px;
}
.pinkBtn {
  width: 80px;
  height: 30px;
  border: none;
  margin-right: 5px;

  background: #FF9999;
  border-radius: 30px;

  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 13px;
  line-height: 20px;
  text-align: center;

  color: #FFFFFF;
  }
.grayBtn {
  width: 80px;
  height: 30px;
  border: none;
  margin-right: 5px;

  background: #5C5C5C;
  border-radius: 30px;

  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 13px;
  line-height: 20px;
  text-align: center;

  color: #FFFFFF;
  }
</style>