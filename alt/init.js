var _code = null;
function _loop(code, interval=0.25) {
    _code = code;
    var load_script = function (d, s, id, code, src) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (src == null) {
            var request = new XMLHttpRequest();
            request.open("GET", "//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@3653131a280516c6479bd91034917dfa92bae968/alt/core.py", false);
            request.onreadystatechange = function () {
                if(request.readyState === 4) {
                    if(request.status === 200 || request.status == 0) {
                        ALT_core = request.responseText;
                        _code = __BRYTHON__.python_to_js(ALT_core + _code);
                        setInterval(function () {
                        }, interval * 1000);
                    }
                }
            }
            request.send(null);
            return;
        }
        if (d.getElementById(id)) {
            if (id == "brython-sdk") {
                load_script(document, 'script', 'brython-stdlib', code, "//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@3b0216df4ce31ac5777aaf78a4a9b1aeef6d1098/brython/brython_stdlib.js")
            } else if (id == "brython-stdlib") {
                load_script(document, 'script', null, code, null)
            }
            return;
        }
        js = d.createElement(s);
        js.id = id;
        js.onload = function () {
            if (id == "brython-sdk") {
                load_script(document, 'script', 'brython-stdlib', code, "//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@3b0216df4ce31ac5777aaf78a4a9b1aeef6d1098/brython/brython_stdlib.js")
            } else if (id == "brython-stdlib") {
                load_script(document, 'script', null, code, null)
            }
        };
        js.src = src;
        fjs.parentNode.insertBefore(js, fjs);
    }
    load_script(document, 'script', 'brython-sdk', code, "//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@aed59b5bc175bd56fa5d8edb3d5fcb5938905cfe/brython/brython.js")
}