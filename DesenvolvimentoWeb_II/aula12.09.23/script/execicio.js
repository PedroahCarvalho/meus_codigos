function calcular(){
    var idade =document.getElementById("idade").value;
    var resp = document.getElementById("resp");
    if((idade >= 18) && (idade <= 65)){
        resp.innerHTML = "Voto obrigatorio";
    }else if(idade < 16){
        resp.innerHTML= "Não vota";
    }else{
        resp.innerHTML= "Voto facultativo";
    }
    
}