const btnCriar = document.querySelector("#btnCriar")
const listaFilmes = document.querySelector('#listaFilmes')
const inputUsuario = document.querySelector('#inputUsuario')

const filmes = [
    {
        nome: "Tropa de Elite",
        ano: 2008,
        diretor: "José Padilha"
    },
    {
        nome: "Carros",
        ano: 2006,
        diretor: "John Lasseter"
    },
    {
        nome: "Titanic",
        ano: 1997,
        diretor: "James Cameron"
    }
]

btnCriar.addEventListener('click', function (infosDoEvento){
    infosDoEvento.preventDefault();

    let novoFilme = document.createElement('li')
    novoFilme.innerText = inputUsuario.value
    novoFilme.style.color = 'red'
    novoFilme.classList.add('itens-lista')
    novoFilme.classList.remove('itens-lista')

    let btnEditar = document.createElement('button')
    btnEditar.innerHTML = <'Editar'>
    btnEditar.addEventListener('click', function(){
        novoFilme.classList.toggle('esconder')
    })
    listaFilmes.append(btnEditar)
    // criar um carrosel
    // let imagem = document.createElement('img')
    // imagem.src = "link da imagem"
    novoFilme.innerHTML = `
    <h1> ${inputUsuario.value}</h1>
    <p> Avaliação: 8.0</p>
    <span> Atores</span>`

    listaFilmes.append(novoFilme)
})

// CREATE
function criarFilme(){
    const filmeNovo = {
        nome: inputUsuario.value,
        ano: inputAno.value,
        diretor: inputDiretor.value
    }

    filmes.unshift(filmeNovo)

    renderizarNaTela()
}

// READ
window.onload = renderizarNaTela()

function renderizarNaTela(){
    filmes.forEach(
        filme => {
            let novoFilme = document.createElement('li')
            novoFilme.innerHTML = `
            <h1>${filme.nome}</h1>
            <p>${filme.ano}</p>
            <h3>${filme.diretor}</h3>
            <button> Editar </button>`

            listaFilmes.append(novoFilme)
        }
    )
}

// UPDATE

// DELETE