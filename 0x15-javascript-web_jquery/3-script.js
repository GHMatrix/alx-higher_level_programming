// Wait for the document to be fully loaded before manipulating the DOM
$(document).ready(function () {
  // Attach a click event handler to the div with id 'red_header'
  $('#red_header').click(function () {
    // Select the <header> element and add the 'red' class to it
    $('header').addClass('red');
  });
});
