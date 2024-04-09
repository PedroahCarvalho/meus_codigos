CREATE DATABASE loja;
USE loja;
CREATE TABLE marca(
    id_marca INT NOT NULL AUTO_INCREMENT,
    nome_marca VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_marca)
);
CREATE TABLE produto(
    id_produto INT NOT NULL AUTO_INCREMENT,
    nome_produto VARCHAR(50) NOT NULL,
    preco_produto FLOAT NOT NULL,
    id_marca INT NOT NULL,
    PRIMARY KEY(id_produto),
    FOREIGN KEY(id_marca) REFERENCES marca(id_marca)
);

CREATE TABLE venda_produto(
    id_venda_produto INT NOT NULL AUTO_INCREMENT,
    id_produto INT NOT NULL,
    id_venda INT NOT NULL,
    PRIMARY KEY(id_venda_produto),
    FOREIGN KEY(id_produto) REFERENCES produto(id_produto),
    FOREIGN KEY(id_venda) REFERENCES vendedor(id_venda)
);
CREATE TABLE venda(
    id_venda INT NOT NULL AUTO_INCREMENT,
    numero_nfe INT NOT NULL,
    quantidade INT NOT NULL,
    valor FLOAT NOT NULL,
    comissão INT NOT NULL,
    id_vendedor INT NOT NULL,
    PRIMARY KEY(id_venda),
    FOREIGN KEY(id_vendedor) REFERENCES vendedor(id_vendedor)

);
CREATE TABLE cliente(
    id_cliente INT NOT NULL AUTO_INCREMENT,
    nome_cliente VARCHAR(50) NOT NULL,
    cpf_cliente VARCHAR(11) NOT NULL,
    logradouro VARCHAR(100) NOT NULL,
    numero INT NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    telefone VARCHAR(100) NOT NULL,
    id_cidade INT NOT NULL,
    PRIMARY KEY(id_cliente)
    FOREIGN KEY(id_cidade) REFERENCES cidade(id_cidade)
);

CREATE TABLE cidade(
    id_cidade INT NOT NULL AUTO_INCREMENT,
    nome_cidade VARCHAR(50) NOT NULL,
    cep INT NOT NULL,
    uf CHAR(2) NOT NULL,
    PRIMARY KEY(id_cidade),
);

CREATE TABLE vendedor(
    id_vendedor INT NOT NULL AUTO_INCREMENT,
    nome_vendedor VARCHAR(50) NOT NULL,
    cpf_vendedor VARCHAR(11) NOT NULL,
    logradouro VARCHAR(100) NOT NULL,
    numero INT NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    telefone VARCHAR(100) NOT NULL,
    id_cidade INT NOT NULL,
    PRIMARY KEY(id_vendedor)
    FOREIGN KEY(id_cidade) REFERENCES cidade(id_cidade)
);

CREATE TABLE cliente_venda(
    id_cliente_venda INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_venda INT NOT NULL,
    PRIMARY KEY(id_cliente_venda),
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY(id_venda) REFERENCES venda(id_venda)
);

CREATE TABLE cliente_produto(
    id_cliente_produto INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_produto INT NOT NULL,
    PRIMARY KEY(id_cliente_produto),
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY(id_produto) REFERENCES produto(id_produto)
);

CREATE TABLE cliente_venda_produto(
    id_cliente_venda_produto INT NOT NULL AUTO_INCREMENT,
    id_cliente_produto INT NOT NULL,
    id_venda_produto INT NOT NULL,
    PRIMARY KEY(id_cliente_venda_produto),
    FOREIGN KEY(id_cliente_produto) REFERENCES cliente_produto(id_cliente_produto),
    FOREIGN KEY(id_venda_produto) REFERENCES venda_produto(id_venda),
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY(id_venda) REFERENCES venda(id_venda)
);
CREATE TABLE contas_a_receber(
    id_conta_a_receber INT NOT NULL AUTO_INCREMENT,
    data DATETIME NOT NULL,
    valor FLOAT NOT NULL,
    vencimento DATA NOT NULL,
    pagamento DATETIME NOT NULL,
);

CREATE TABLE cliente_contas(
    id_cliente_contas INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_conta_a_receber INT NOT NULL,
    PRIMARY KEY(id_cliente_contas),
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY(id_conta_a_receber) REFERENCES contas_a_receber(id_conta_a_receber),
);
CREATE TABLE compras(
    id_compra INT NOT NULL AUTO_INCREMENT,
    data DATETIME NOT NULL,
    quantidade INT NOT NULL,
    valor FLOAT NOT NULL,
    comissão INT NOT NULL,
);
CREATE TABLE fornecedor(
    id_fornecedor INT NOT NULL AUTO_INCREMENT,
    nome_fornecedor VARCHAR(50) NOT NULL,
    cnpj_fornecedor VARCHAR(14) NOT NULL,
    logradouro VARCHAR(100) NOT NULL,
    numero INT NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cep char(2) NOT NULL,
);

CREATE TABLE fornecedor_compra(
    id_fornecedor_compra INT NOT NULL AUTO_INCREMENT,
    id_fornecedor INT NOT NULL,
    id_compra INT NOT NULL,
    PRIMARY KEY(id_fornecedor_compra),
    FOREIGN KEY(id_fornecedor) REFERENCES fornecedor(id_fornecedor),
    FOREIGN KEY(id_compra) REFERENCES compras(id_compra)
);

CREATE TABLE contas_a_apagar(
    id_conta_a_apagar INT NOT NULL AUTO_INCREMENT,
    data DATETIME NOT NULL,
    valor FLOAT NOT NULL,
    vencimento DATA NOT NULL,
    pagamento DATETIME NOT NULL,
    valor_pago FLOAT NOT NULL,
    PRIMARY KEY(id_conta_a_apagar)

);
CREATE TABLE caixa(
    id_caixa INT NOT NULL AUTO_INCREMENT,
    data DATETIME NOT NULL,
    descrição VARCHAR(255) NOT NULL,
    valor FLOAT NOT NULL,
    debito_credito VARCHAR(50) NOT NULL,
    id_contas_a_pagar INT NOT NULL,
    PRIMARY KEY(id_caixa),
    FOREIGN KEY(id_contas_a_pagar) REFERENCES contas_a_apagar(id_contas_a_pagar)
);
CREATE TABLE usuario(
    id_usuario INT NOT NULL AUTO_INCREMENT,
    nome_usuario VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_usuario)
);
