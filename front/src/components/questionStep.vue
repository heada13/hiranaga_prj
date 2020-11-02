<template>
    <div id="stepview">
       <el-steps :active="active" finish-status="success">
            <el-step title="Step 1"></el-step>
            <el-step title="Step 2"></el-step>
            <el-step title="Step 3"></el-step>
        </el-steps>
        <el-button style="margin-top: 12px;" @click="next">Next step</el-button>
    </div>
</template>


<script>
// import {Steps, Step} from 'element-ui'
// import 'element-ui/lib/theme-default/date-picker.css'

export default {
    name: 'step',
    // components: {Steps, Step},
    data() {
        return {
            active: 0
        };
    },
    methods: {
        next() {
            if (this.active++ > 2) this.active = 0;
        }
    }
}
</script>

<style scoped>
/* @import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css"); */
</style>