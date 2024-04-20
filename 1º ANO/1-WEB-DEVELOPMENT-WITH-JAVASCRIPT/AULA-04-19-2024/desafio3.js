var resultado = document.getElementById('')

function calcular(){
    let velocidade = document.getElementById('numSpeed').value;

    if (velocidade > 600) {
        preco = velocidade*15
        console.log(`Você comprou ${livros} livro(s) e o total foi R$${preco},00`)
    }
    else {
        preco = livros*22 
        console.log(`Você comprou ${livros} livro(s) e o total foi R$${preco},00`)
    }
}
