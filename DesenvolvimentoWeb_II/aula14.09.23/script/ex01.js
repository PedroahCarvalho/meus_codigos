/* peça para o usuario digitar o preço de um produto e a quantidade mostre o valor total, sendo que se a pessoa comprar mais de  10 intens ela ganha 10% de desconto.
*/

function calcular() {
    var preco = document.getElementById("preco").value;
    var quant = document.getElementById("quantidade").value;
    var resp = document.getElementById("resp");
    var total = quant*preco;
    if (quant > 10){
        total = total - (total * 10/100);
    }
    resp.innerHTML = "Valor Total" + total.toFixed(2);
}

