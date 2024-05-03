function escolhaDoPC(){
    
    const jokeipo = ['Pedra', 'Papel', 'Tesoura']
    var numeroAleatorio = Math.floor(Math.random() * 3)
    return jokeipo[numeroAleatorio]
}

function jogar(escolhaDoJogador){
    var escolhaPC = escolhaDoPC()
    var resultado = ""

    if(escolhaPC === escolhaDoJogador){
        resultado = "EMPATE!"
    } else if (
        (escolhaDoJogador === "Pedra" && escolhaPC === "Tesoura") ||
        (escolhaDoJogador === "Papel" && escolhaPC === "Pedra") ||
        (escolhaDoJogador === "Tesoura" && escolhaPC === "Papel")
    ) {
        resultado = 'GANHOOOU!!! :D';
        document.getElementById('resultado').style.color = 'green';
    } else {
        resultado = 'PERDEU KKKK :(';
        document.getElementById('resultado').style.color = 'red';
    }

    document.getElementById('resultado').innerText = resultado
}



