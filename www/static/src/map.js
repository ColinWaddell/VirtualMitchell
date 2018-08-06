const Vue = require('vue');

const MapApp = require('./components/Map.vue');

new Vue({
  el: 'vmmap',
  render: (createElement) => createElement(MapApp)
});