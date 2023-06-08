document.addEventListener("DOMContentLoaded", function() {
  // Vérifie si l'utilisateur est connecté en vérifiant le cookie
  var isLoggedIn = getCookie("loggedin");
  if (isLoggedIn === "true") {
    // L'utilisateur est connecté, affichez le contenu de la page protégée
  } else {
    // L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
    window.location.href = "login.html";
  }
});
