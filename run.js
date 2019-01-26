var loading = null;
var loop = function(code, interval=0.25) {
    (function(d, s, id){
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)){ _loop(code, interval); return; }
        js = d.createElement(s); js.id = id;
        js.onload = function(){console.log("AdventureLanThon has been imported")};
        js.src = "//raw.githubusercontent.com/R0bertus/AdventureLanThon/master/alt/init.js";
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
# Here you can script in python
# All functionality is a 1-1 relationship
# with the official runner functions from  https://github.com/kaansoral/adventureland
# Unofficial documentation -> https://nexusnull.github.io/adventureland/index.html
# ***This is a work in progress***

set_message("ALT loaded")

`