var esportes = []; // Array para armazenar esportes

document.addEventListener('DOMContentLoaded', function () {
    // Carregar esportes salvos ao iniciar a página
    abriresportes();
});

function inserirEsporte() {
    var nomeEsporte = document.getElementById('nomeEsporte').value;
    var quantJogadores = document.getElementById('quantidadeJogadores').value;
    var dataJogo = document.getElementById('dataJogo');
    var treinador = document.getElementById('nomeTreinador').value;
    var quadra = document.getElementById('quadra').value;

    var curso = {
        nome: nomeEsporte,
        preco: quantJogadores,
        duracao: dataJogo,
        professor: treinador,
        descricao: quadra
    };

    esportes.push(curso);

    // Limpar campos de entrada
    limparCampos();

    // Atualizar tabela de esportes
    listarEsporte();
}

function listarEsporte() {
    var tabelaEsportes = document.getElementById('tabelaEsportes');
    tabelaEsportes.innerHTML = ''; // Limpar tabela

    // Cabeçalho da tabela
    var cabecalho = tabelaEsportes.insertRow();
    cabecalho.insertCell(0).textContent = 'Exporte';
    cabecalho.insertCell(1).textContent = 'Quantidade de jogadores';
    cabecalho.insertCell(2).textContent = 'Data do jogo';
    cabecalho.insertCell(3).textContent = 'Treinador';
    cabecalho.insertabelaesportestCell(4).textContent = 'Quadra';
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
    listarEsporte();
}

function limparCampos() {
    document.getElementById('nomeEsporte').value = '';
    document.getElementById('quantJogadores').value = '';
    document.getElementById('dataJogo').value = '';
    document.getElementById('treinador').value = '';
    document.getElementById('quadra').value = '';
}

function salvaresportes() {
    // Salvar esportes no localStorage
    localStorage.setItem('esportes', JSON.stringify(esportes));
}

function abriresportes() {
    // Recuperar esportes do localStorage ao iniciar a página
    var esportesSalvos = localStorage.getItem('esportes');
    if (esportesSalvos) {
        esportes = JSON.parse(esportesSalvos);
        listarEsporte();
    }
}

