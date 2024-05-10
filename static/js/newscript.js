
function limitDescription() {
    const descriptionTextarea = document.getElementById('description');
    console.log(descriptionTextarea)
    const maxChars = 100; // Set the maximum character limit

    if (descriptionTextarea.textContent.length > maxChars) {
      // Truncate the text
      descriptionTextarea.textContent = descriptionTextarea.textContent.substring(0, maxChars);

      // Add an ellipsis to indicate truncated text
      descriptionTextarea.textContent += '...';
    }
  }

