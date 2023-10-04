// Wait for the document to be fully loaded before manipulating the DOM
$(document).ready(function () {
  // Attach a click event handler to the div with id 'update_header'
  $('#update_header').click(function () {
    // Select the <header> element and update its text content
    $('header').text('New Header!!!');
  });
});
