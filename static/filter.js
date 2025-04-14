
document.addEventListener('DOMContentLoaded', function() {
    const table = document.getElementById('table');
    const rows = table.getElementsByTagName('tr');
    const searchInput = document.getElementById('search');

    searchInput.addEventListener('input', function() {
        const filter = searchInput.value.toUpperCase();
        for (let i = 1; i < rows.length; i++) {
            const row = rows[i];
            const cells = row.getElementsByTagName('td');
            let found = false;
            for (let j = 0; j < cells.length; j++) {
                const cell = cells[j];
                if (cell) {
                    const txtValue = cell.textContent || cell.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        found = true;
                        break;
                    }
                }
            }
            row.style.display = found ? '' : 'none';
        }
    });

    function resetTable() {
        for (let i = 1; i < rows.length; i++) {
            rows[i].style.display = '';
        }
    }
});
// deconnexion.
function confirmLogout() {
    // Affiche une boîte de dialogue de confirmation
    var confirmation = window.confirm("Voulez-vous vraiment vous déconnecter ?");
  
    // Si l'utilisateur clique sur "OK" (ou "Oui" dans certains navigateurs), effectuez l'action de déconnexion
    if (confirmation) {
        // Placez ici le code pour la déconnexion de l'utilisateur
        // Par exemple : window.location.href = "page_de_deconnexion.html";
        alert("Vous êtes maintenant déconnecté !");
        window.location.href = 'http://127.0.0.1:5000/';
    } else {
        // Si l'utilisateur clique sur "Annuler" (ou "Non" dans certains navigateurs), n'effectuez aucune action
        alert("La déconnexion a été annulée.");
    }
}
//inscription
// Fonction qui sera exécutée lorsque le formulaire est soumis
function handleFormSubmit(event) {
    event.preventDefault(); // Empêcher le comportement par défaut du formulaire (envoi des données au serveur)
  
    // Récupérer les données du formulaire
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;
  
    // Vérifier si les mots de passe correspondent
    if (password !== confirmPassword) {
      alert("Les mots de passe ne correspondent pas.");
      return; // Arrêter l'exécution de la fonction
    }
  
    // Vérifier si l'email est unique 
  
    // Simuler une requête AJAX avec un délai de 1 seconde 
    setTimeout(() => {
      const isEmailUnique = true; // Remplacez cela par le résultat de votre requête AJAX
      if (!isEmailUnique) {
        alert("Cet email est déjà utilisé. Veuillez en choisir un autre.");
        return; // Arrêter l'exécution de la fonction
      }
  
      // Si toutes les vérifications passent, soumettre le formulaire
      document.getElementById("inscriptionForm").submit();
    }, 1000); // 1 seconde de délai pour simuler la requête AJAX
  }
  
  // Ajouter un écouteur d'événement pour le formulaire
  document.getElementById("inscriptionForm").addEventListener("submit", handleFormSubmit);

  //A propos page inscription
  function toggleMoreText() {
    const moreText = document.getElementById('moreText');
    const showMoreButton = document.getElementById('showMoreButton');

    if (moreText.style.display === 'none') {
        moreText.style.display = 'block';
        showMoreButton.textContent = 'Masquer';

        // Défilement de la page vers la zone de texte supplémentaire
        moreText.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
        moreText.style.display = 'none';
        showMoreButton.textContent = 'A propos';
    }
}
  


