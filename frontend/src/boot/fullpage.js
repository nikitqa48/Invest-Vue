// import something here
import Vue from 'vue'
import FullPage from 'vue-fullpage.js'
// "async" is optional

export default  ({ Vue, FullPage }) => {
  // Vue.directive('fillpage', FullPage)
  Vue.use(FullPage)
}
