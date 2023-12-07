 
var esportes = []; // Array para armazenar esportes

document.addEventListener('DOMContentLoaded', function () {
    // Carregar esportes salvos ao iniciar a página
    abrirEsportes();
});

function inserirEsporte() {
    var nomeEsporte = document.getElementById('nomeEsporte').value;
    var precoEsporte = document.getElementById('precoEsporte').value;
    var duracaoEsporte = document.getElementById('duracaoEsporte').value;
    var professorEsporte = document.getElementById('professorEsporte').value;
    var descricaoEsporte = document.getElementById('descricaoEsporte').value;

    var esporte = {
        nome: nomeEsporte,
        preco: precoEsporte,
        duracao: duracaoEsporte,
        professor: professorEsporte,
        descricao: descricaoEsporte
    };

    esportes.push(esporte);

    // Limpar campos de entrada
    limparCampos();

    // Atualizar tabela de esportes
    listarEsportes();
}

function listarEsportes() {
    var tabelaEsportes = document.getElementById('tabelaEsportes');
    tabelaEsportes.innerHTML = ''; // Limpar tabela

    // Cabeçalho da tabela
    var cabecalho = tabelaEsportes.insertRow();
    cabecalho.insertCell(0).textContent = 'Nome do Esporte';
    cabecalho.insertCell(1).textContent = 'Preço';
    cabecalho.insertCell(2).textContent = 'Tempo de Duração';
    cabecalho.insertCell(3).textContent = 'Nome do Professor';
    cabecalho.insertCell(4).textContent = 'Descrição';
    cabecalho.insertCell(5).textContent = 'Ação'; // Nova coluna para o botão de exclusão

    // Adicionar esportes à tabela
    for (var i = 0; i < esportes.length; i++) {
        var linha = tabelaEsportes.insertRow();
        linha.insertCell(0).textContent = esportes[i].nome;
        linha.insertCell(1).textContent = esportes[i].preco;
        linha.insertCell(2).textContent = esportes[i].duracao;
        linha.insertCell(3).textContent = esportes[i].professor;
        linha.insertCell(4).textContent = esportes[i].descricao;

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
    esportes.splice(indice, 1);
    listarEsportes();
}

function limparCampos() {
    document.getElementById('nomeEsporte').value = '';
    document.getElementById('precoEsporte').value = '';
    document.getElementById('duracaoEsporte').value = '';
    document.getElementById('professorEsporte').value = '';
    document.getElementById('descricaoEsporte').value = '';
}

function salvarEsportes() {
    // Salvar esportes no localStorage
    localStorage.setItem('esportes', JSON.stringify(esportes));
}

function abrirEsportes() {
    // Recuperar esportes do localStorage ao iniciar a página
    var esportesSalvos = localStorage.getItem('esportes');
    if (esportesSalvos) {
        esportes = JSON.parse(esportesSalvos);
        listarEsportes();
    }
}