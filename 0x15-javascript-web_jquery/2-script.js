// Wait for the document to be fully loaded before manipulating the DOM
$(document).ready(function () {
  // Attach a click event handler to the entire document
  $(document).on('click', '#red_header', function () {
    // Select the <header> element and update its text color to red (#FF0000)
    $('header').css('color', '#FF0000');
  });
});
