<template>
    <div id="result-View">
        <p>10問中、{{resultData}}正解です！！</p>
        <div class="reset-button">
            <button v-on:click="resetTriger">最初から</button>
        </div>
    </div>
</template>

<script>
import store from '@/store';

export default {
    name: 'result',
    data(){
        return {
            resultData: this.$store.state.correctCount
        }
    },
    computed: {
        getStoreData(){
            return this.$store.state.correctCount
        }
    },
    methods: {
        async resetTriger(){
            await store.dispatch('executeReset')
            this.$router.push('/views/start')
            console.log("reset", this.$store.state.data)
        }
    }
}
</script>

<style scoped>
#result-View{
    font-size: 50px;
}
</style>