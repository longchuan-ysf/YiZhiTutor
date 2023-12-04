(() => {
    var n = {
        351: () => {
            layui.define(["form", "layer", "laydate", "upload", "element", "base"], (function (n) {
                "use strict";
                var e = layui.form, t = void 0 === parent.layer ? layui.layer : top.layer, i = layui.laydate,
                    a = layui.upload, o = (layui.element, layui.base), r = layui.$, l = {
                        edit: function (n, e = 0, t = 0, i = 0, a = [], r = null, c = !1) {
                            var s = e > 0 ? "修改" : "新增";
                            o.isEmpty(n) ? s += "内容" : s += n;
                            var u = cUrl + "/edit/" + e;
                            if (Array.isArray(a)) for (var f in a) u += "?" + a[f];
                            l.showWin(s, u, t, i, a, 2, [], (function (n, e) {
                                r && r(n, e)
                            }), c)
                        }, detail: function (n, e, t = 0, i = 0, a = !1) {
                            var o = cUrl + "/detail/" + e;
                            l.showWin(n + "详情", o, t, i, [], 2, [], null, a)
                        }, cache: function (n) {
                            var e = cUrl + "/cache";
                            l.ajaxPost(e, {id: n}, (function (n, e) {
                            }))
                        }, copy: function (n, e, t = 0, i = 0) {
                            var a = cUrl + "/copy/" + e;
                            l.showWin(n + "复制", a, t, i)
                        }, delete: function (n, e = null) {
                            t.confirm("您确定要删除吗？删除后将无法恢复！", {
                                icon: 3,
                                skin: "layer-ext-moon",
                                btn: ["确认", "取消"]
                            }, (function (i) {
                                var a = cUrl + "/delete/" + n;
                                console.log(a), l.ajaxPost(a, {}, (function (n, a) {
                                    e && (t.close(i), e(n, a))
                                }), "正在删除。。。", "delete")
                            }))
                        }, batchFunc: function (n, e = null, i = "POST") {
                            var a = n.url, o = n.title, r = (n.form, n.confirm || !1), c = n.show_tips || "处理中...",
                                s = n.data || [], u = n.param || [], f = n.type || "POST";
                            if ("导出数据" != o && 0 == s.length) return t.msg("请选择数据", {icon: 5}), !1;
                            var d = [];
                            for (var m in s) d.push(s[m].id);
                            var y = d.join(","), p = {};
                            if (p.id = y, Array.isArray(u)) for (var m in u) {
                                var v = u[m].split("=");
                                p[v[0]] = v[1]
                            }
                            console.log(p), r ? t.confirm("您确定要【" + o + "】选中的数据吗？", {
                                icon: 3,
                                title: "提示信息"
                            }, (function (n) {
                                "POST" == f || "PUT" == f || "DELETE" == f ? a.indexOf("/delete") >= 0 ? l.ajaxPost(a + "/" + y, {}, e, c, i) : l.ajaxPost(a, p, e, c, i) : l.ajaxGet(a + "/" + y, {}, e, c)
                            })) : "POST" == f ? l.ajaxPost(a, p, e, c) : l.ajaxGet(a + "/" + y, {}, e, c)
                        }, verify: function () {
                            e.verify({
                                number: [/^[0-9]*$/, "请输入数字"], username: function (n, e) {
                                    return new RegExp("^[a-zA-Z0-9_一-龥\\s·]+$").test(n) ? /(^\_)|(\__)|(\_+$)/.test(n) ? title + "首尾不能出现下划线'_'" : /^\d+\d+\d$/.test(n) ? title + "不能全为数字" : void 0 : title + "不能含有特殊字符"
                                }, pass: [/^[\S]{6,12}$/, "密码必须6到12位，且不能出现空格"]
                            })
                        }, submitForm: function (n, e = null, t = null, i = !0) {
                            var a = [], c = [], s = n;
                            if (r.each(s, (function (n, e) {
                                if (console.log(n + ":" + e), /\[|\]|【|】/g.test(n)) {
                                    var t = n.match(/\[(.+?)\]/g);
                                    e = n.match("\\[(.+?)\\]")[1];
                                    var i = n.replace(t, "");
                                    r.inArray(i, a) < 0 && a.push(i), c[i] || (c[i] = []), c[i].push(e)
                                }
                            })), console.log(s), console.log(a), console.log(c), r.each(a, (function (n, e) {
                                var t = [];
                                r.each(c[e], (function (n, i) {
                                    t.push(i), delete s[e + "[" + i + "]"]
                                })), s[e] = t.join(",")
                            })), null == e) {
                                e = cUrl;
                                var u = "POST", f = r("form").attr("action");
                                o.isEmpty(f) ? null != n.id && (0 == n.id ? (e += "/add", u = "POST") : n.id > 0 && (e += "/update", u = "PUT")) : e = f
                            }
                            console.log(s), l.ajaxPost(e, JSON.stringify(s), (function (n, e) {
                                if (e) return i && setTimeout((function () {
                                    var n = parent.layer.getFrameIndex(window.name);
                                    parent.layer.close(n)
                                }), 500), t && t(n, e), !1
                            }), "数据提交中...", u)
                        }, searchForm: function (n, e, t = "tableList") {
                            n.reload(t, {page: {curr: 1}, where: e.field})
                        }, initDate: function (n, e = null) {
                            if (Array.isArray(n)) for (var t in n) {
                                var a = n[t].split("|");
                                if (a[2]) var o = a[2].split(",");
                                var r = {};
                                if (r.elem = "#" + a[0], r.type = a[1], r.theme = "molv", r.range = "true" === a[3] || a[3], r.calendar = !0, r.show = !1, r.position = "absolute", r.trigger = "click", r.btns = ["clear", "now", "confirm"], r.mark = {
                                    "0-06-25": "生日",
                                    "0-12-31": "跨年"
                                }, r.ready = function (n) {
                                }, r.change = function (n, e, t) {
                                }, r.done = function (n, t, i) {
                                    e && e(n, t)
                                }, o) {
                                    var l = o[0];
                                    if (l) {
                                        var c = !isNaN(l);
                                        r.min = c ? parseInt(l) : l
                                    }
                                    var s = o[1];
                                    if (s) {
                                        var u = !isNaN(s);
                                        r.max = u ? parseInt(s) : s
                                    }
                                }
                                i.render(r)
                            }
                        }, showWin: function (n, e, t = 0, i = 0, a = [], o = 2, l = [], c = null, s = !1) {
                            var u = layui.layer.open({
                                title: n,
                                type: o,
                                area: [t + "px", i + "px"],
                                content: e,
                                shadeClose: s,
                                shade: .4,
                                skin: "layui-layer-admin",
                                success: function (n, e) {
                                    if (Array.isArray(a)) for (var t in a) {
                                        var i = a[t].split("=");
                                        layui.layer.getChildFrame("body", e).find("#" + i[0]).val(i[1])
                                    }
                                    c && c(e, 1)
                                },
                                end: function () {
                                    c(u, 2)
                                }
                            });
                            0 == t && (layui.layer.full(u), r(window).on("resize", (function () {
                                layui.layer.full(u)
                            })))
                        }, ajaxPost: function (n, e, i = null, a = "处理中,请稍后...", o = "POST") {
                            var l = null;
                            r.ajax({
                                type: o,
                                url: n,
                                data: e,
                                dataType: "json",
                                contentType: !1,
                                processData: !1,
                                beforeSend: function () {
                                    l = t.msg(a, {icon: 16, shade: .01, time: 0})
                                },
                                success: function (n) {
                                    if (0 != n.code) return t.close(l), t.msg(n.msg, {icon: 5}), !1;
                                    t.msg(n.msg, {icon: 1, time: 500}, (function () {
                                        t.close(l), i && i(n, !0)
                                    }))
                                },
                                error: function () {
                                    t.close(l), t.msg("AJAX请求异常"), i && i(null, !1)
                                }
                            })
                        }, ajaxGet: function (n, e, i = null, a = "处理中,请稍后...") {
                            var o = null;
                            r.ajax({
                                type: "GET",
                                url: n,
                                data: e,
                                contentType: "application/json",
                                dataType: "json",
                                beforeSend: function () {
                                    o = t.msg(a, {icon: 16, shade: .01, time: 0})
                                },
                                success: function (n) {
                                    if (0 != n.code) return t.msg(n.msg, {icon: 5}), !1;
                                    t.msg(n.msg, {icon: 1, time: 500}, (function () {
                                        t.close(o), i && i(n, !0)
                                    }))
                                },
                                error: function () {
                                    t.msg("AJAX请求异常"), i && i(null, !1)
                                }
                            })
                        }, formSwitch: function (n, t = "", i = null, a = "处理中,请稍后...", r = "PUT") {
                            e.on("switch(" + n + ")", (function (e) {
                                var c = this.checked ? "1" : "2";
                                o.isEmpty(t) && (t = cUrl + "/" + n);
                                var s = {};
                                s.id = this.value, s[n] = c;
                                var u = JSON.stringify(s);
                                JSON.parse(u), console.log(s), l.ajaxPost(t, u, (function (n, e) {
                                    i && i(n, e)
                                }), a, r)
                            }))
                        }, uploadFile: function (n, e = null, i = "", r = "xls|xlsx", l = 10240, c = {}) {
                            o.isEmpty(i) && (i = cUrl + "/uploadFile"), a.render({
                                elem: "#" + n,
                                url: i,
                                auto: !1,
                                exts: r,
                                accept: "file",
                                size: l,
                                method: "post",
                                data: c,
                                before: function (n) {
                                    t.msg("上传并处理中。。。", {icon: 16, shade: .01, time: 0})
                                },
                                done: function (n) {
                                    return t.closeAll(), 0 == n.code ? t.alert(n.msg, {
                                        title: "上传反馈",
                                        skin: "layui-layer-molv",
                                        closeBtn: 1,
                                        anim: 0,
                                        btn: ["确定", "取消"],
                                        icon: 6,
                                        yes: function () {
                                            e && e(n, !0)
                                        },
                                        btn2: function () {
                                        }
                                    }) : t.msg(n.msg, {icon: 5}), !1
                                },
                                error: function () {
                                    return t.msg("数据请求异常")
                                }
                            })
                        }
                    };
                n("common", l)
            }))
        }
    }, e = {};
    !function t(i) {
        var a = e[i];
        if (void 0 !== a) return a.exports;
        var o = e[i] = {exports: {}};
        return n[i](o, o.exports, t), o.exports
    }(351)
})();