<template>
    <div class="quizbuttons-container">
        <button class="replay-button" v-on:click="voiceReplay" :class="color1">
            <div class="innerButton"></div>
        </button>
    </div>
</template>

<script>
export default {
    name: 'QuizButton',
    props: {
        buttonData: [Array],
    },
    data (){
        return {
            color1:'default-class1',
        }
    },
    created (){
        let dataIndex = this.buttonData[1]
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
        voiceReplay (){
            let preValue = Object.values(this.buttonData[0])[0];
            let voiceData = preValue.replace('/front/public', '');
            console.log("data",voiceData);
            let m = new Audio(voiceData);
            m.play();
        }
    }
}
</script>

<style scoped>

.quizbuttons-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: cneter;
}

.replay-button{
    width: 100px;
    height: 100px;
    border-radius: 50px;
}

.innerButton{
    position: relative;
    left: 20px;
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 30px 0 30px 48px;
    border-color: transparent transparent transparent rgba(0, 0, 0, 0.5);
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

</style>