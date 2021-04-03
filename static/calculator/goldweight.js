function LoanAmount()
{
    var weight = parseInt(document.getElementById("goldweight").value);
    var goldrate = parseInt(document.getElementById("goldvalue").value);
    var amt = document.getElementById("loanamount");
    amt.value = ((weight/10)*goldrate).toFixed(0);
    return amt.value;
}