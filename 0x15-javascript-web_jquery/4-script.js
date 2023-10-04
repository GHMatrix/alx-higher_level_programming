// Wait for the document to be fully loaded before manipulating the DOM
$(document).ready(function () {
  // Attach a click event handler to the div with id 'toggle_header'
  $('#toggle_header').click(function () {
    // Select the <header> element
    const headerElement = $('header');

    // Check the current class of the <header> element
    if (headerElement.hasClass('red')) {
      // If it has the 'red' class, remove it and add the 'green' class
      headerElement.removeClass('red').addClass('green');
    } else {
      // If it has the 'green' class or no class, remove it and add the 'red' class
      headerElement.removeClass('green').addClass('red');
    }
  });
});
