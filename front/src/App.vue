<template>
  <div id="app">
    <header id="header-css">
      <step-progress :steps="mySteps" :current-step="currentStep" icon-class="fa fa-check"></step-progress>
    </header> 
    <div id="body">
      <button class="start-button" v-show="showButton" v-on:click="showButtonTrigger">スタート</button>
        <!-- <router-link to='./views/start'>スタート</router-link> -->
      <router-view/>
    </div>
  </div>
</template>

<script>
import StepProgress from 'vue-step-progress';
import 'vue-step-progress/dist/main.css';

export default {
  name: 'app',
  components: {
    'step-progress': StepProgress
  },
  data () {
    return {
      showButton: true,
      mySteps: [
        'Learn Vue',
        'Open Source',
        '???',
        'Profit'
      ],
      currentStep: 0,
      activeColor: 'red',
      passiveColor: 'gray',
      lineThickness: 12,
      activeThickness: 5,
      passiveThickness: 5
      }
  },
  methods: {
    showButtonTrigger(){
      this.showButton = false
      this.$router.push('/views/start')
    }
  }
}
</script>

<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */

/* .start-button{
  background-color: aqua;
  padding: 300px 150px 300px 150px;
  border-radius: 2em 2em 2em 2em/2em 2em 2em 2em;
  font-size: 100px;
} */

#header-css{
  background-color: lightgreen;
  width: 100%;
  height: 200px;
}

#body {
  background-color: rgb(194, 247, 194);
}


</style>
