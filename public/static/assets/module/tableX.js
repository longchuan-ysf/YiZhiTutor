(() => {
    var e = {
        576: () => {
            layui.define(["layer", "table", "laytpl", "contextMenu"], (function (e) {
                var t = layui.jquery, a = layui.layer, o = layui.table, n = layui.laytpl, r = layui.contextMenu,
                    i = layui.device(), l = "txField_", d = {
                        merges: function (e, a, n, r) {
                            "boolean" == typeof n && (r = n, n = void 0);
                            for (var i = t('[lay-filter="' + e + '"]+.layui-table-view>.layui-table-box>.layui-table-body>table').find(">tbody>tr"), l = 0; l < a.length; l++) n ? c(e, a[l], n[l]) : c(e, a[l]);

                            function c(e, t, a) {
                                var n = o.cache[e];
                                if (n.length > 0) {
                                    var r, l = 1;
                                    r = a ? n[0][a] : i.eq(0).find("td").eq(t).find(".layui-table-cell").html();
                                    for (var d = 1; d < n.length; d++) {
                                        var c;
                                        if ((c = a ? n[d][a] : i.eq(d).find("td").eq(t).find(".layui-table-cell").html()) === r) {
                                            if (l++, d === n.length - 1) {
                                                i.eq(d - l + 1).find("td").eq(t).attr("rowspan", l);
                                                for (var s = 1; s < l; s++) i.eq(d - s + 1).find("td").eq(t).attr("del", "true")
                                            }
                                        } else {
                                            i.eq(d - l).find("td").eq(t).attr("rowspan", l);
                                            for (var u = 1; u < l; u++) i.eq(d - u).find("td").eq(t).attr("del", "true");
                                            l = 1, r = c
                                        }
                                    }
                                }
                            }

                            i.find('[del="true"]').remove(), (void 0 === r || r) && o.on("sort(" + e + ")", (function () {
                                d.merges(e, a, n, !1)
                            }))
                        }, bindCtxMenu: function (e, a) {
                            var n = o.cache[e], i = "#" + e + "+.layui-table-view .layui-table-body tr";
                            t(i).bind("contextmenu", (function (e) {
                                var o, l = t(this);
                                return t(i).removeClass("layui-table-click"), l.addClass("layui-table-click"), o = "function" == typeof a ? a(n[l.data("index")], e.currentTarget) : a, r.show(function e(a) {
                                    if (a) {
                                        for (var o = [], r = 0; r < a.length; r++) o.push({
                                            icon: a[r].icon,
                                            name: a[r].name,
                                            _click: a[r].click,
                                            click: function (e, a) {
                                                var o = t(a.currentTarget);
                                                this._click && this._click(n[o.data("index")], a.currentTarget), o.removeClass("layui-table-click")
                                            },
                                            subs: e(a[r].subs)
                                        });
                                        return o
                                    }
                                }(o), e.clientX, e.clientY, e), !1
                            }))
                        }, exportData: function (e) {
                            var t = e.cols, n = e.data, r = e.fileName, c = e.expType, s = e.option;
                            if (s || (s = {}), i.ie) return a.msg("不支持ie导出");
                            if ("string" == typeof n) {
                                var u = a.load(2);
                                return s.url = n, void d.loadUrl(s, (function (t) {
                                    a.close(u), e.data = t, d.exportData(e)
                                }))
                            }
                            for (var p = 0; p < t.length; p++) for (var f = 0; f < t[p].length; f++) void 0 === t[p][f].type && (t[p][f].type = "normal"), void 0 === t[p][f].hide && (t[p][f].hide = !1);
                            var v = [], h = [], m = [];
                            o.eachCols(void 0, (function (e, t) {
                                "normal" !== t.type || t.hide || (v.push(t.title || ""), h.push(t.field || l + e))
                            }), t);
                            for (var b = d.parseTbData(t, d.deepClone(n), !0), y = 0; y < b.length; y++) {
                                for (var x = [], g = 0; g < h.length; g++) {
                                    var w = b[y][h[g]];
                                    w && (w = w.toString().replace(/,/g, "，")), x.push(w)
                                }
                                m.push(x.join(","))
                            }
                            var D = document.createElement("a"),
                                C = {csv: "text/csv", xls: "application/vnd.ms-excel"}[c || "xls"],
                                k = encodeURIComponent(v.join(",") + "\r\n" + m.join("\r\n"));
                            D.href = "data:" + C + ";charset=utf-8,\ufeff" + k, D.download = (r || "table") + "." + (c || "xls"), document.body.appendChild(D), D.click(), document.body.removeChild(D)
                        }, exportDataX: function (e) {
                            layui.use("excel", (function () {
                                var t = layui.excel, n = e.cols, r = e.data, i = e.fileName, c = e.expType, s = e.option;
                                if (s || (s = {}), c || (c = "xlsx"), r && "string" == typeof r) {
                                    var u = a.load(2);
                                    return s.url = r, void d.loadUrl(s, (function (t) {
                                        a.close(u), e.data = t, d.exportDataX(e)
                                    }))
                                }
                                for (var p = 0; p < n.length; p++) for (var f = 0; f < n[p].length; f++) void 0 === n[p][f].type && (n[p][f].type = "normal"), void 0 === n[p][f].hide && (n[p][f].hide = !1);
                                var v = {}, h = [];
                                o.eachCols(void 0, (function (e, t) {
                                    if ("normal" === t.type && !t.hide) {
                                        var a = t.field || l + e;
                                        h.push(a), v[a] = t.title || ""
                                    }
                                }), n);
                                var m = d.parseTbData(n, d.deepClone(r), !0), b = t.filterExportData(m, h);
                                b.unshift(v), t.exportExcel({sheet1: b}, (i || "table") + "." + c, c)
                            }))
                        }, exportDataBack: function (e, a, o) {
                            if (a || (a = {}), o && "get" !== o.toString().toLowerCase()) {
                                var n = '<html><body><form id="eFrom" action="' + e + '" method="' + o + '">';
                                for (var r in a) n += '<textarea name="' + r + '">' + a[r] + "</textarea>";
                                n += "</form></body></html>", t("#exportFrame").remove(), t("body").append('<iframe id="exportFrame" style="display: none;"></iframe>');
                                var i = document.getElementById("exportFrame").contentWindow, l = i.document;
                                i.focus(), l.open(), l.write(n), l.close(), l.getElementById("eFrom").submit()
                            } else {
                                var d = "";
                                for (var c in a) d ? d += "&" + c + "=" + a[c] : d = "?" + c + "=" + a[c];
                                window.open(e + d)
                            }
                        }, render: function (e) {
                            var a = t(e.elem).attr("lay-filter");
                            e.autoSort = !1;
                            var n = o.render(e);
                            return o.on("sort(" + a + ")", (function (a) {
                                var o = a.field, r = a.type, i = t.extend(e.where, {sort: o, order: r});
                                n.reload({where: i, page: {curr: 1}})
                            })), n
                        }, renderFront: function (e) {
                            var a, n = t(e.elem).attr("lay-filter");
                            e.autoSort = !1;
                            for (var r = 0; r < e.cols.length; r++) for (var i = 0; i < e.cols[r].length; i++) e.cols[r][i].templet && !e.cols[r][i].field && (e.cols[r][i].field = l + r + "_" + i);
                            if (e.url) {
                                var c = d.deepClone(e);
                                c.data = [], c.url = void 0, (a = o.render(c)).reloadUrl = function (o) {
                                    var r = d.deepClone(e);
                                    o && (r = t.extend(r, o)), t(e.elem + "+.layui-table-view>.layui-table-box").append('<div class="layui-table-init"><i class="layui-icon layui-icon-loading layui-anim layui-anim-rotate layui-anim-loop"></i></div>'), d.loadUrl(r, (function (e) {
                                        a.reload({
                                            url: "",
                                            data: e,
                                            page: {curr: 1}
                                        }), d.putTbData(n, d.parseTbData(r.cols, e)), t('input[tb-search="' + n + '"]').val(""), window.tbX.cacheSearch[n] = void 0
                                    }))
                                }, a.reloadUrl()
                            } else (a = o.render(e)).reloadData = function (o) {
                                a.reload(o), d.parseTbData(e.cols, o.data), d.putTbData(n, o.data), t('input[tb-search="' + n + '"]').val(""), window.tbX.cacheSearch[n] = void 0
                            }, d.putTbData(n, d.parseTbData(e.cols, e.data));
                            return d.renderAllTool(a), a
                        }, loadUrl: function (e, o) {
                            e.response = t.extend({
                                statusName: "code",
                                statusCode: 0,
                                msgName: "msg",
                                dataName: "data",
                                countName: "count"
                            }, e.response);
                            var n = e.response, r = e.where;
                            e.contentType && 0 === e.contentType.indexOf("application/json") && (r = JSON.stringify(r)), t.ajax({
                                type: e.method || "get",
                                url: e.url,
                                contentType: e.contentType,
                                data: r,
                                dataType: "json",
                                headers: e.headers || {},
                                success: function (t) {
                                    if ("function" == typeof e.parseData && (t = e.parseData(t) || t), t[n.statusName] != n.statusCode) {
                                        var r = t[n.msgName] || "返回的数据不符合规范，正确的成功状态码 (" + n.statusName + ") 应为：" + n.statusCode;
                                        a.msg(r, {icon: 2})
                                    } else o(t[n.dataName])
                                },
                                error: function (e, t) {
                                    a.msg("数据接口请求异常：" + t, {icon: 2})
                                }
                            })
                        }, parseTbData: function (e, a, r) {
                            var i = [];
                            o.eachCols(void 0, (function (e, a) {
                                if (a.templet) {
                                    var o = {field: a.field && (r || 0 === a.field.indexOf(l)) ? a.field : "txField_" + e};
                                    "string" == typeof a.templet ? o.templet = function (e) {
                                        var o = void 0;
                                        return n(t(a.templet).html()).render(e, (function (e) {
                                            o = e
                                        })), o
                                    } : o.templet = a.templet, i.push(o)
                                }
                            }), e);
                            for (var d = 0; d < a.length; d++) for (var c = a[d], s = 0; s < i.length; s++) {
                                var u = "<div>" + i[s].templet(c) + "</div>";
                                c[i[s].field] = t(u).not(".export-hide").text().replace(/(^\s*)|(\s*$)/g, "")
                            }
                            return a
                        }, putTbData: function (e, t) {
                            window.tbX.cache[e] = t
                        }, getTbData: function (e) {
                            var t = window.tbX.cache[e];
                            return d.deepClone(t || o.cache[e])
                        }, filterData: function (e, t, a) {
                            for (var o, n = [], r = 0; r < e.length; r++) {
                                var i = e[r];
                                if (!o) if (t) o = t.split(","); else for (var l in o = [], i) i.hasOwnProperty(l) && o.push(l);
                                for (var c = 0; c < o.length; c++) if (d.isContains(i[o[c]], a)) {
                                    n.push(i);
                                    break
                                }
                            }
                            return n
                        }, isContains: function (e, t) {
                            return e || (e = ""), t || (t = ""), (e = e.toString().toLowerCase()) === (t = t.toString().toLowerCase()) || e.indexOf(t) >= 0
                        }, renderAllTool: function (e) {
                            u(e), s(e), c(e), p(e)
                        }, deepClone: function (e) {
                            var t, a = d.isClass(e);
                            if ("Object" === a) t = {}; else {
                                if ("Array" !== a) return e;
                                t = []
                            }
                            for (var o in e) if (e.hasOwnProperty(o)) {
                                var n = e[o];
                                "Object" === d.isClass(n) || "Array" === d.isClass(n) ? t[o] = arguments.callee(n) : t[o] = e[o]
                            }
                            return t
                        }, isClass: function (e) {
                            return null === e ? "Null" : void 0 === e ? "Undefined" : Object.prototype.toString.call(e).slice(8, -1)
                        }
                    };
                window.tbX || (window.tbX = {}), window.tbX.cache || (window.tbX.cache = {}), window.tbX.cacheSearch || (window.tbX.cacheSearch = {});
                var c = function (e) {
                    var o = e.config.id, n = t('input[tb-search="' + o + '"]');
                    n && n.length > 0 && (n.attr("placeholder") || n.attr("placeholder", "输入关键字按回车键搜索"), n.off("keydown").on("keydown", (function (t) {
                        if (13 === t.keyCode) {
                            var r = n.attr("name"), i = n.val().replace(/(^\s*)|(\s*$)/g, ""),
                                l = a.msg("搜索中..", {icon: 16, shade: .01, time: 0}), c = d.getTbData(o),
                                s = d.filterData(c, r, i);
                            window.tbX.cacheSearch[o] = s, e.reload({url: "", data: s, page: {curr: 1}}), a.close(l)
                        }
                    })))
                }, s = function (e) {
                    var t = e.config.id;
                    o.on("sort(" + t + ")", (function (o) {
                        var n = o.field, r = o.type, i = a.msg("加载中..", {icon: 16, shade: .01, time: 0}),
                            l = window.tbX.cacheSearch[t];
                        l || (l = d.getTbData(t)), r && (l = l.sort((function (e, t) {
                            var a = e[n], o = t[n];
                            return "asc" === r ? a === o ? 0 : a < o ? -1 : 1 : a === o ? 0 : a < o ? 1 : -1
                        }))), e.reload({initSort: o, url: "", data: l, page: {curr: 1}}), a.close(i)
                    }))
                }, u = function (e) {
                    t('[tb-refresh="' + e.config.id + '"]').off("click").on("click", (function () {
                        e.reloadUrl ? e.reloadUrl() : e.reload({page: {curr: 1}})
                    }))
                }, p = function (e) {
                    var n = e.config.id;
                    t('[tb-export="' + n + '"]').off("click").on("click", (function (r) {
                        t(this).find(".tbx-dropdown-menu").length > 0 || (void 0 !== r && (r.preventDefault(), r.stopPropagation()), t(this).append('<div class="tbx-dropdown-menu">      <div class="tbx-dropdown-menu-item" data-type="check">导出选中数据</div>      <div class="tbx-dropdown-menu-item" data-type="current">导出当前页数据</div>      <div class="tbx-dropdown-menu-item" data-type="all">导出全部数据</div>   </div>'), t(this).addClass("tbx-dropdown-btn"), t(this).parent().css("position", "relative"), t(this).parent().css("z-index", "9998"), t(".tbx-dropdown-menu").off("click").on("click", ".tbx-dropdown-menu-item", (function (r) {
                            var i = t(this).data("type");
                            if ("check" === i) {
                                var l = o.checkStatus(n);
                                0 === l.data.length ? a.msg("请选择要导出的数据", {icon: 2}) : (t(".tbx-dropdown-menu").remove(), d.exportData({
                                    fileName: e.config.title,
                                    cols: e.config.cols,
                                    data: l.data
                                }))
                            } else "current" === i ? d.exportData({
                                fileName: e.config.title,
                                cols: e.config.cols,
                                data: o.cache[n]
                            }) : "all" === i && d.exportData({
                                fileName: e.config.title,
                                cols: e.config.cols,
                                data: d.getTbData(n)
                            });
                            void 0 !== r && (r.preventDefault(), r.stopPropagation())
                        })))
                    })), t(document).off("click.tbxDropHide").on("click.tbxDropHide", (function () {
                        t(".tbx-dropdown-menu").remove()
                    }))
                };
                t("head").append('<style id="ew-css-tbx" type="text/css">.tbx-dropdown-btn {        position: relative;   }   .tbx-dropdown-btn:hover {        opacity: 1   }   .tbx-dropdown-menu {        position: absolute;        top: 100%;        right: 0;        padding: 5px 0;        margin: 5px 0 0 0;        overflow: visible;        min-width: 110px;        background: #fff;        border-radius: 2px;        box-shadow: 0 2px 4px rgba(0, 0, 0, .12);        border: 1px solid #d2d2d2;        z-index: 9998;        cursor: default;   }   .tbx-dropdown-menu .tbx-dropdown-menu-item {        display: block;        color: #555;        font-size: 14px;        padding: 10px 15px;        text-decoration: none;        white-space: nowrap;        cursor: pointer;        user-select: none;        line-height: normal;   }   .tbx-dropdown-menu .tbx-dropdown-menu-item:hover {        background-color: #eeeeee;   }   .export-show {        display: none;   }</style>'), e("tableX", d)
            }))
        }
    }, t = {};
    !function a(o) {
        var n = t[o];
        if (void 0 !== n) return n.exports;
        var r = t[o] = {exports: {}};
        return e[o](r, r.exports, a), r.exports
    }(576)
})();