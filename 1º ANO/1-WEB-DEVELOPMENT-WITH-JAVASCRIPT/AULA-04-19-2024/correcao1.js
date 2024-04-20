// desafio 1

var resultado = document.getElementById('resultado');

function clicar(){
    var livros = parseInt(document.getElementById('numBooks').value);
    var preco = ""
    if(livros < 7){
        preco = livros * 22
    }
    else {
        preco = livros * 15
    }
    
    resultado.innerText = `O preço dos livros é R$${preco},00`
}

//desafio 3
