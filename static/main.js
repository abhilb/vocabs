
$(function() { 
    $("#answer").css('visibility', 'hidden');

    $("#show_btn").click(() => {
        console.log("show button is clicked...");
        
        $("#answer").css('visibility', 'visible');
    });
})