# AdventureLanThon
Adventure Land :: Browser Python Scripting Support

paste the run.js content in the CODE editor

```javascript
var _code=null;function run(code,interval=-1){_code=code;var load_script=function(d,s,id,code,src){var js,fjs=d.getElementsByTagName(s)[0];if(null==src){var request=new XMLHttpRequest;return request.open("GET","//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@e354490124e4edb1a0cc5f4831240f2afe43ad10/alt/core.py",!1),request.onreadystatechange=function(){4===request.readyState&&(200===request.status||0==request.status)&&(ALT_core=request.responseText,_code=__BRYTHON__.python_to_js(ALT_core+_code),-1==interval?eval(_code):setInterval(function(){eval(_code)},1e3*interval))},void request.send(null)}return d.getElementById(id)?void("brython-sdk"==id?load_script(document,"script","brython-stdlib",code,"//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@749ac07f2fa6b376cb85f056d3abb39869d729a8/brython/brython_stdlib.js"):"brython-stdlib"==id&&load_script(document,"script",null,code,null)):void(js=d.createElement(s),js.id=id,js.onload=function(){"brython-sdk"==id?load_script(document,"script","brython-stdlib",code,"//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@749ac07f2fa6b376cb85f056d3abb39869d729a8/brython/brython_stdlib.js"):"brython-stdlib"==id&&load_script(document,"script",null,code,null)},js.src=src,fjs.parentNode.insertBefore(js,fjs))};load_script(document,"script","brython-sdk",code,"//cdn.jsdelivr.net/gh/R0bertus/AdventureLanThon@749ac07f2fa6b376cb85f056d3abb39869d729a8/brython/brython.min.js")}function loop(a,b=0.25){run(a,b)}

// run(code) executes the code once

run(`
alt = AdventureLanThon()
alt.buy_potions(health=1, mana=2)
`)

// to loop a function use loop(code, interval)
// run(code) could be used to initialize variables 
// and afterwards you can loop the main code with loop(code)
```
