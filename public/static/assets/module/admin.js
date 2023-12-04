(() => {
    var e = {
        199: () => {
            layui.define(["layer"],
                (function (e) {
                    var a = layui.jquery,
                        t = layui.layer,
                        i = layui.cache,
                        n = ".layui-layout-admin>.layui-body",
                        o = n + ">.layui-tab", l = ".layui-layout-admin>.layui-side>.layui-side-scroll",
                        s = ".layui-layout-admin>.layui-header",
                        r = {
                            version: "3.1.8",
                            layerData: {},

                            flexible: function (e) {
                                if (window !== top && !r.isTop() && top.layui && top.layui.admin)
                                    return top.layui.admin.flexible(e);
                                var t = a(".layui-layout-admin"),
                                    i = t.hasClass("admin-nav-mini");
                                void 0 === e && (e = i),
                                i === e && (
                                    window.sideFlexTimer && clearTimeout(window.sideFlexTimer),
                                        t.addClass("admin-side-flexible"),
                                        window.sideFlexTimer = setTimeout(
                                            (function () {
                                                t.removeClass("admin-side-flexible")
                                            }),
                                            600),
                                        e ? (r.hideTableScrollBar(),
                                            t.removeClass("admin-nav-mini")) : t.addClass("admin-nav-mini"),
                                        layui.event.call(this, "admin", "flexible({*})", {expand: e}))
                            },

                            activeNav: function (e) {
                                if (window !== top && !r.isTop() && top.layui && top.layui.admin)
                                    return top.layui.admin.activeNav(e);
                                if (!e)
                                    return console.warn("active url is null");
                                a(l + ">.layui-nav .layui-nav-item .layui-nav-child dd.layui-this").removeClass("layui-this"),
                                    a(l + ">.layui-nav .layui-nav-item.layui-this").removeClass("layui-this");
                                var t = a(l + '>.layui-nav a[lay-href="' + e + '"]');
                                if (0 === t.length)
                                    return console.warn(e + " not found");
                                var i = a(".layui-layout-admin").hasClass("admin-nav-mini");

                                if ("_all" === a(l + ">.layui-nav").attr("lay-shrink")) {
                                    var n = t.parent("dd").parents(".layui-nav-child");
                                    i || a(l + ">.layui-nav .layui-nav-itemed>.layui-nav-child").not(n).css("display", "block").slideUp(
                                        "fast",
                                        (function () {
                                            a(this).css("display", "")
                                        })),
                                        a(l + ">.layui-nav .layui-nav-itemed").not(n.parent()).removeClass("layui-nav-itemed")
                                }
                                t.parent().addClass("layui-this");

                                var o = t.parent("dd").parents(".layui-nav-child").parent();
                                if (!i) {
                                    var c = o.not(".layui-nav-itemed").children(".layui-nav-child");
                                    c.slideDown(
                                        "fast",
                                        (function () {
                                                if (a(this).is(c.last())) {
                                                    c.css("display", "");
                                                    var e = t.offset().top + t.outerHeight() + 30 - r.getPageHeight(),
                                                        i = 115 - t.offset().top;
                                                    e > 0 ? a(l).animate(
                                                        {scrollTop: a(l).scrollTop() + e},
                                                        300
                                                    ) : i > 0 && a(l).animate({scrollTop: a(l).scrollTop() - i}, 300)
                                                }
                                            }
                                        ))
                                }
                                o.addClass("layui-nav-itemed"), a('ul[lay-filter="admin-side-nav"]').addClass("layui-hide");

                                var d = t.parents(".layui-nav");
                                d.removeClass("layui-hide"),
                                    a(s + ">.layui-nav>.layui-nav-item").removeClass("layui-this"),
                                    a(s + '>.layui-nav>.layui-nav-item>a[nav-bind="' + d.attr("nav-id") + '"]').parent().addClass("layui-this")
                            },

                            popupRight: function (e) {
                                return e.anim = -1,
                                    e.offset = "r",
                                    e.move = !1,
                                    e.fixed = !0,
                                void 0 === e.area && (e.area = "336px"),
                                void 0 === e.title && (e.title = !1),
                                void 0 === e.closeBtn && (e.closeBtn = !1),
                                void 0 === e.shadeClose && (e.shadeClose = !0),
                                void 0 === e.skin && (e.skin = "layui-anim layui-anim-rl layui-layer-adminRight"),
                                    r.open(e)
                            },

                            open: function (e) {
                                e.content && 2 === e.type && (e.url = void 0),
                                !e.url || 2 !== e.type && void 0 !== e.type || (e.type = 1),
                                void 0 === e.area && (e.area = 2 === e.type ? ["360px", "300px"] : "360px"),
                                void 0 === e.offset && (e.offset = "70px"),
                                void 0 === e.shade && (e.shade = .1),
                                void 0 === e.fixed && (e.fixed = !1),
                                void 0 === e.resize && (e.resize = !1),
                                void 0 === e.skin && (e.skin = "layui-layer-admin");
                                var n = e.end;
                                /*
                                * 首先计算 e.end 的值，但不使用这个值
                                * 然后计算 e.url 的值
                                * if 语句的条件判斷实际上是基于 e.url 的值
                                * */
                                if (e.end = function () {
                                    t.closeAll("tips"), n && n()
                                }, e.url) {
                                    var o = e.success;
                                    e.success = function (t, i) {
                                        a(t).data("tpl", e.tpl || ""),
                                            r.reloadLayer(i, e.url, o)
                                    }
                                } else {
                                    e.tpl && e.content && (e.content = r.util.tpl(e.content, e.data, i.tplOpen, i.tplClose));
                                }
                                var l = t.open(e);
                                return e.data && (r.layerData["d" + l] = e.data), l
                            },

                            getLayerData: function (e, a) {
                                if (void 0 === e)
                                    return void 0 === (e = parent.layer.getFrameIndex(window.name)) ? null : parent.layui.admin.getLayerData(parseInt(e), a);
                                if (isNaN(e) && (e = r.getLayerIndex(e)), void 0 !== e) {
                                    var t = r.layerData["d" + e];
                                    return a && t ? t[a] : t
                                }
                            },

                            putLayerData: function (e, a, t) {
                                if (void 0 === t)
                                    return void 0 === (t = parent.layer.getFrameIndex(window.name)) ? void 0 : parent.layui.admin.putLayerData(e, a, parseInt(t));
                                if (isNaN(t) && (t = r.getLayerIndex(t)), void 0 !== t) {
                                    var i = r.getLayerData(t);
                                    i || (i = {}),
                                        i[e] = a, r.layerData["d" + t] = i
                                }
                            },

                            reloadLayer: function (e, t, n) {
                                if ("function" == typeof t && (n = t, t = void 0), isNaN(e) && (e = r.getLayerIndex(e)), void 0 !== e) {
                                    var o = a("#layui-layer" + e);
                                    void 0 === t && (t = o.data("url")),
                                    t && (o.data("url", t),
                                            r.showLoading(o),
                                            r.ajax({
                                                url: t,
                                                dataType: "html",
                                                success: function (t) {
                                                    r.removeLoading(o, !1),
                                                    "string" != typeof t && (t = JSON.stringify(t));
                                                    var l = o.data("tpl");
                                                    if (!0 === l || "true" === l) {
                                                        var s = r.getLayerData(e) || {};
                                                        s.layerIndex = e;
                                                        var c = a("<div>" + t + "</div>"),
                                                            d = {};
                                                        for (var u in c.find("script,[tpl-ignore]").each((function (e) {
                                                            var t = a(this);
                                                            d["temp_" + e] = t[0].outerHTML,
                                                                t.after("${temp_" + e + "}").remove()
                                                        })),
                                                            t = r.util.tpl(
                                                                c.html(),
                                                                s,
                                                                i.tplOpen,
                                                                i.tplClose),
                                                            d)
                                                            t = t.replace("${" + u + "}", d[u])
                                                    }
                                                    o.children(".layui-layer-content").html(t),
                                                        r.renderTpl("#layui-layer" + e + " [ew-tpl]"),
                                                    n && n(o[0], e)
                                                }
                                            })
                                    )
                                }
                            },

                            alert: function (e, a, i) {
                                return "function" == typeof a && (i = a, a = {}),
                                void 0 === a.skin && (a.skin = "layui-layer-admin"),
                                void 0 === a.shade && (a.shade = .1),
                                    t.alert(e, a, i)
                            },

                            confirm: function (e, a, i, n) {
                                return "function" == typeof a && (n = i, i = a, a = {}),
                                void 0 === a.skin && (a.skin = "layui-layer-admin"),
                                void 0 === a.shade && (a.shade = .1),
                                    t.confirm(e, a, i, n)
                            },

                            prompt: function (e, a) {
                                return "function" == typeof e && (a = e, e = {}),
                                void 0 === e.skin && (e.skin = "layui-layer-admin layui-layer-prompt"),
                                void 0 === e.shade && (e.shade = .1),
                                    t.prompt(e, a)
                            },
                            /*不敢动原代码，这是理解后的代码，不得不吐槽，写这段代码的人真的是依托答辩
                            *
                            req: function(e, t, n, o, l) {
                                // 如果 t 是函数，重新排列参数
                                if (typeof t === "function") {
                                    l = o;
                                    o = n;
                                    n = t;
                                    t = {};
                                }

                                // 如果 o 已定义且不是字符串，则将其值赋给 l
                                if (o !== undefined && typeof o !== "string") {
                                    l = o;
                                    o = undefined;
                                }

                                // 如果 o 未定义或为空，则默认为 "GET"
                                if (!o) {
                                    o = "GET";
                                }

                                // 如果 t 是字符串，确保 l 是对象，并设置 contentType
                                if (typeof t === "string") {
                                    if (!l) {
                                        l = {};
                                    }
                                    if (!l.contentType) {
                                        l.contentType = "application/json;charset=UTF-8";
                                    }
                                } else if (i.reqPutToPost) {
                                    // 根据 i.reqPutToPost 修改请求类型
                                    if (o.toLowerCase() === "put") {
                                        o = "POST";
                                        t._method = "PUT";
                                    } else if (o.toLowerCase() === "delete") {
                                        o = "GET";
                                        t._method = "DELETE";
                                    }
                                }

                                // 发送 AJAX 请求
                                return r.ajax(a.extend({
                                    url: (i.baseServer || "") + e,
                                    data: t,
                                    type: o,
                                    dataType: "json",
                                    success: n
                                }, l));
                            },
                            * */
                            req: function (e, t, n, o, l) {
                                return "function" == typeof t && (l = o, o = n, n = t, t = {}),
                                void 0 !== o && "string" != typeof o && (l = o, o = void 0),
                                o || (o = "GET"),
                                    "string" == typeof t ? (l || (l = {}),
                                    l.contentType || (l.contentType = "application/json;charset=UTF-8")) : i.reqPutToPost && ("put" === o.toLowerCase() ? (o = "POST", t._method = "PUT") : "delete" === o.toLowerCase() && (o = "GET", t._method = "DELETE")),
                                    r.ajax(a.extend({
                                        url: (i.baseServer || "") + e,
                                        data: t,
                                        type: o,
                                        dataType: "json",
                                        success: n
                                    }, l))
                            },

                            /*不敢动，垃圾代码*/
                            ajax: function (e) {
                                var t = r.util.deepClone(e);
                                e.dataType || (e.dataType = "json"),
                                e.headers || (e.headers = {});
                                var n = i.getAjaxHeaders(e.url);
                                if (n)
                                    for (var o = 0; o < n.length; o++)
                                        void 0 === e.headers[n[o].name] && (e.headers[n[o].name] = n[o].value);
                                var l = e.success;
                                return e.success = function (n, o, s) {
                                    !1 !== i.ajaxSuccessBefore(
                                        r.parseJSON(n),
                                        e.url,
                                        {
                                            param: t,
                                            reload: function (e) {
                                                r.ajax(a.extend(!0, t, e))
                                            },

                                            update: function (e) {
                                                n = e
                                            },
                                            xhr: s
                                        }) ? l && l(n, o, s) : e.cancel && e.cancel()
                                },
                                    e.error = function (a, t) {
                                        e.success({
                                                code: a.status, msg: a.statusText
                                            },
                                            t, a)
                                    },
                                !layui.cache.version
                                || i.apiNoCache && "json" === e.dataType.toLowerCase()
                                || (-1 === e.url.indexOf("?") ? e.url += "?v=" : e.url += "&v=",
                                    !0 === layui.cache.version ? e.url += (new Date).getTime() : e.url += layui.cache.version),
                                    a.ajax(e)
                            },

                            parseJSON: function (e) {
                                if ("string" == typeof e)
                                    try {
                                        return JSON.parse(e)
                                    } catch (e) {

                                    }
                                return e
                            },

                            showLoading: function (e, t, n, o) {
                                void 0 === e
                                || "string" == typeof e
                                || e instanceof a
                                || (t = e.type, n = e.opacity, o = e.size, e = e.elem),
                                void 0 === t && (t = i.defaultLoading || 1),
                                void 0 === o && (o = "sm"),
                                void 0 === e && (e = "body");
                                var l = [
                                    '<div class="ball-loader ' + o + '"><span></span><span></span><span></span><span></span></div>',
                                    '<div class="rubik-loader ' + o + '"></div>',
                                    '<div class="signal-loader ' + o + '"><span></span><span></span><span></span><span></span></div>',
                                    '<div class="layui-loader ' + o + '"><i class="layui-icon layui-icon-loading layui-anim layui-anim-rotate layui-anim-loop"></i></div>'];
                                a(e).addClass("page-no-scroll"),
                                    a(e).scrollTop(0);
                                var s = a(e).children(".page-loading");
                                s.length <= 0 && (a(e).append('<div class="page-loading">' + l[t - 1] + "</div>"),
                                    s = a(e).children(".page-loading")), void 0 !== n && s.css("background-color", "rgba(255,255,255," + n + ")"),
                                    s.show()
                            },

                            removeLoading: function (e, t, i) {
                                void 0 === e && (e = "body"),
                                void 0 === t && (t = !0);
                                var n = a(e).children(".page-loading");
                                i ? n.remove() : t ? n.fadeOut("fast") : n.hide(),
                                    a(e).removeClass("page-no-scroll")
                            },


                            putTempData: function (e, a, t) {
                                var n = t ? i.tableName : i.tableName + "_tempData";
                                /*第一次看到这么写的垃圾*/
                                null == a
                                    ? t
                                        ? layui.data(n, {key: e, remove: !0})
                                        : layui.sessionData(n, {key: e, remove: !0})
                                    : t
                                        ? layui.data(n, {key: e, value: a})
                                        : layui.sessionData(n, {key: e, value: a})
                            },


                            getTempData: function (e, a) {
                                "boolean" == typeof e && (a = e, e = void 0);
                                var t = a ? i.tableName : i.tableName + "_tempData",
                                    n = a ? layui.data(t) : layui.sessionData(t);
                                return e ? n ? n[e] : void 0 : n
                            },

                            rollPage: function (e) {
                                if (window !== top && !r.isTop() && top.layui && top.layui.admin)
                                    return top.layui.admin.rollPage(e);
                                var t = a(o + ">.layui-tab-title"),
                                    i = t.scrollLeft();
                                if ("left" === e)
                                    t.animate({scrollLeft: i - 120}, 100);
                                else if ("auto" === e) {
                                    var n = 0;
                                    t.children("li").each((function () {
                                        if (a(this).hasClass("layui-this"))
                                            return !1;
                                        n += a(this).outerWidth()
                                    })),
                                        t.animate({scrollLeft: n - 120}, 100)
                                } else
                                    t.animate({scrollLeft: i + 120}, 100)
                            },

                            refresh: function (e, t) {
                                if (window !== top && !r.isTop() && top.layui && top.layui.admin)
                                    return top.layui.admin.refresh(e);
                                var i;
                                if (e
                                    ? (!(i = a(o + '>.layui-tab-content>.layui-tab-item>.admin-iframe[lay-id="' + e + '"]')) || i.length <= 0) && (i = a(n + ">.admin-iframe"))
                                    : (!(i = a(o + ">.layui-tab-content>.layui-tab-item.layui-show>.admin-iframe")) || i.length <= 0) && (i = a(n + ">div>.admin-iframe")),
                                !i || !i[0])
                                    return console.warn(e + " is not found");
                                try {
                                    t
                                    && i[0].contentWindow.refreshTab
                                        ? i[0].contentWindow.refreshTab()
                                        : (r.showLoading({
                                            elem: i.parent(), size: ""
                                        }),
                                            i[0].contentWindow.location.reload())
                                } catch (e) {
                                    console.warn(e),
                                        i.attr("src", i.attr("src"))
                                }
                            },


                            closeThisTabs: function (e) {
                                if (window !== top && !r.isTop() && top.layui && top.layui.admin)
                                    return top.layui.admin.closeThisTabs(e);
                                r.closeTabOperNav();
                                var i = a(o + ">.layui-tab-title");
                                if (e) {
                                    if (e === i.find("li").first().attr("lay-id"))
                                        return t.msg("主页不能关闭", {icon: 2});
                                    i.find('li[lay-id="' + e + '"]').find(".layui-tab-close").trigger("click")
                                } else {
                                    if (i.find("li").first().hasClass("layui-this"))
                                        return t.msg("主页不能关闭", {icon: 2});
                                    i.find("li.layui-this").find(".layui-tab-close").trigger("click")
                                }
                            },

                            closeOtherTabs: function (e) {
                                if (window !== top && !r.isTop() && top.layui && top.layui.admin)
                                    return top.layui.admin.closeOtherTabs(e);
                                e ? a(o + ">.layui-tab-title li:gt(0)").each((
                                        function () {
                                            e !== a(this).attr("lay-id")
                                            && a(this).find(".layui-tab-close").trigger("click")
                                        }
                                    ))
                                    : a(o + ">.layui-tab-title li:gt(0):not(.layui-this)").find(".layui-tab-close").trigger("click"),
                                    r.closeTabOperNav()
                            },

                            closeAllTabs: function () {
                                if (window !== top && !r.isTop() && top.layui && top.layui.admin)
                                    return top.layui.admin.closeAllTabs();
                                a(o + ">.layui-tab-title li:gt(0)").find(".layui-tab-close").trigger("click"),
                                    a(o + ">.layui-tab-title li:eq(0)").trigger("click"),
                                    r.closeTabOperNav()
                            },

                            closeTabOperNav: function () {
                                if (window !== top && !r.isTop() && top.layui && top.layui.admin)
                                    return top.layui.admin.closeTabOperNav();
                                a(".layui-icon-down .layui-nav .layui-nav-child").removeClass("layui-show")
                            },

                            changeTheme: function (e, a, t, i) {
                                if (t || r.putSetting("defaultTheme", e), a || (a = top), r.removeTheme(a), e)
                                    try {
                                        var n = a.layui.jquery("body");
                                        n.addClass(e), n.data("theme", e)
                                    } catch (e) {
                                    }
                                if (!i)
                                    for (var o = a.frames, l = 0; l < o.length; l++)
                                        r.changeTheme(e, o[l], !0, !1)
                            },

                            removeTheme: function (e) {
                                e || (e = window);
                                try {
                                    var a = e.layui.jquery("body"),
                                        t = a.data("theme");
                                    t && a.removeClass(t),
                                        a.removeData("theme")
                                } catch (e) {
                                }
                            },

                            closeThisDialog: function () {
                                return r.closeDialog()
                            },

                            closeDialog: function (e) {
                                e ? t.close(r.getLayerIndex(e))
                                    : parent.layer.close(parent.layer.getFrameIndex(window.name))
                            },

                            getLayerIndex: function (e) {
                                if (!e)
                                    return parent.layer.getFrameIndex(window.name);
                                var t = a(e).parents(".layui-layer").first().attr("id");
                                return t && t.length >= 11 ? t.substring(11) : void 0
                            },

                            iframeAuto: function () {
                                return parent.layer.iframeAuto(parent.layer.getFrameIndex(window.name))
                            },

                            getPageHeight: function () {
                                return document.documentElement.clientHeight || document.body.clientHeight
                            },

                            getPageWidth: function () {
                                return document.documentElement.clientWidth || document.body.clientWidth
                            },

                            modelForm: function (e, t, i) {
                                var n = a(e);
                                n.addClass("layui-form"),
                                i && n.attr("lay-filter", i);
                                var o = n.find(".layui-layer-btn .layui-layer-btn0");
                                o.attr("lay-submit", ""),
                                    o.attr("lay-filter", t)
                            },

                            btnLoading: function (e, t, i) {
                                void 0 !== t
                                && "boolean" == typeof t
                                && (i = t, t = void 0),
                                void 0 === t && (t = "&nbsp;加载中"),
                                void 0 === i && (i = !0);
                                var n = a(e);
                                i ? (n.addClass("ew-btn-loading"),
                                        n.prepend('<span class="ew-btn-loading-text">' +
                                            '<i class="layui-icon layui-icon-loading layui-anim layui-anim-rotate layui-anim-loop">' +
                                            '</i>' + t + "</span>"),
                                        n.attr("disabled", "disabled").prop("disabled", !0))
                                    : (n.removeClass("ew-btn-loading"),
                                        n.children(".ew-btn-loading-text").remove(),
                                        n.removeProp("disabled").removeAttr("disabled"));

                            },

                            openSideAutoExpand: function () {
                                var e = a(".layui-layout-admin>.layui-side");
                                e.off("mouseenter.openSideAutoExpand").on(
                                    "mouseenter.openSideAutoExpand", (
                                        function () {
                                            a(this).parent().hasClass("admin-nav-mini") && (r.flexible(!0),
                                                a(this).addClass("side-mini-hover"))
                                        })
                                ),
                                    e.off("mouseleave.openSideAutoExpand").on
                                    ("mouseleave.openSideAutoExpand",
                                        (
                                            function () {
                                                a(this).hasClass("side-mini-hover")
                                                && (r.flexible(!1),
                                                    a(this).removeClass("side-mini-hover"))
                                            }
                                        )
                                    )
                            },

                            openCellAutoExpand: function () {
                                var e = a("body");
                                e.off("mouseenter.openCellAutoExpand").on(
                                    "mouseenter.openCellAutoExpand",
                                    ".layui-table-view td",
                                    (
                                        function () {
                                            a(this).find(".layui-table-grid-down").trigger("click")
                                        }
                                    )),
                                    e.off("mouseleave.openCellAutoExpand").on(
                                        "mouseleave.openCellAutoExpand",
                                        ".layui-table-tips>.layui-layer-content",
                                        (
                                            function () {
                                                a(".layui-table-tips-c").trigger("click")
                                            })
                                    )
                            },

                            parseLayerOption: function (e) {
                                for (var t in e)
                                    e.hasOwnProperty(t)
                                    && e[t]
                                    && -1 !== e[t].toString().indexOf(",")
                                    && (e[t] = e[t].toString().split(","));
                                var i = {
                                    success: "layero,index",
                                    cancel: "index,layero",
                                    end: "",
                                    full: "",
                                    min: "",
                                    restore: ""
                                };

                                for (var n in i)
                                    if (i.hasOwnProperty(n) && e[n])
                                        try {
                                            /^[a-zA-Z_]+[a-zA-Z0-9_]+$/.test(e[n]) && (e[n] += "()"),
                                                e[n] = new Function(i[n], e[n])
                                        } catch (a) {
                                            e[n] = void 0
                                        }
                                return e.content
                                && "string" == typeof e.content
                                && 0 === e.content.indexOf("#")
                                && (
                                    a(e.content).is("script")
                                        ? e.content = a(e.content).html()
                                        : e.content = a(e.content)
                                ),

                                void 0 === e.type
                                && void 0 === e.url
                                && (e.type = 2), e
                            },


                            strToWin: function (e) {
                                var a = window;
                                if (!e)
                                    return a;
                                for (var t = e.split("."), i = 0; i < t.length; i++)
                                    a = a[t[i]];
                                return a
                            },

                            hideTableScrollBar: function (e) {
                                if (!(r.getPageWidth() <= 768)) {
                                    if (!e) {
                                        var t = a(o + ">.layui-tab-content>.layui-tab-item.layui-show>.admin-iframe");
                                        t.length <= 0 && (t = a(n + ">div>.admin-iframe")),
                                        t.length > 0 && (e = t[0].contentWindow)
                                    }
                                    try {
                                        window.hsbTimer && clearTimeout(window.hsbTimer),
                                            e.layui.jquery(".layui-table-body.layui-table-main").addClass("no-scrollbar"),
                                            window.hsbTimer = setTimeout((
                                                    function () {
                                                        e.layui.jquery(".layui-table-body.layui-table-main").removeClass("no-scrollbar")
                                                    }),
                                                800
                                            )
                                    } catch (e) {
                                    }
                                }
                            },
                            isTop: function () {
                                return a(n).length > 0
                            }
                        };
                    r.events = {
                        flexible: function () {
                            r.strToWin(a(this).data("window")).layui.admin.flexible()
                        }, refresh: function () {
                            r.strToWin(a(this).data("window")).layui.admin.refresh()
                        }, back: function () {
                            r.strToWin(a(this).data("window")).history.back()
                        }, theme: function () {
                            var e = r.util.deepClone(a(this).data());
                            r.strToWin(e.window).layui.admin.popupRight(a.extend({
                                id: "layer-theme",
                                url: e.url || "/static/assets/libs/templets/tpl-theme.html"
                            }, r.parseLayerOption(e)))
                        }, note: function () {
                            var e = r.util.deepClone(a(this).data());
                            r.strToWin(e.window).layui.admin.popupRight(a.extend({
                                id: "layer-note",
                                url: e.url || "/static/assets/libs/templets/tpl-note.html"
                            }, r.parseLayerOption(e)))
                        }, message: function () {
                            var e = r.util.deepClone(a(this).data());
                            r.strToWin(e.window).layui.admin.popupRight(a.extend({
                                id: "layer-notice",
                                url: e.url || "/static/assets/libs/templets/tpl-message.html"
                            }, r.parseLayerOption(e)))
                        }, psw: function () {
                            var e = r.util.deepClone(a(this).data());
                            r.strToWin(e.window).layui.admin.open(a.extend({
                                id: "layer-psw",
                                title: "修改密码",
                                shade: 0,
                                url: e.url || "/static/assets/libs/templets/tpl-password.html"
                            }, r.parseLayerOption(e)))
                        }, logout: function () {
                            var e = r.util.deepClone(a(this).data());

                            function n() {
                                if (e.ajax) {
                                    var a = t.load(2);
                                    r.req(e.ajax, (function (n) {
                                        if (t.close(a), e.parseData) try {
                                            n = new Function("res", e.parseData)(n)
                                        } catch (e) {
                                            console.error(e)
                                        }
                                        n.code == (e.code || 0) ? (i.removeToken && i.removeToken(), location.replace(e.url || "/")) : t.msg(n.msg, {icon: 2})
                                    }), e.method || "delete")
                                } else i.removeToken && i.removeToken(), location.replace(e.url || "/")
                            }

                            if (r.unlockScreen(), !1 === e.confirm || "false" === e.confirm) return n();
                            r.strToWin(e.window).layui.layer.confirm(e.content || "确定要退出登录吗？", a.extend({
                                title: "温馨提示",
                                skin: "layui-layer-admin",
                                shade: .1
                            }, r.parseLayerOption(e)), (function () {
                                n()
                            }))
                        }, open: function () {
                            var e = r.util.deepClone(a(this).data());
                            r.strToWin(e.window).layui.admin.open(r.parseLayerOption(e))
                        }, popupRight: function () {
                            var e = r.util.deepClone(a(this).data());
                            r.strToWin(e.window).layui.admin.popupRight(r.parseLayerOption(e))
                        }, fullScreen: function () {
                            var e = "layui-icon-screen-full", t = "layui-icon-screen-restore", i = a(this).find("i");
                            if (document.fullscreenElement || document.msFullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement) {
                                var n = document.exitFullscreen || document.webkitExitFullscreen || document.mozCancelFullScreen || document.msExitFullscreen;
                                if (n) n.call(document); else if (window.ActiveXObject) {
                                    var o = new ActiveXObject("WScript.Shell");
                                    o && o.SendKeys("{F11}")
                                }
                                i.addClass(e).removeClass(t)
                            } else {
                                var l = document.documentElement,
                                    s = l.requestFullscreen || l.webkitRequestFullscreen || l.mozRequestFullScreen || l.msRequestFullscreen;
                                if (s) s.call(l); else if (window.ActiveXObject) {
                                    var r = new ActiveXObject("WScript.Shell");
                                    r && r.SendKeys("{F11}")
                                }
                                i.addClass(t).removeClass(e)
                            }
                        }, leftPage: function () {
                            r.strToWin(a(this).data("window")).layui.admin.rollPage("left")
                        }, rightPage: function () {
                            r.strToWin(a(this).data("window")).layui.admin.rollPage()
                        }, closeThisTabs: function () {
                            var e = a(this).data("url");
                            r.strToWin(a(this).data("window")).layui.admin.closeThisTabs(e)
                        }, closeOtherTabs: function () {
                            r.strToWin(a(this).data("window")).layui.admin.closeOtherTabs()
                        }, closeAllTabs: function () {
                            r.strToWin(a(this).data("window")).layui.admin.closeAllTabs()
                        }, closeDialog: function () {
                            a(this).parents(".layui-layer").length > 0 ? r.closeDialog(this) : r.closeDialog()
                        }, closeIframeDialog: function () {
                            r.closeDialog()
                        }, closePageDialog: function () {
                            r.closeDialog(this)
                        }, lockScreen: function () {
                            r.strToWin(a(this).data("window")).layui.admin.lockScreen(a(this).data("url"))
                        }
                    }, r.chooseLocation = function (e) {
                        var i = e.title, n = e.onSelect, o = e.needCity, l = e.center, s = e.defaultZoom,
                            c = e.pointZoom, d = e.keywords, u = e.pageSize, p = e.mapJsUrl;
                        void 0 === i && (i = "选择位置"), void 0 === s && (s = 11), void 0 === c && (c = 17), void 0 === d && (d = ""), void 0 === u && (u = 30), void 0 === p && (p = "https://webapi.amap.com/maps?v=1.4.14&key=006d995d433058322319fa797f2876f5");
                        var y, m = !1, f = function (e, t) {
                                AMap.service(["AMap.PlaceSearch"], (function () {
                                    var i = new AMap.PlaceSearch({type: "", pageSize: u, pageIndex: 1}), n = [t, e];
                                    i.searchNearBy(d, n, 1e3, (function (e, t) {
                                        if ("complete" === e) {
                                            for (var i = t.poiList.pois, n = "", o = 0; o < i.length; o++) {
                                                var l = i[o];
                                                void 0 !== l.location && (n += '<div data-lng="' + l.location.lng + '" data-lat="' + l.location.lat + '" class="ew-map-select-search-list-item">', n += '     <div class="ew-map-select-search-list-item-title">' + l.name + "</div>", n += '     <div class="ew-map-select-search-list-item-address">' + l.address + "</div>", n += '     <div class="ew-map-select-search-list-item-icon-ok layui-hide"><i class="layui-icon layui-icon-ok-circle"></i></div>', n += "</div>")
                                            }
                                            a("#ew-map-select-pois").html(n)
                                        }
                                    }))
                                }))
                            }, v = function () {
                                var e = {resizeEnable: !0, zoom: s};
                                l && (e.center = l);
                                var i = new AMap.Map("ew-map-select-map", e);
                                i.on("complete", (function () {
                                    var e = i.getCenter();
                                    f(e.lat, e.lng)
                                })), i.on("moveend", (function () {
                                    if (m) m = !1; else {
                                        a("#ew-map-select-tips").addClass("layui-hide"), a("#ew-map-select-center-img").removeClass("bounceInDown"), setTimeout((function () {
                                            a("#ew-map-select-center-img").addClass("bounceInDown")
                                        }));
                                        var e = i.getCenter();
                                        f(e.lat, e.lng)
                                    }
                                })), a("#ew-map-select-pois").off("click").on("click", ".ew-map-select-search-list-item", (function () {
                                    a("#ew-map-select-tips").addClass("layui-hide"), a("#ew-map-select-pois .ew-map-select-search-list-item-icon-ok").addClass("layui-hide"), a(this).find(".ew-map-select-search-list-item-icon-ok").removeClass("layui-hide"), a("#ew-map-select-center-img").removeClass("bounceInDown"), setTimeout((function () {
                                        a("#ew-map-select-center-img").addClass("bounceInDown")
                                    }));
                                    var e = a(this).data("lng"), t = a(this).data("lat"),
                                        n = a(this).find(".ew-map-select-search-list-item-title").text(),
                                        o = a(this).find(".ew-map-select-search-list-item-address").text();
                                    y = {name: n, address: o, lat: t, lng: e}, m = !0, i.setZoomAndCenter(c, [e, t])
                                })), a("#ew-map-select-btn-ok").click((function () {
                                    if (void 0 === y) t.msg("请点击位置列表选择", {icon: 2, anim: 6}); else if (n) if (o) {
                                        var e = t.load(2);
                                        i.setCenter([y.lng, y.lat]), i.getCity((function (a) {
                                            t.close(e), y.city = a, r.closeDialog("#ew-map-select-btn-ok"), n(y)
                                        }))
                                    } else r.closeDialog("#ew-map-select-btn-ok"), n(y); else r.closeDialog("#ew-map-select-btn-ok")
                                }));
                                var d = a("#ew-map-select-input-search");
                                d.off("input").on("input", (function () {
                                    var e = a(this).val(), t = a("#ew-map-select-tips");
                                    e || (t.html(""), t.addClass("layui-hide")), AMap.plugin("AMap.Autocomplete", (function () {
                                        new AMap.Autocomplete({city: "全国"}).search(e, (function (e, i) {
                                            if (i.tips) {
                                                for (var n = i.tips, o = "", l = 0; l < n.length; l++) {
                                                    var s = n[l];
                                                    void 0 !== s.location && (o += '<div data-lng="' + s.location.lng + '" data-lat="' + s.location.lat + '" class="ew-map-select-search-list-item">', o += '     <div class="ew-map-select-search-list-item-icon-search"><i class="layui-icon layui-icon-search"></i></div>', o += '     <div class="ew-map-select-search-list-item-title">' + s.name + "</div>", o += '     <div class="ew-map-select-search-list-item-address">' + s.address + "</div>", o += "</div>")
                                                }
                                                t.html(o), 0 === n.length ? a("#ew-map-select-tips").addClass("layui-hide") : a("#ew-map-select-tips").removeClass("layui-hide")
                                            } else t.html(""), t.addClass("layui-hide")
                                        }))
                                    }))
                                })), d.off("blur").on("blur", (function () {
                                    var e = a(this).val(), t = a("#ew-map-select-tips");
                                    e || (t.html(""), t.addClass("layui-hide"))
                                })), d.off("focus").on("focus", (function () {
                                    a(this).val() && a("#ew-map-select-tips").removeClass("layui-hide")
                                })), a("#ew-map-select-tips").off("click").on("click", ".ew-map-select-search-list-item", (function () {
                                    a("#ew-map-select-tips").addClass("layui-hide");
                                    var e = a(this).data("lng"), t = a(this).data("lat");
                                    y = void 0, i.setZoomAndCenter(c, [e, t])
                                }))
                            },
                            h = ['<div class="ew-map-select-tool" style="position: relative;">', '     搜索：<input id="ew-map-select-input-search" class="layui-input icon-search inline-block" style="width: 190px;" placeholder="输入关键字搜索" autocomplete="off" />', '     <button id="ew-map-select-btn-ok" class="layui-btn icon-btn pull-right" type="button"><i class="layui-icon">&#xe605;</i>确定</button>', '     <div id="ew-map-select-tips" class="ew-map-select-search-list layui-hide">', "     </div>", "</div>", '<div class="layui-row ew-map-select">', '     <div class="layui-col-sm7 ew-map-select-map-group" style="position: relative;">', '          <div id="ew-map-select-map"></div>', '          <i id="ew-map-select-center-img2" class="layui-icon layui-icon-add-1"></i>', '          <img id="ew-map-select-center-img" src="https://3gimg.qq.com/lightmap/components/locationPicker2/image/marker.png" alt=""/>', "     </div>", '     <div id="ew-map-select-pois" class="layui-col-sm5 ew-map-select-search-list">', "     </div>", "</div>"].join("");
                        r.open({
                            id: "ew-map-select",
                            type: 1,
                            title: i,
                            area: "750px",
                            content: h,
                            success: function (e, t) {
                                var i = a(e).children(".layui-layer-content");
                                i.css("overflow", "visible"), r.showLoading(i), void 0 === window.AMap ? a.getScript(p, (function () {
                                    v(), r.removeLoading(i)
                                })) : (v(), r.removeLoading(i))
                            }
                        })
                    }, r.cropImg = function (e) {
                        var i = "image/jpeg", n = e.aspectRatio, o = e.imgSrc, l = e.imgType, s = e.onCrop,
                            c = e.limitSize, d = e.acceptMime, u = e.exts, p = e.title;
                        void 0 === n && (n = 1), void 0 === p && (p = "裁剪图片"), l && (i = l), layui.use(["Cropper", "upload"], (function () {
                            var e = layui.Cropper, l = layui.upload;

                            function y() {
                                var p, m = a("#ew-crop-img"), f = {
                                    elem: "#ew-crop-img-upload", auto: !1, drag: !1, choose: function (a) {
                                        a.preview((function (a, t, n) {
                                            i = t.type, m.attr("src", n), o && p ? (p.destroy(), p = new e(m[0], v)) : (o = n, y())
                                        }))
                                    }
                                };
                                if (void 0 !== c && (f.size = c), void 0 !== d && (f.acceptMime = d), void 0 !== u && (f.exts = u), l.render(f), !o) return a("#ew-crop-img-upload").trigger("click");
                                var v = {aspectRatio: n, preview: "#ew-crop-img-preview"};
                                p = new e(m[0], v), a(".ew-crop-tool").on("click", "[data-method]", (function () {
                                    var e, n, o = a(this).data();
                                    if (p && o.method) {
                                        switch (o = a.extend({}, o), e = p.cropped, o.method) {
                                            case"rotate":
                                                e && v.viewMode > 0 && p.clear();
                                                break;
                                            case"getCroppedCanvas":
                                                "image/jpeg" === i && (o.option || (o.option = {}), o.option.fillColor = "#fff")
                                        }
                                        switch (n = p[o.method](o.option, o.secondOption), o.method) {
                                            case"rotate":
                                                e && v.viewMode > 0 && p.crop();
                                                break;
                                            case"scaleX":
                                            case"scaleY":
                                                a(this).data("option", -o.option);
                                                break;
                                            case"getCroppedCanvas":
                                                n ? (s && s(n.toDataURL(i)), r.closeDialog("#ew-crop-img")) : t.msg("裁剪失败", {
                                                    icon: 2,
                                                    anim: 6
                                                })
                                        }
                                    }
                                }))
                            }

                            var m = ['<div class="layui-row">', '     <div class="layui-col-sm8" style="min-height: 9rem;">', '          <img id="ew-crop-img" src="', o || "", '" style="max-width:100%;" alt=""/>', "     </div>", '     <div class="layui-col-sm4 layui-hide-xs" style="padding: 15px;text-align: center;">', '          <div id="ew-crop-img-preview" style="width: 100%;height: 9rem;overflow: hidden;display: inline-block;border: 1px solid #dddddd;"></div>', "     </div>", "</div>", '<div class="text-center ew-crop-tool" style="padding: 15px 10px 5px 0;">', '     <div class="layui-btn-group" style="margin-bottom: 10px;margin-left: 10px;">', '          <button title="放大" data-method="zoom" data-option="0.1" class="layui-btn icon-btn" type="button"><i class="layui-icon layui-icon-add-1"></i></button>', '          <button title="缩小" data-method="zoom" data-option="-0.1" class="layui-btn icon-btn" type="button"><span style="display: inline-block;width: 12px;height: 2.5px;background: rgba(255, 255, 255, 0.9);vertical-align: middle;margin: 0 4px;"></span></button>', "     </div>", '     <div class="layui-btn-group layui-hide-xs" style="margin-bottom: 10px;">', '          <button title="向左旋转" data-method="rotate" data-option="-45" class="layui-btn icon-btn" type="button"><i class="layui-icon layui-icon-refresh-1" style="transform: rotateY(180deg) rotate(40deg);display: inline-block;"></i></button>', '          <button title="向右旋转" data-method="rotate" data-option="45" class="layui-btn icon-btn" type="button"><i class="layui-icon layui-icon-refresh-1" style="transform: rotate(30deg);display: inline-block;"></i></button>', "     </div>", '     <div class="layui-btn-group" style="margin-bottom: 10px;">', '          <button title="左移" data-method="move" data-option="-10" data-second-option="0" class="layui-btn icon-btn" type="button"><i class="layui-icon layui-icon-left"></i></button>', '          <button title="右移" data-method="move" data-option="10" data-second-option="0" class="layui-btn icon-btn" type="button"><i class="layui-icon layui-icon-right"></i></button>', '          <button title="上移" data-method="move" data-option="0" data-second-option="-10" class="layui-btn icon-btn" type="button"><i class="layui-icon layui-icon-up"></i></button>', '          <button title="下移" data-method="move" data-option="0" data-second-option="10" class="layui-btn icon-btn" type="button"><i class="layui-icon layui-icon-down"></i></button>', "     </div>", '     <div class="layui-btn-group" style="margin-bottom: 10px;">', '          <button title="左右翻转" data-method="scaleX" data-option="-1" class="layui-btn icon-btn" type="button" style="position: relative;width: 41px;"><i class="layui-icon layui-icon-triangle-r" style="position: absolute;left: 9px;top: 0;transform: rotateY(180deg);font-size: 16px;"></i><i class="layui-icon layui-icon-triangle-r" style="position: absolute; right: 3px; top: 0;font-size: 16px;"></i></button>', '          <button title="上下翻转" data-method="scaleY" data-option="-1" class="layui-btn icon-btn" type="button" style="position: relative;width: 41px;"><i class="layui-icon layui-icon-triangle-d" style="position: absolute;left: 11px;top: 6px;transform: rotateX(180deg);line-height: normal;font-size: 16px;"></i><i class="layui-icon layui-icon-triangle-d" style="position: absolute; left: 11px; top: 14px;line-height: normal;font-size: 16px;"></i></button>', "     </div>", '     <div class="layui-btn-group" style="margin-bottom: 10px;">', '          <button title="重新开始" data-method="reset" class="layui-btn icon-btn" type="button"><i class="layui-icon layui-icon-refresh"></i></button>', '          <button title="选择图片" id="ew-crop-img-upload" class="layui-btn icon-btn" type="button" style="border-radius: 0 2px 2px 0;"><i class="layui-icon layui-icon-upload-drag"></i></button>', "     </div>", '     <button data-method="getCroppedCanvas" data-option="{ &quot;maxWidth&quot;: 4096, &quot;maxHeight&quot;: 4096 }" class="layui-btn icon-btn" type="button" style="margin-left: 10px;margin-bottom: 10px;"><i class="layui-icon">&#xe605;</i>完成</button>', "</div>"].join("");
                            r.open({
                                title: p, area: "665px", type: 1, content: m, success: function (e, t) {
                                    a(e).children(".layui-layer-content").css("overflow", "visible"), y()
                                }
                            })
                        }))
                    }, r.util = {
                        Convert_BD09_To_GCJ02: function (e) {
                            var a = 52.35987755982988, t = e.lng - .0065, i = e.lat - .006,
                                n = Math.sqrt(t * t + i * i) - 2e-5 * Math.sin(i * a),
                                o = Math.atan2(i, t) - 3e-6 * Math.cos(t * a);
                            return {lng: n * Math.cos(o), lat: n * Math.sin(o)}
                        }, Convert_GCJ02_To_BD09: function (e) {
                            var a = 52.35987755982988, t = e.lng, i = e.lat,
                                n = Math.sqrt(t * t + i * i) + 2e-5 * Math.sin(i * a),
                                o = Math.atan2(i, t) + 3e-6 * Math.cos(t * a);
                            return {lng: n * Math.cos(o) + .0065, lat: n * Math.sin(o) + .006}
                        }, animateNum: function (e, t, i, n) {
                            t = null == t || !0 === t || "true" === t, i = isNaN(i) ? 500 : i, n = isNaN(n) ? 100 : n;
                            var o = function (e, a) {
                                return a && /^[0-9]+.?[0-9]*$/.test(e) ? (e = e.toString()).replace(e.indexOf(".") > 0 ? /(\d)(?=(\d{3})+(?:\.))/g : /(\d)(?=(\d{3})+(?:$))/g, "$1,") : e
                            };
                            a(e).each((function () {
                                var e = a(this), l = e.data("num");
                                l || (l = e.text().replace(/,/g, ""), e.data("num", l));
                                var s = "INPUT,TEXTAREA".indexOf(e.get(0).tagName) >= 0, r = function (e) {
                                    for (var a = "", t = 0; t < e.length; t++) {
                                        if (!isNaN(e.charAt(t))) return a;
                                        a += e.charAt(t)
                                    }
                                }(l.toString()), c = function (e) {
                                    for (var a = "", t = e.length - 1; t >= 0; t--) {
                                        if (!isNaN(e.charAt(t))) return a;
                                        a = e.charAt(t) + a
                                    }
                                }(l.toString()), d = l.toString().replace(r, "").replace(c, "");
                                if (isNaN(1 * d) || "0" === d) return s ? e.val(l) : e.html(l), console.error("not a number");
                                var u = d.split("."), p = u[1] ? u[1].length : 0, y = 0, m = d;
                                Math.abs(1 * m) > 10 && (y = parseFloat(u[0].substring(0, u[0].length - 1) + (u[1] ? ".0" + u[1] : "")));
                                var f = (m - y) / n, v = 0, h = setInterval((function () {
                                    var a = r + o(y.toFixed(p), t) + c;
                                    s ? e.val(a) : e.html(a), y += f, v++, (Math.abs(y) >= Math.abs(1 * m) || v > 5e3) && (a = r + o(m, t) + c, s ? e.val(a) : e.html(a), clearInterval(h))
                                }), i / n)
                            }))
                        }, deepClone: function (e) {
                            var a, t = r.util.isClass(e);
                            if ("Object" === t) a = {}; else {
                                if ("Array" !== t) return e;
                                a = []
                            }
                            for (var i in e) if (e.hasOwnProperty(i)) {
                                var n = e[i], o = r.util.isClass(n);
                                a[i] = "Object" === o || "Array" === o ? arguments.callee(n) : e[i]
                            }
                            return a
                        }, isClass: function (e) {
                            return null === e ? "Null" : void 0 === e ? "Undefined" : Object.prototype.toString.call(e).slice(8, -1)
                        }, fullTextIsEmpty: function (e) {
                            if (!e) return !0;
                            for (var a = ["img", "audio", "video", "iframe", "object"], t = 0; t < a.length; t++) if (e.indexOf("<" + a[t]) > -1) return !1;
                            var i = e.replace(/\s*/g, "");
                            return !i || !(i = i.replace(/&nbsp;/gi, "")) || !(i = i.replace(/<[^>]+>/g, ""))
                        }, removeStyle: function (e, t) {
                            "string" == typeof t && (t = [t]);
                            for (var i = 0; i < t.length; i++) a(e).css(t[i], "")
                        }, scrollTop: function (e) {
                            a(e || "html,body").animate({scrollTop: 0}, 300)
                        }, tpl: function (e, a, t, i) {
                            if (null == e || "string" != typeof e) return e;
                            a || (a = {}), t || (t = "{{"), i || (i = "}}");
                            var n = {
                                exp: function (e) {
                                    return new RegExp(e, "g")
                                }, query: function (e, a, o) {
                                    var l = ["#([\\s\\S])+?", "([^{#}])*?"][e || 0];
                                    return n.exp((a || "") + t + l + i + (o || ""))
                                }, escape: function (e) {
                                    return String(e || "").replace(/&(?!#?[a-zA-Z0-9]+;)/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/'/g, "&#39;").replace(/"/g, "&quot;")
                                }, error: function (e, a) {
                                    console.error("Laytpl Error：" + e + "\n" + (a || ""))
                                }, parse: function (e, a) {
                                    var o = e;
                                    try {
                                        var l = n.exp("^" + t + "#"), s = n.exp(i + "$");
                                        return e = '"use strict";var view = "' + (e = e.replace(n.exp(t + "#"), t + "# ").replace(n.exp(i + "}"), "} " + i).replace(/\\/g, "\\\\").replace(n.exp(t + "!(.+?)!" + i), (function (e) {
                                            return e.replace(n.exp("^" + t + "!"), "").replace(n.exp("!" + i), "").replace(n.exp(t + "|" + i), (function (e) {
                                                return e.replace(/(.)/g, "\\$1")
                                            }))
                                        })).replace(/(?="|')/g, "\\").replace(n.query(), (function (e) {
                                            return '";' + (e = e.replace(l, "").replace(s, "")).replace(/\\/g, "") + ';view+="'
                                        })).replace(n.query(1), (function (e) {
                                            var a = '"+(';
                                            return e.replace(/\s/g, "") === t + i ? "" : (e = e.replace(n.exp(t + "|" + i), ""), /^=/.test(e) && (e = e.replace(/^=/, ""), a = '"+_escape_('), a + e.replace(/\\/g, "") + ')+"')
                                        })).replace(/\r\n/g, '\\r\\n" + "').replace(/\n/g, '\\n" + "').replace(/\r/g, '\\r" + "')) + '";return view;', (e = new Function("d, _escape_", e))(a, n.escape)
                                    } catch (e) {
                                        return n.error(e, o), o
                                    }
                                }
                            };
                            return n.parse(e, a)
                        }, render: function (e) {
                            if ("string" == typeof e.url) return e.success = function (t) {
                                r.util.render(a.extend({}, e, {url: t}))
                            }, void ("ajax" === e.ajax ? r.ajax(e) : r.req(e.url, e.where, e.success, e.method, e));
                            var t = r.util.tpl(e.tpl, e.url, e.open || i.tplOpen, e.close || i.tplClose);
                            a(e.elem).next("[ew-tpl-rs]").remove(), a(e.elem).after(t), a(e.elem).next().attr("ew-tpl-rs", ""), e.done && e.done(e.url)
                        }
                    }, r.lockScreen = function (e) {
                        if (window !== top && !r.isTop() && top.layui && top.layui.admin) return top.layui.admin.lockScreen(e);
                        console.log(e), e || (e = "/static/assets/libs/templets/tpl-lock-screen.html");
                        var i = a("#ew-lock-screen-group");
                        if (i.length > 0) i.fadeIn("fast"), r.isLockScreen = !0, r.putTempData("isLockScreen", r.isLockScreen, !0); else {
                            var n = t.load(2);
                            r.ajax({
                                url: e, dataType: "html", success: function (i) {
                                    t.close(n), "string" == typeof i ? (a("body").append('<div id="ew-lock-screen-group">' + i + "</div>"), r.isLockScreen = !0, r.putTempData("isLockScreen", r.isLockScreen, !0), r.putTempData("lockScreenUrl", e, !0)) : (console.error(i), t.msg(JSON.stringify(i), {
                                        icon: 2,
                                        anim: 6
                                    }))
                                }
                            })
                        }
                    }, r.unlockScreen = function (e) {
                        if (window !== top && !r.isTop() && top.layui && top.layui.admin) return top.layui.admin.unlockScreen(e);
                        var t = a("#ew-lock-screen-group");
                        e ? t.remove() : t.fadeOut("fast"), r.isLockScreen = !1, r.putTempData("isLockScreen", null, !0)
                    }, r.tips = function (e) {
                        return t.tips(e.text, e.elem, {
                            tips: [e.direction || 1, e.bg || "#191a23"],
                            tipsMore: e.tipsMore,
                            time: e.time || -1,
                            success: function (t) {
                                var i = a(t).children(".layui-layer-content");
                                if ((e.padding || 0 === e.padding) && i.css("padding", e.padding), e.color && i.css("color", e.color), e.bgImg && i.css("background-image", e.bgImg).children(".layui-layer-TipsG").css("z-index", "-1"), e.fontSize && i.css("font-size", e.fontSize), e.offset) {
                                    var n = e.offset.split(","), o = n[0], l = n.length > 1 ? n[1] : void 0;
                                    o && a(t).css("margin-top", o), l && a(t).css("margin-left", l)
                                }
                            }
                        })
                    }, r.renderTpl = function (e) {
                        function t(e) {
                            if (e) try {
                                return new Function("return " + e + ";")()
                            } catch (a) {
                                console.error(a + "\nlay-data: " + e)
                            }
                        }

                        layui.admin || (layui.admin = r), a(e || "[ew-tpl]").each((function () {
                            var e = a(this), i = a(this).data();
                            if (i.elem = e, i.tpl = e.html(), i.url = t(e.attr("ew-tpl")), i.headers = t(i.headers), i.where = t(i.where), i.done) try {
                                i.done = new Function("res", i.done)
                            } catch (e) {
                                console.error(e + "\nlay-data:" + i.done), i.done = void 0
                            }
                            r.util.render(i)
                        }))
                    }, r.on = function (e, a) {
                        return layui.onevent.call(this, "admin", e, a)
                    }, r.putSetting = function (e, a) {
                        i[e] = a, r.putTempData(e, a, !0)
                    }, r.recoverState = function () {
                        if (r.getTempData("isLockScreen", !0) && r.lockScreen(r.getTempData("lockScreenUrl", !0)), i.defaultTheme && r.changeTheme(i.defaultTheme, window, !0, !0), i.closeFooter && a("body").addClass("close-footer"), void 0 !== i.navArrow) {
                            var e = a(l + ">.layui-nav-tree");
                            e.removeClass("arrow2 arrow3"), i.navArrow && e.addClass(i.navArrow)
                        }
                        i.pageTabs && "true" == i.tabAutoRefresh && a(o).attr("lay-autoRefresh", "true")
                    }, r.on = function (e, a) {
                        return layui.onevent.call(this, "admin", e, a)
                    };
                    var c = ".layui-layout-admin.admin-nav-mini>.layui-side .layui-nav .layui-nav-item";
                    a(document).on("mouseenter", c + "," + c + " .layui-nav-child>dd", (function () {
                        if (r.getPageWidth() > 768) {
                            var e = a(this), t = e.find(">.layui-nav-child");
                            if (t.length > 0) {
                                e.addClass("admin-nav-hover"), t.css("left", e.offset().left + e.outerWidth());
                                var i = e.offset().top;
                                i + t.outerHeight() > r.getPageHeight() && ((i = i - t.outerHeight() + e.outerHeight()) < 60 && (i = 60), t.addClass("show-top")), t.css("top", i), t.addClass("ew-anim-drop-in")
                            } else e.hasClass("layui-nav-item") && r.tips({
                                elem: e,
                                text: e.find("cite").text(),
                                direction: 2,
                                offset: "12px"
                            })
                        }
                    })).on("mouseleave", c + "," + c + " .layui-nav-child>dd", (function () {
                        t.closeAll("tips");
                        var e = a(this);
                        e.removeClass("admin-nav-hover");
                        var i = e.find(">.layui-nav-child");
                        i.removeClass("show-top ew-anim-drop-in"), i.css({left: "auto", top: "auto"})
                    })), a(document).on("click", "*[ew-event]", (function () {
                        var e = r.events[a(this).attr("ew-event")];
                        e && e.call(this, a(this))
                    })), a(document).on("mouseenter", "*[lay-tips]", (function () {
                        var e = a(this);
                        r.tips({
                            elem: e,
                            text: e.attr("lay-tips"),
                            direction: e.attr("lay-direction"),
                            bg: e.attr("lay-bg"),
                            offset: e.attr("lay-offset"),
                            padding: e.attr("lay-padding"),
                            color: e.attr("lay-color"),
                            bgImg: e.attr("lay-bgImg"),
                            fontSize: e.attr("lay-fontSize")
                        })
                    })).on("mouseleave", "*[lay-tips]", (function () {
                        t.closeAll("tips")
                    })), a(document).on("click", ".form-search-expand,[search-expand]", (function () {
                        var e = a(this), t = e.parents(".layui-form").first(), i = e.data("expand"),
                            n = e.attr("search-expand");
                        if (void 0 === i || !0 === i) {
                            i = !0, e.data("expand", !1), e.html('收起 <i class="layui-icon layui-icon-up"></i>');
                            var o = t.find(".form-search-show-expand");
                            o.attr("expand-show", ""), o.removeClass("form-search-show-expand")
                        } else i = !1, e.data("expand", !0), e.html('展开 <i class="layui-icon layui-icon-down"></i>'), t.find("[expand-show]").addClass("form-search-show-expand");
                        n && new Function("d", n)({expand: i, elem: e})
                    })), a(document).on("click.ew-sel-fixed", ".ew-select-fixed .layui-form-select .layui-select-title", (function () {
                        var e = a(this), t = e.parent().children("dl"), i = e.offset().top, n = e.outerWidth(),
                            o = e.outerHeight(), l = a(document).scrollTop(), s = t.outerWidth(), c = t.outerHeight(),
                            d = i + o + 5 - l, u = e.offset().left;
                        d + c > r.getPageHeight() && (d = d - c - o - 10), u + s > r.getPageWidth() && (u = u - s + n), t.css({
                            left: u,
                            top: d,
                            "min-width": n
                        })
                    })), r.hideFixedEl = function () {
                        a(".ew-select-fixed .layui-form-select").removeClass("layui-form-selected layui-form-selectup"), a("body>.layui-laydate").remove()
                    }, a(document).on("click", ".layui-nav-tree>.layui-nav-item a", (function () {
                        var e = a(this), t = e.siblings(".layui-nav-child"), i = e.parent();
                        if (0 !== t.length && !i.hasClass("admin-nav-hover") && (i.hasClass("layui-nav-itemed") ? t.css("display", "none").slideDown("fast", (function () {
                            a(this).css("display", "")
                        })) : t.css("display", "block").slideUp("fast", (function () {
                            a(this).css("display", "")
                        })), "_all" === e.parents(".layui-nav").attr("lay-shrink"))) {
                            var n = e.parent().siblings(".layui-nav-itemed");
                            n.children(".layui-nav-child").css("display", "block").slideUp("fast", (function () {
                                a(this).css("display", "")
                            })), n.removeClass("layui-nav-itemed")
                        }
                    })), a('.layui-nav-tree[lay-shrink="all"]').attr("lay-shrink", "_all"), a(document).on("click", ".layui-collapse>.layui-colla-item>.layui-colla-title", (function () {
                        var e = a(this), t = e.siblings(".layui-colla-content"), i = e.parent().parent(),
                            n = t.hasClass("layui-show");
                        if (n ? t.removeClass("layui-show").slideDown("fast").addClass("layui-show") : t.css("display", "block").slideUp("fast", (function () {
                            a(this).css("display", "")
                        })), e.children(".layui-colla-icon").html("&#xe602;").css({
                            transition: "all .3s",
                            transform: "rotate(" + (n ? "90deg" : "0deg") + ")"
                        }), "_all" === i.attr("lay-shrink")) {
                            var o = i.children(".layui-colla-item").children(".layui-colla-content.layui-show").not(t);
                            o.css("display", "block").slideUp("fast", (function () {
                                a(this).css("display", "")
                            })), o.removeClass("layui-show"), o.siblings(".layui-colla-title").children(".layui-colla-icon").html("&#xe602;").css({
                                transition: "all .3s",
                                transform: "rotate(0deg)"
                            })
                        }
                    })), a(".layui-collapse[lay-accordion]").attr("lay-shrink", "_all").removeAttr("lay-accordion"), t.oldTips = t.tips, t.tips = function (e, i, n) {
                        var o;
                        if (a(i).length > 0 && a(i).parents(".layui-form").length > 0 && (a(i).is("input") || a(i).is("textarea") ? o = a(i) : (a(i).hasClass("layui-form-select") || a(i).hasClass("layui-form-radio") || a(i).hasClass("layui-form-checkbox") || a(i).hasClass("layui-form-switch")) && (o = a(i).prev())), !o) return t.oldTips(e, i, n);
                        n.tips = [o.attr("lay-direction") || 3, o.attr("lay-bg") || "#ff4c4c"], setTimeout((function () {
                            n.success = function (e) {
                                a(e).children(".layui-layer-content").css("padding", "6px 12px")
                            }, t.oldTips(e, i, n)
                        }), 100)
                    }, a(document).on("click", "*[ew-href]", (function () {
                        var e = a(this), t = e.attr("ew-href");
                        if (t && "#" !== t) {
                            if (0 === t.indexOf("javascript:")) return new Function(t.substring(11))();
                            var i = e.attr("ew-title") || e.text(), n = e.data("window");
                            n = n ? r.strToWin(n) : top;
                            var o = e.attr("ew-end");
                            try {
                                o = o ? new Function(o) : void 0
                            } catch (e) {
                                console.error(e)
                            }
                            n.layui && n.layui.index ? n.layui.index.openTab({
                                title: i || "",
                                url: t,
                                end: o
                            }) : location.href = t
                        }
                    })), layui.contextMenu || a(document).off("click.ctxMenu").on("click.ctxMenu", (function () {
                        try {
                            for (var e = top.window.frames, a = 0; a < e.length; a++) {
                                var t = e[a];
                                try {
                                    t.layui && t.layui.jquery && t.layui.jquery("body>.ctxMenu").remove()
                                } catch (e) {
                                }
                            }
                            try {
                                top.layui && top.layui.jquery && top.layui.jquery("body>.ctxMenu").remove()
                            } catch (e) {
                            }
                        } catch (e) {
                        }
                    })), i = a.extend({
                        pageTabs: !0,
                        cacheTab: !0,
                        openTabCtxMenu: !0,
                        maxTabNum: 20,
                        tableName: "easyweb-iframe",
                        apiNoCache: !0,
                        ajaxSuccessBefore: function (e, a, t) {
                            return !r.ajaxSuccessBefore || r.ajaxSuccessBefore(e, a, t)
                        },
                        getAjaxHeaders: function (e, a, t) {
                            return r.getAjaxHeaders ? r.getAjaxHeaders(e, a, t) : []
                        }
                    }, i);
                    var d = r.getTempData(!0);
                    if (d) for (var u = ["pageTabs", "cacheTab", "defaultTheme", "navArrow", "closeFooter", "tabAutoRefresh"], p = 0; p < u.length; p++) void 0 !== d[u[p]] && (i[u[p]] = d[u[p]]);
                    r.recoverState(), r.renderTpl(), r.setter = i, layui.device().ios && a("body").addClass("ios-iframe-body"), e("admin", r)
                }))
        }
    }, a = {};
    !function t(i) {
        var n = a[i];
        if (void 0 !== n) return n.exports;
        var o = a[i] = {exports: {}};
        return e[i](o, o.exports, t), o.exports
    }(199)
})();