// Wait for the document to be fully loaded before manipulating the DOM
$(document).ready(function () {
  // Attach a click event handler to the div with id 'add_item'
  $('#add_item').click(function () {
    // Create a new <li> element with the text 'Item'
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to the <ul> element with class 'my_list'
    $('.my_list').append(newItem);
  });
});
