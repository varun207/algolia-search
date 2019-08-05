
const search = instantsearch({
  appId: '5MOBI7FV78',
  apiKey: '7a2c03f64a54f740cea34a137587a887',
  indexName: 'products',
});

search.addWidget({
  init: function(opts) {
    const helper = opts.helper;
    const input = document.querySelector('#searchBox');
    input.addEventListener('input', function(e) {
      helper.setQuery(e.currentTarget.value) // update the parameters
            .search(); // launch the query
    });
  }
});

search.addWidget({
  render: function(opts) {
    const results = opts.results;
    // read the hits from the results and transform them into HTML.
    document.querySelector('#hits').innerHTML = results.hits.map(function(h) {
      return '<p>' + h._highlightResult.name.value + '</p>';
    }).join('');
  }
});

search.start();
