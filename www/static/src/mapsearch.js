const Vue = require('vue');

const VueMap = require('./components/VueMap.vue')
Vue.component('vuemap', VueMap);

const MapSearch = require('./components/MapSearch.vue');
new Vue({
  el: 'vmmapsearch',
  render: (createElement) => createElement(MapSearch),
  components: {
    VueMap
  },
});