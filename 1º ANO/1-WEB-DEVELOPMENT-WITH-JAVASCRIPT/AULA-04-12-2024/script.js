var resultado = document.getElementById('resultado')

function somar(){
    /*alert('Clicoooouu!!!')*/
    var n1 = parseFloat(document.getElementById('numero1').value);
    var n2 = parseFloat(document.getElementById('numero2').value);

    var soma = n1 + n2

    // console.log(soma)
    resultado.innerText = `O resultado da soma é ${soma}`
}

function subtrair(){
    var n1 = parseFloat(document.getElementById('numero1').value);
    var n2 = parseFloat(document.getElementById('numero2').value);

    var subtrair = n1 - n2

    // console.log(soma)
    resultado.innerText = `O resultado da subtração é ${subtrair}`
}

function multiplicar(){
    var n1 = parseFloat(document.getElementById('numero1').value);
    var n2 = parseFloat(document.getElementById('numero2').value);

    var multiplicar = n1 * n2

    // console.log(soma)
    resultado.innerText = `O resultado da multiplicação é ${multiplicar}`
}

function dividir(){
    var n1 = parseFloat(document.getElementById('numero1').value);
    var n2 = parseFloat(document.getElementById('numero2').value);

    if (n2 === 0) {
        document.getElementById("result").innerText = "Erro: divisão por zero";
    } else {
        document.getElementById("result").innerText = n1 / n2;
    }

    var dividir = n1 / n2

    // console.log(soma)
    resultado.innerText = `O resultado da divisão é ${dividir}`
}

