import Vue  from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    strict: true,
    state: {
        data: null,
        count: 0,
        correctCount: 0
    },
    getters: {
        getData(state) {
            return state.data
        }
    },
    mutations: {
        setData(state, payload) {
            state.data = payload.getquestion;
        },
        countPlus(state){
            state.count++
        },
        correctCountPlus(state){
            state.correctCount++
        },
        resetData(state) {
            state.data = null
        },
        resetCount(state){
            state.count = 0
        },
        resetCorrectCount(state){
            state.correctCount = 0
        }
    },
    actions: {
        async getQuestionAction(context) {
            const qst = await axios.get('/views/start').then(
                (res) => res.data
        ); 
        const payload = {    
            getquestion: qst,
        };
        context.commit('setData', payload);
        },
        getCountPlus(context){
            context.commit('countPlus')
        },
        getCrrectCountPlus(context){
            context.commit('correctCountPlus')
        },
        executeReset(context){
            context.commit('resetData')
            context.commit('resetCount')
            context.commit('resetCorrectCount')
        }
    }
})