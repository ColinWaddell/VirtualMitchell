const Vue = require('vue');

const App = require('./components/RecordLocation.vue');

new Vue({
  el: 'recordlocation',
  render: (createElement) => createElement(App)
});