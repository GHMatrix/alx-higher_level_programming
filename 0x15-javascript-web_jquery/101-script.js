// Wait for the document to be fully loaded before manipulating the DOM
$(document).ready(function () {
  // Attach a click event handler to the 'Add item' div
  $('#add_item').click(function () {
    // Create a new <li> element with the text 'Item'
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to the <ul> with class 'my_list'
    $('ul.my_list').append(newItem);
  });

  // Attach a click event handler to the 'Remove item' div
  $('#remove_item').click(function () {
    // Select the last <li> element in the list
    const lastItem = $('ul.my_list li:last-child');

    // Remove the last <li> element from the list if it exists
    if (lastItem.length > 0) {
      lastItem.remove();
    }
  });

  // Attach a click event handler to the 'Clear list' div
  $('#clear_list').click(function () {
    // Remove all <li> elements from the list
    $('ul.my_list').empty();
  });
});
