# AdventureLanThon
Adventure Land :: Browser Python Scripting Support

paste the run.js content in the CODE editor

```javascript
var _code=null;function loop(code,interval=0.25){_code=code;var load_script=function(d,s,id,code,src){var js,fjs=d.getElementsByTagName(s)[0];if(null==src){var request=new XMLHttpRequest;return request.open("GET","//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@3653131a280516c6479bd91034917dfa92bae968/alt/core.py",!1),request.onreadystatechange=function(){4===request.readyState&&(200===request.status||0==request.status)&&(ALT_core=request.responseText,_code=__BRYTHON__.python_to_js(ALT_core+_code),setInterval(function(){eval(_code)},1e3*interval))},void request.send(null)}return d.getElementById(id)?void("brython-sdk"==id?load_script(document,"script","brython-stdlib",code,"//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@749ac07f2fa6b376cb85f056d3abb39869d729a8/brython/brython_stdlib.js"):"brython-stdlib"==id&&load_script(document,"script",null,code,null)):void(js=d.createElement(s),js.id=id,js.onload=function(){"brython-sdk"==id?load_script(document,"script","brython-stdlib",code,"//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@749ac07f2fa6b376cb85f056d3abb39869d729a8/brython/brython_stdlib.js"):"brython-stdlib"==id&&load_script(document,"script",null,code,null)},js.src=src,fjs.parentNode.insertBefore(js,fjs))};load_script(document,"script","brython-sdk",code,"//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@749ac07f2fa6b376cb85f056d3abb39869d729a8/brython/brython.min.js")}

loop(`
# Python code starts here
# this will be a 1-1 relationship of the runner_functions
set_message("Hello World", random_color())
`)
```
