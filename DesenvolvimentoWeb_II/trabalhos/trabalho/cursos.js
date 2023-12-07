var cursos = []; // Array para armazenar cursos

document.addEventListener('DOMContentLoaded', function () {
    // Carregar cursos salvos ao iniciar a página
    abrirCursos();
});

function inserirEsporte() {
    var nomeEsporte = document.getElementById('nomeEsporte').value;
    var aluguelCampo = document.getElementById('aluguelCampo').value;
    var duraçãoJogo = document.getElementById('duraçãoJogo').value;
    var professorjogo = document.getElementById('professorjogo').value;
    var descriçãoJogo = document.getElementById('descriçãoJogo').value;

    var treino = {
        nome: nomeEsporte,
        preco: aluguelCampo,
        duracao: duraçãoJogo,
        professor: professorjogo,
        descricao: descriçãoJogo
    };

    cursos.push(treino);

    // Limpar campos de entrada
    limparCampos();

    // Atualizar tabela de cursos
    listarEsporte();
}

function listarEsporte() {
    var tabelaCursos = document.getElementById('tabelaCursos');
    tabelaCursos.innerHTML = ''; // Limpar tabela

    // Cabeçalho da tabela
    var cabecalho = tabelaCursos.insertRow();
    cabecalho.insertCell(0).textContent = 'Nome do esporte';
    cabecalho.insertCell(1).textContent = 'Preço do campo';
    cabecalho.insertCell(2).textContent = 'Duração do jogo';
    cabecalho.insertCell(3).textContent = 'Nome do Professor';
    cabecalho.insertCell(4).textContent = 'Descrição';
    cabecalho.insertCell(5).textContent = 'Ação'; // Nova coluna para o botão de exclusão

    // Adicionar cursos à tabela
    for (var i = 0; i < cursos.length; i++) {
        var linha = tabelaCursos.insertRow();
        linha.insertCell(0).textContent = cursos[i].nome;
        linha.insertCell(1).textContent = cursos[i].preco;
        linha.insertCell(2).textContent = cursos[i].duracao;
        linha.insertCell(3).textContent = cursos[i].professor;
        linha.insertCell(4).textContent = cursos[i].descricao;

        // Adicionar botão de exclusão
        var cellAcao = linha.insertCell(5);
        var btnExcluir = document.createElement('button');
        btnExcluir.textContent = 'Excluir';
        btnExcluir.addEventListener('click', criarFuncaoExcluir(i));
        cellAcao.appendChild(btnExcluir);
    }
}

function criarFuncaoExcluir(indice) {
    return function () {
        excluirCurso(indice);
    };
}

function excluirCurso(indice) {
    cursos.splice(indice, 1);
    listarEsporte();
}

function limparCampos() {
    document.getElementById('nomeEsporte').value = '';
    document.getElementById('aluguelCampo').value = '';
    document.getElementById('duraçãoJogo').value = '';
    document.getElementById('professorjogo').value = '';
    document.getElementById('descriçãoJogo').value = '';
}

function salvarCursos() {
    // Salvar cursos no localStorage
    localStorage.setItem('cursos', JSON.stringify(cursos));
}

function abrirCursos() {
    // Recuperar cursos do localStorage ao iniciar a página
    var cursosSalvos = localStorage.getItem('cursos');
    if (cursosSalvos) {
        cursos = JSON.parse(cursosSalvos);
        listarEsporte();
    }
}

