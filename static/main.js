const zeroAngle = "rotateY(0deg)";
const flipAngle = "rotateY(180deg)";
var angle = zeroAngle;

$(function() {
  $(".flip-card").click(() => {
    console.log("clicked");
    if(angle === zeroAngle) {
      $(".flip-card-inner").css("transform", flipAngle);
      angle = flipAngle;
    } else {
      $(".flip-card-inner").css("transform", zeroAngle);         angle = zeroAngle;
    }
  });
});