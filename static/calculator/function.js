function CheckLoanAmount()
{
    var weight = parseInt(document.getElementById("GoldWeight").value);
    var goldrate = parseInt(document.getElementById("GoldValue").value);
    var amt = document.getElementById("LoanAmount");
    amt.value = ((weight/10)*goldrate).toFixed(0);

}
function CheckEMI()
    {
        var val1 = parseInt(document.getElementById("LoanAmount").value);
        var val2 = parseInt(document.getElementById("HomeLoanTenure").value);
        var interest = parseInt(document.getElementById("interest").value);
        var r = interest/(12*100); // to calculate rate percentage..
        var ansD = document.getElementById("HomeLoanEMI20");
        ansD.value = ((val1 * r * Math.pow((1+r),val2*12))/(Math.pow((1+r),val2*12)-1)).toFixed(0);
    }
var rangeSlider = function(){
  var slider = $('.range-slider'),
      range = $('.range-slider__range'),
      value = $('.range-slider__value');

slider.each(function(){

  value.each(function(){
      var value = $(this).prev().attr('value');
      $(this).html(value);
  });

  range.on('input', function(){
      $(this).next(value).html(this.value);
  });
});
};
rangeSlider();