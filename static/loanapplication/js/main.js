$(function(){
    $("#form-register").validate({
        rules: {
            password : {
                required : true,
            },
            confirm_password: {
                equalTo: "#password"
            }
        },
        messages: {
            username: {
                required: "Please provide an username"
            },
            email: {
                required: "Please provide an email"
            },
            password: {
                required: "Please provide a password"
            },
            confirm_password: {
                required: "Please provide a password",
                equalTo: "Please enter the same password"
            }
        }
    });
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",
        // enableAllSteps: true,
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate : '<div class="title">#title#</div>',
        labels: {
            previous : 'Back',
            next : '<i class="zmdi zmdi-arrow-right"></i>',
            finish : '<i class="zmdi zmdi-arrow-right"></i>',
            current : ''
        },
        onStepChanging: function (event, currentIndex, newIndex) { 
            var username = $('#username').val();
            var email = $('#email').val();
            var cardtype = $('#cardtype').val();
            var cardnumber = $('#cardnumber').val();
            var cvc = $('#cvc').val();
            var month = $('#expmonth').val();
            var year = $('#expyear').val();

            $('#username-val').text(username);
            $('#email-val').text(email);
            $('#cardtype-val').text(cardtype);
            $('#cardnumber-val').text(cardnumber);
            $('#cvc-val').text(cvc);
            $('#expmonth-val').text(month);
            $('#expyear-val').text(year);

            $("#form-register").validate().settings.ignore = ":disabled,:hidden";
            return $("#form-register").valid();
        }
    });
});
