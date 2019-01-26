(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)){ return; }
    js = d.createElement(s); js.id = id;
    js.onload = function(){alert("AdventureLanThon has been imported")};
    js.src = "////github.com/R0bertus/AdventureLanThon/alt/init.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'alt-engine'));