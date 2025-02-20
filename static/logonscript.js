Document.addEventListener(“DOMContentLoaded”, function() {
 // Seleciona o botão “Sair”
 Const sairBotao = document.querySelector(‘a[href=”/”]:nth-child(2)’);

 // Adiciona evento de clique
 sairBotao.addEventListener(“click”, function(event) {
 const confirmacao = confirm(“Tem certeza que deseja sair?”);
 if (!confirmacao) {
 event.preventDefault(); // Cancela a ação se o usuário clicar em “Cancelar”
 }
 });
});

document.addEventListener("DOMContentLoaded", function () {
        var logoutButton = document.getElementById("logoutButton");

        if (logoutButton) {
            logoutButton.addEventListener("click", function (event) {
                var confirmLogout = confirm("Você tem certeza que deseja sair?");
                if (!confirmLogout) {
                    event.preventDefault(); // Cancela o redirecionamento se o usuário clicar em "Cancelar"
                }
            });
        }
    });