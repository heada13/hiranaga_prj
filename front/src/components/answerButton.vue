<template>
    <div class="answerbuttons-container">
        <div class="vertical-line" :class="color1"/>
        <button class="answer-button" v-on:click="answer" :class="color1">
            <div class="innerButton"></div>
        </button>
    </div>
</template>

<script>
export default {
    name: 'AnswerButton',
    props: {
        answerData: [Array]
    },
    data (){
        return {
            color1:'default-class1',
            color2:'default-class2'
        }
    },
    created (){
        let dataIndex = this.answerData[1]
        if(dataIndex === 0){
            this.color1 = 'outer-class1'
        }else if(dataIndex === 1){
            this.color1 = 'outer-class2'
        }else if(dataIndex === 2){
            this.color1 = 'outer-class3'
        }else{
            this.color1 = 'outer-class4'
        }
    },
    methods:{
        answer: function(){
            let answer = Object.keys(this.answerData[0])[0]
            console.log("answer", answer)
            this.$emit("ans",answer);
        }
    }
}
</script>

<style scoped>

.answerbuttons-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: cneter;
}

.answer-button{
    width: 100px;
    height: 100px;
    border-radius: 10px;
}

.innerButton{
    position: relative;
    left: 10px;
    width: 60px;
    height: 60px;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.5);
}

.default-class1{
    background-color: white;
}

.outer-class1{
    background-color: #FA9D12;
}

.outer-class2{
    background-color: #12ECFA;
}

.outer-class3{
    background-color: #5DFF43;
}

.outer-class4{
    background-color: #EC79FF;
}

.vertical-line{
  margin-left: 50px;
  width: 5px;
  height: 100px;
}


</style>