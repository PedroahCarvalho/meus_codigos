/* 
2- peça para o usuario digitar 2 notas. Clacule a media e mostre se o aluno foi aprovado, reprovado ou se ficou de prova final. Para ser aprovado a nota tem que ser maior que 40 ficam de prova final. Noatas abaixo de 40 são reprovado
*/

function calcular(){
    var nota01 = document.getElementById("nota01").value;
    var nota02 = document.getElementById("nota02").value;
    var resp = document.getElementById("resp");
    var mediafinal = parseFloat(nota01 + nota02) /2;
    if(mediafinal >= 70){
        resp.innerHTML = "Aluno aprovado";
    }else if(mediafinal >= 40){
        resp.innerHTML = "Aluno de Prova final.";
    }else{
        resp.innerHTML = "aluno reprovado ";
    }
}