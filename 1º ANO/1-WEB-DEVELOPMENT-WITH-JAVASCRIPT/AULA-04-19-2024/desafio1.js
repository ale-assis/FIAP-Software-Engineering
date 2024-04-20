var resultado = document.getElementById('resultado')

function calcular(){
    let livros = document.getElementById('numBooks').value;

    if (livros > 7) {
        preco = livros*15
        console.log(`Você comprou ${livros} livro(s) e o total foi R$${preco},00`)
    }
    else {
        preco = livros*22 
        console.log(`Você comprou ${livros} livro(s) e o total foi R$${preco},00`)
    }
}

