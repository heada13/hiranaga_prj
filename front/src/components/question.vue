<template>
    <div class="question-container">
        <div class="q-text">{{questionData}}</div>
    </div>
</template>
<script>
export default {
    name: 'Qestion',
    props: [
        'questionData'
    ]
}
    // data: function() {
    //         return this.quesionData
    //     }
    // }
</script>

<style scoped>

.question-container{
    display: flex;
    justify-content: center;
    width: 200px;
    height: 200px;
    margin: 30px;
    border-radius: 20px;
    background-color: rgb(212, 211, 211);
}

.q-text{
    font-size: 100px;
    align-content: center;
    align-self: center;
}

</style>