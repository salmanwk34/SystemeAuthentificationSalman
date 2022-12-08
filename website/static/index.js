function deletePost(noteId) { 
  fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({ noteId: noteId})
  }).then((_res) => { 
    window.location.href = "/"; // Redirection vers la page d'accueil
  });
}

