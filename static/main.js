
$(function() { 
    $("#answer").hide();

    $("#show_btn").click(() => {
        console.log("show button is clicked...");
        
        $("#answer").show();
    });
})