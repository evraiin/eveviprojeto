Function validar() {
 var input1 = document.getElementById(“nomeuser”).value;
 var botao = document.getElementById(“botaoenviar”)
 var mensagem = document.getElementById(“mensagem”);
 if(input1 == “”){
 botao.type = “reset”;
 mensagem.textContent = “*O campo nome está vazio”;
 mensagem.style.color = “red”;
 }else{
 botao.type = “submit”;




 function validarFormularioCadastro() {
 const nome = document.getElementById(‘nome’).value.trim();
 const nomeAnimal = document.getElementById(‘nomeanimal’).value.trim();
 const email = document.getElementById(‘email’).value.trim();
 const senha = document.getElementById(‘senha’).value.trim();
 if (nome === ‘’ nomeAnimal === ‘’ email === ‘’ || senha === ‘’) {
 alert(‘Por favor, preencha todos os campos do cadastro.’);
 return false;
 }
 if (!email.includes(‘@’)) {
 alert(‘Por favor, insira um e-mail válido.’);
 return false;
 }
 return true;
}
 }