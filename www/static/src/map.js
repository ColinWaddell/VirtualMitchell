const Vue = require('vue');

const VueMap = require('./components/VueMap.vue');

new Vue({
  el: 'vuemap',
  render: (createElement) => createElement(VueMap)
});