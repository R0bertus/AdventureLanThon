var loading = null;
var loop = function(code, interval=0.25) {
    (function(d, s, id){
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)){ _loop(code, interval); return; }
        js = d.createElement(s); js.id = id;
        js.onload = function(){console.log("AdventureLanThon has been imported")};
        js.src = "//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@749ac07f2fa6b376cb85f056d3abb39869d729a8/alt/init.js";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'alt-engine'))
    if(loading == null) {
        loading = setInterval(function(){
            if(_loop != null) {
                _loop(code, interval)
            }
            clearInterval(loading)
        }, 100);
    }
};

var code = `
set_message("ALT loaded")
`

loop(code)