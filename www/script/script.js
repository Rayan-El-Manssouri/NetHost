function validateForm(event) {
  event.preventDefault(); // Empêche la soumission du formulaire

  // Récupère les valeurs des champs de connexion
  var loginInput = document.getElementById("login").value;
  var passwordInput = document.getElementById("password").value;

  // Récupère les données du fichier JSON
  fetch("data.json")
    .then(response => response.json())
    .then(data => {
      // Vérifie si les informations de connexion sont valides
      if (data.login === loginInput && data.password === passwordInput) {
        // Stocke l'état de connexion dans le localStorage
        localStorage.setItem("loggedin", "true");
        alert("Connexion réussie !");
        // Effectuez ici les actions nécessaires après la connexion réussie
        window.location.href = "home.html";
      } else {
        alert("Identifiants de connexion invalides !");
      }
    })
    .catch(error => {
      console.error("Erreur lors de la récupération du fichier JSON :", error);
    });
}

