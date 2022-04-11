const fetch = require('node-fetch');
let url = 'https://api.squiggle.com.au';

fetch(url)
.then(res => res.json())
.then((out) => {
  console.log('Checkout this JSON! ', out);
})
.catch(err => { throw err });