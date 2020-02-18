<template>

<div class="title">
     <header-vue/>
      <forms-vue/>
     <router-view/>
   
   

</div>
</template>
<script>
import formsVue from "../components/forms.vue";
import headerVue from "../components/header.vue";
export default {
    components: {
    formsVue,
    headerVue,
  },
}
</script>
<style scoped>

body{
    margin:0;
    padding:0;
}
.header{
    top:0;
}

@font-face {
  font-family: "Montserrat";
  src: url("../assets/fonts/Montserrat/Montserrat-Regular.woff") format("woff");
}
*{
  font-family: 'Montserrat';
}

</style>