$(document).ready(function(){
    var controller = new ScrollMagic.Controller();
    var ourScene = new ScrollMagic.Scene({
    triggerEvent: '.fade-in',
    reverse: false
    })
        .setClassToggle('.fade-in','show')
        .addTo(controller);
});