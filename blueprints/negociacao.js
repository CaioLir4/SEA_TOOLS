
function calcularNegociacao() {
    var listaVencimentos = document.getElementById("vencimentos").getElementsByTagName("li");
    var valorBoleto = parseFloat(document.getElementById("valorBoleto").value);
    var dataSolicitacao = document.getElementById("dataSolicitacao").value;

    for (var i = 0; i < listaVencimentos.length; i++) {
        var dataVencimento = listaVencimentos[i].textContent;
        
        var resultado = Calculo_negociacao1(valorBoleto, dataSolicitacao, dataVencimento);

        console.log(resultado); 
    }
}
