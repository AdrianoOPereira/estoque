
function teste(){
    alert('funciona mesmo')
}



// Função para calcular o valor total
function calcularTotal() {
    var qtde = parseFloat(document.getElementById('Qtde').value) || 0;
    var unitario = parseFloat(document.getElementById('Unitario').value) || 0;
    var total = qtde * unitario;
    document.getElementById('Total').value = total.toFixed(2);
}

document.addEventListener('DOMContentLoaded', function () {
    var btnAbrirModal = document.getElementById('btnAbrirModal');
    var btnFecharModal = document.getElementById('btnFecharModal');
    var modal = document.getElementById('cadastroModal');

    btnAbrirModal.onclick = function () {
        modal.showModal();
    };

    btnFecharModal.onclick = function () {
        modal.close();
    };

        // Adicione um ouvinte de evento de mudança para calcular o total
    document.getElementById('Qtde').addEventListener('input', calcularTotal);
    document.getElementById('Unitario').addEventListener('input', calcularTotal);
});
