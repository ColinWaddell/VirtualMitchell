const Vue = require('vue');

const App = require('./components/Map.vue');

new Vue({
  el: '#map',
  render: (createElement) => createElement(App)
});