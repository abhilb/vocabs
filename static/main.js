
$(function() { 
    $("#answer").css('visibility', 'hidden');
    $("#form_btn").hide();

    $("#show_btn").click(() => {
        console.log("show button is clicked...");        
        $("#answer").css('visibility', 'visible');
        $("#show_btn").hide();
        $("#form_btn").show();
    });
})