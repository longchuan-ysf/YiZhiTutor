(() => {
    var t = {
        626: () => {
            layui.define(["jquery"], (function (t) {
                var e = layui.jquery, i = {
                    bind: function (t, o) {
                        e(t).bind("contextmenu", (function (t) {
                            return i.show(o, t.clientX, t.clientY, t), !1
                        }))
                    }, show: function (t, o, n, c) {
                        var r = '<div class="ctxMenu" style="left: ' + o + "px; top: " + n + 'px;">';
                        r += i.getHtml(t, ""), r += "   </div>", i.remove(), e("body").append(r);
                        var u = e(".ctxMenu");
                        o + u.outerWidth() > i.getPageWidth() && (o -= u.outerWidth()), n + u.outerHeight() > i.getPageHeight() && (n -= u.outerHeight()) < 0 && (n = 0), u.css({
                            top: n,
                            left: o
                        }), i.setEvents(t, c), e(".ctxMenu-item").on("mouseenter", (function (t) {
                            if (t.stopPropagation(), e(this).parent().find(".ctxMenu-sub").css("display", "none"), e(this).hasClass("haveMore")) {
                                var o = e(this).find(">a"), n = e(this).find(">.ctxMenu-sub"),
                                    c = o.offset().top - e("body,html").scrollTop(),
                                    r = o.offset().left + o.outerWidth() - e("body,html").scrollLeft();
                                r + n.outerWidth() > i.getPageWidth() && (r = o.offset().left - n.outerWidth()), c + n.outerHeight() > i.getPageHeight() && (c = c - n.outerHeight() + o.outerHeight()) < 0 && (c = 0), e(this).find(">.ctxMenu-sub").css({
                                    top: c,
                                    left: r,
                                    display: "block"
                                })
                            }
                        }))
                    }, remove: function () {
                        for (var t = parent.window.frames, e = 0; e < t.length; e++) {
                            var i = t[e];
                            try {
                                i.layui.jquery("body>.ctxMenu").remove()
                            } catch (t) {
                            }
                        }
                        try {
                            parent.layui.jquery("body>.ctxMenu").remove()
                        } catch (t) {
                        }
                    }, setEvents: function (t, i) {
                        function o(t, e) {
                            for (var i = 0; i < e.length; i++) {
                                var n = e[i];
                                if (t == n.itemId) return n;
                                if (n.subs && n.subs.length > 0) {
                                    var c = o(t, n.subs);
                                    if (c) return c
                                }
                            }
                        }

                        e(".ctxMenu").off("click").on("click", "[lay-id]", (function (n) {
                            var c = o(e(this).attr("lay-id"), t);
                            c.click && c.click(n, i)
                        }))
                    }, getHtml: function (t, e) {
                        for (var o = "", n = 0; n < t.length; n++) {
                            var c = t[n];
                            c.itemId = "ctxMenu-" + e + n, c.subs && c.subs.length > 0 ? (o += '<div class="ctxMenu-item haveMore" lay-id="' + c.itemId + '">', o += "<a>", c.icon && (o += '<i class="' + c.icon + ' ctx-icon"></i>'), o += c.name, o += '<i class="layui-icon layui-icon-right icon-more"></i>', o += "</a>", o += '<div class="ctxMenu-sub" style="display: none;">', o += i.getHtml(c.subs, e + n), o += "</div>") : (o += '<div class="ctxMenu-item" lay-id="' + c.itemId + '">', o += "<a>", c.icon && (o += '<i class="' + c.icon + ' ctx-icon"></i>'), o += c.name, o += "</a>"), o += "</div>", 1 == c.hr && (o += "<hr/>")
                        }
                        return o
                    }, getCommonCss: function () {
                        return ".ctxMenu, .ctxMenu-sub {        max-width: 250px;        min-width: 110px;        background: white;        border-radius: 2px;        padding: 5px 0;        white-space: nowrap;        position: fixed;        z-index: 2147483647;        box-shadow: 0 2px 4px rgba(0, 0, 0, .12);        border: 1px solid #d2d2d2;        overflow: visible;   }   .ctxMenu-item {        position: relative;   }   .ctxMenu-item > a {        font-size: 14px;        color: #666;        padding: 0 26px 0 35px;        cursor: pointer;        display: block;        line-height: 36px;        text-decoration: none;        position: relative;   }   .ctxMenu-item > a:hover {        background: #f2f2f2;        color: #666;   }   .ctxMenu-item > a > .icon-more {        position: absolute;        right: 5px;        top: 0;        font-size: 12px;        color: #666;   }   .ctxMenu-item > a > .ctx-icon {        position: absolute;        left: 12px;        top: 0;        font-size: 15px;        color: #666;   }   .ctxMenu hr {        background-color: #e6e6e6;        clear: both;        margin: 5px 0;        border: 0;        height: 1px;   }   .ctx-ic-lg {        font-size: 18px !important;        left: 11px !important;    }"
                    }, getPageHeight: function () {
                        return document.documentElement.clientHeight || document.body.clientHeight
                    }, getPageWidth: function () {
                        return document.documentElement.clientWidth || document.body.clientWidth
                    }
                };
                e(document).off("click.ctxMenu").on("click.ctxMenu", (function () {
                    i.remove()
                })), e(document).off("click.ctxMenuMore").on("click.ctxMenuMore", ".ctxMenu-item", (function (t) {
                    e(this).hasClass("haveMore") ? void 0 !== t && (t.preventDefault(), t.stopPropagation()) : i.remove()
                })), e("head").append('<style id="ew-css-ctx">' + i.getCommonCss() + "</style>"), t("contextMenu", i)
            }))
        }
    }, e = {};
    !function i(o) {
        var n = e[o];
        if (void 0 !== n) return n.exports;
        var c = e[o] = {exports: {}};
        return t[o](c, c.exports, i), c.exports
    }(626)
})();