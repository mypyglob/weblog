/**
 * Created by sunwell on 16/7/4.
 */
var _vds = _vds || [];
window._vds = _vds;

var allcookies = document.cookie;

// 定义一个函数，用来读取特定的cookie值。

function getCookie(cookie_name) {
    var allcookies = document.cookie;
    var cookie_pos = allcookies.indexOf(cookie_name);   //索引的长度
    if (cookie_pos != -1) {
        cookie_pos += cookie_name.length + 1;
        var cookie_end = allcookies.indexOf(";", cookie_pos);
        if (cookie_end == -1) {
            cookie_end = allcookies.length;
        }
        var value = unescape(allcookies.substring(cookie_pos, cookie_end)); //这里就可以得到你想要的cookie的值了。。。
    }
    return value;
}


(function () {
    _vds.push(['setAccountId', '3d82bb7757134159ae903485602ee950']);

    var js = getCookie("gi_static");
    if (js != undefined) {
        var ustr = eval("(" + js + ")");
        var user = eval("(" + ustr + ")");
        _vds.push(['setCS1', 'user_id', user.user_id]);
        _vds.push(['setCS2', 'user_name', user.user_name]);
        _vds.push(['setCS3', 'email', user.user_email]);
    }

    (function () {
        var vds = document.createElement('script');
        vds.type = 'text/javascript';
        vds.async = true;
        vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(vds, s);
    })();
})();