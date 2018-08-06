const Vue = require('vue');

const VueMap = require('./components/VueMap.vue')
Vue.component('vuemap', VueMap);

const App = require('./components/RecordLocation.vue');
new Vue({
  el: 'recordlocation',
  render: (createElement) => createElement(App)
});