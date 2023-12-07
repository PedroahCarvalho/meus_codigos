var esporte = []; // Array para armazenar esporte

document.addEventListener('DOMContentLoaded', function () {
    // Carregar esporte salvos ao iniciar a página
    abrirEsportes();
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

    esporte.push(treino);
    salvarEsportes()

    // Limpar campos de entrada
    limparCampos();

    // Atualizar tabela de esporte
    listarEsporte();
}

function listarEsporte() {
    var tabelaEsporte = document.getElementById('tabelaEsporte');
    tabelaEsporte.innerHTML = ''; // Limpar tabela

    // Cabeçalho da tabela
    var cabecalho = tabelaEsporte.insertRow();
    cabecalho.insertCell(0).textContent = 'Nome do esporte';
    cabecalho.insertCell(1).textContent = 'Preço do campo';
    cabecalho.insertCell(2).textContent = 'Duração do jogo';
    cabecalho.insertCell(3).textContent = 'Nome do Professor';
    cabecalho.insertCell(4).textContent = 'Descrição';
    cabecalho.insertCell(5).textContent = 'Ação'; // Nova coluna para o botão de exclusão

    // Adicionar esporte à tabela
    for (var i = 0; i < esporte.length; i++) {
        var linha = tabelaEsporte.insertRow();
        linha.insertCell(0).textContent = esporte[i].nome;
        linha.insertCell(1).textContent = esporte[i].preco;
        linha.insertCell(2).textContent = esporte[i].duracao;
        linha.insertCell(3).textContent = esporte[i].professor;
        linha.insertCell(4).textContent = esporte[i].descricao;

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
        excluirEsporte(indice);
    };
}

function excluirEsporte(indice) {
    esporte.splice(indice, 1);
    listarEsporte();
}

function limparCampos() {
    document.getElementById('nomeEsporte').value = '';
    document.getElementById('aluguelCampo').value = '';
    document.getElementById('duraçãoJogo').value = '';
    document.getElementById('professorjogo').value = '';
    document.getElementById('descriçãoJogo').value = '';
}

function salvarEsportes() {
    // Salvar esporte no localStorage
    localStorage.setItem('esporte', JSON.stringify(esporte));
}

function abrirEsportes() {
    // Recuperar esporte do localStorage ao iniciar a página
    var esporteSalvo = localStorage.getItem('esporte');
    if (esporteSalvo) {
        esporte = JSON.parse(esporteSalvo);
        listarEsporte();
    }
}

