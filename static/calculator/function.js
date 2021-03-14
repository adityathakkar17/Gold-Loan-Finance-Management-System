function CheckEMI()
    {
        var val1 = parseInt(document.getElementById("HomeLoanAmount").value);
        var val2 = parseInt(document.getElementById("HomeLoanTenure").value);
        var r = 9.5/(12*100); // to calculate rate percentage..
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