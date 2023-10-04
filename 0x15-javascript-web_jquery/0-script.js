// Wait for the document to be fully loaded before manipulating the DOM
document.addEventListener('DOMContentLoaded', function () {
  // Select the <header> element using document.querySelector
  const headerElement = document.querySelector('header');

  // Update the text color to red (#FF0000)
  headerElement.style.color = '#FF0000';
});
