/* alert('Olá, mundo!')
prompt("Digite seu nome")
confirm("Você deseja sair?") */

var nome = prompt('Digite seu nome: ');
console.log("Olá, " + nome + "! Seja bem-vindo!");
console.log(`Olá ${nome}, Seja bem-vindo!`);

var titulo = document.querySelector('h1');
titulo.innerText = `Olá ${nome}, seja bem-vindo`;

/*var idade = 23;
var idade2 = 23;
console.log('Resultado entre 23 sem aspas');
console.log(idade + idade2);
var idade3 = '23';
var idade4 = '23';
console.log('Resultado entre 23 COM aspas');
console.log(idade3 + idade4); */

/* var nome = prompt("Informe o seu nome: ");
var idade = prompt("Informe a sua idade: ");
var profissao = prompt("Informe a sua profissão: ");

console.log(`Olá ${nome}! Você tem ${idade} anos e sua profissão é ${profissao}. Seja bem-vindo!`); */

