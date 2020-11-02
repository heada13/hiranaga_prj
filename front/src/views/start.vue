<template>
  <div class="start-container">
      <!-- <div v-if="loading" class="loading">
        Loading...
      </div> -->

      <div class="Question-view">
        <Question :question-data='answerData'></Question>
      </div>
      <div class="QuizButton-con">
        <div class="QuizButton-view" v-for="(value,key) in buttonData" v-bind:key="`first-${key}`">
          <QuizButton :button-data=[value,key]></QuizButton> 
        </div>
      </div>
      <div class="AnswerButton-con">
        <div class="AnswerButton-view" v-for="(value,key) in buttonData" v-bind:key="`second-${key}`">
          <AnswerButton :answer-data=[value,key] @ans="anscheack"></AnswerButton>
        </div>
      </div>
    <div id="overlay" v-show="showModal">
      <div id="content">
        <p v-show="showCrrect">せいかい！</p>
        <p v-show="showWrong">はずれ！</p>
        <button v-on:click="closeAction">次へ</button>
      </div>
    </div>
  </div>
</template>

<script>
import QuizButton from '../components/quizButton.vue'
import Question from '../components/question.vue'
import AnswerButton from '../components/answerButton.vue'
import store from '@/store';

export default {
  name: 'start',
  components: {
    QuizButton,
    Question,
    AnswerButton
  },
  data (){
    return {
      loading: false,
      qData: this.$store.state.data,
      buttonData: Array,
      answerData: String,
      showModal: false,
      showCrrect: false,
      showWrong: false
    }
  },
  async beforeRouteEnter(to, from, next) {
    console.log('api start')
    await store.dispatch('getQuestionAction')
    next()
    console.log('api end', store.state.data)
  },
  computed: {
    getStoreData: function(){
      return this.$store.state.data
    }
  },
  created: function(){
      // this.qData = this.$store.state.data
      this.buttonData = this.qData.createQ.buttons
      this.answerData = this.qData.createQ.question
      console.log('qData', this.qData)
      console.log('buttonData', this.buttonData)
  },
  methods: {
    anscheack(a){
      this.showModal = true;
      if(a === this.answerData){
        this.showCrrect = true;
        store.dispatch('getCrrectCountPlus')
        console.log('correct count', this.$store.state.correctCount)
      }else{
        this.showWrong = true;
      }
    },
    async closeAction(){
      this.showModal = false;
      this.showCrrect = false;
      this.showWrong = false;
      if(this.$store.state.count < 3){
        store.dispatch('getCountPlus')
        await store.dispatch('getQuestionAction')
        this.qData = this.$store.state.data
        console.log('count', this.$store.state.count)
      }else{
        this.$router.push('/views/result')
      }
    }
  },
  watch: {
    qData: function(){
      this.buttonData = this.qData.createQ.buttons
      this.answerData = this.qData.createQ.question
    }
  }
}
</script>

<style>

#overlay{
  z-index:1;
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background-color:rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

#content{
  z-index:2;
  width:50%;
  padding: 1em;
  background:#fff;
}

.start-container{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;  
}

.Question-view {
  width: 100%;
  display: flex;
  justify-content: center;
}

.QuizButton-con {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100px;
  /* background-color: green; */
}

.QuizButton-view {
  width: 110px;
  height: 110px;
  margin: 10px;
  /* background-color: blue; */
}

.AnswerButton-con {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 200px;
  /* background-color: red; */
}

.AnswerButton-view {
  width: 110px;
  height: 110px;
  margin: 10px;
}


</style>
