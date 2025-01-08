document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    
    form.addEventListener("submit", function (event) {
        
        if (!validarFormulario()) {
            event.preventDefault();
        }
    });

    
    function validarFormulario() {
        let isValid = true;
        let mensagensErro = [];

        
        const nome = document.getElementById("nome");
        const telefone = document.getElementById("telefone");
        const email = document.getElementById("email");
        const diaconsulta = document.getElementById("diaconsulta");
        const nomePet = document.getElementById("nome-pet");
        const especie = document.getElementById("especie");
        const motivo = document.getElementById("motivo");

        
        if (nome.value.trim() === "") {
            mensagensErro.push("Por favor, preencha o nome completo.");
            isValid = false;
        }

        
        const telefoneRegex = /^\d{2} \d{5}-\d{4}$/;
        if (!telefoneRegex.test(telefone.value.trim())) {
            mensagensErro.push("Por favor, insira um telefone válido no formato (XX) XXXXX-XXXX.");
            isValid = false;
        }

        
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.value.trim())) {
            mensagensErro.push("Por favor, insira um e-mail válido.");
            isValid = false;
        }

        
        if (diaconsulta.value === "") {
            mensagensErro.push("Por favor, selecione um dia para a consulta.");
            isValid = false;
        }

        
        if (nomePet.value.trim() === "") {
            mensagensErro.push("Por favor, insira o nome do seu pet.");
            isValid = false;
        }

        
        if (especie.value === "") {
            mensagensErro.push("Por favor, selecione a espécie do pet.");
            isValid = false;
        }

        
        if (motivo.value.trim() === "") {
            mensagensErro.push("Por favor, descreva o motivo da consulta.");
            isValid = false;
        }

        // Exibe as mensagens de erro, se houver
        if (!isValid) {
            alert("Erros encontrados:\n" + mensagensErro.join("\n"));
        }

        return isValid;
    }
});