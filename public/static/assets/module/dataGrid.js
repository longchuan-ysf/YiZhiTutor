(() => {
    var e = {
        543: () => {
            layui.define(["laytpl", "laypage", "form"], (function (e) {
                var t = layui.jquery, a = layui.laytpl, o = layui.laypage, i = layui.form, r = "DataGrid",
                    n = "ew-datagrid-loading", l = "ew-datagrid-item", d = "ew-loading", c = "ew-more-end",
                    s = {limit: 10, layout: ["prev", "page", "next", "skip", "count", "limit"]}, p = {
                        first: !0,
                        curr: 1,
                        limit: 10,
                        text: "加载更多",
                        loadingText: "加载中...",
                        noMoreText: "没有更多数据了~",
                        errorText: "加载失败，请重试"
                    }, h = function (e) {
                        this.options = t.extend(!0, {
                            method: "GET",
                            request: {pageName: "page", limitName: "limit"},
                            useAdmin: !1,
                            showError: function (e) {
                                t(this.elem).empty()
                            },
                            showEmpty: function (e) {
                                t(this.elem).empty()
                            },
                            showLoading: function () {
                                t(this.elem).addClass(n)
                            },
                            hideLoading: function () {
                                t(this.elem).removeClass(n)
                            }
                        }, e), e.page && (this.options.page = t.extend({}, s, !0 === e.page ? {} : e.page)), e.loadMore && (this.options.loadMore = t.extend({}, p, !0 === e.loadMore ? {} : e.loadMore)), "string" == typeof this.options.data && (this.options.url = this.options.data, this.options.data = void 0), this.init(), this.bindEvents()
                    };
                h.prototype.init = function () {
                    var e = this, a = this.options, o = this.getComponents();
                    if ("static" === o.$elem.css("position") && o.$elem.css("position", "relative"), a.checkAllElem) {
                        var r = o.$checkAll.find('input[lay-filter="' + o.checkAllFilter + '"]');
                        r.next(".layui-form-checkbox").remove(), r.remove(), o.$checkAll.append(['<input type="checkbox"', ' lay-filter="', o.checkAllFilter, '"', ' lay-skin="primary" class="ew-datagrid-checkbox" />'].join("")), o.$checkAll.hasClass("layui-form") || o.$checkAll.addClass("layui-form"), o.$checkAll.attr("lay-filter") || o.$checkAll.attr("lay-filter", a.checkAllElem.substring(1)), i.render("checkbox", o.$checkAll.attr("lay-filter"))
                    }
                    a.url ? a.reqData = function (e, o) {
                        a.where || (a.where = {}), a.where[a.request.pageName] = e.page, a.where[a.request.limitName] = e.limit, (a.useAdmin ? layui.admin : t).ajax({
                            url: a.url,
                            data: a.contentType && 0 === a.contentType.indexOf("application/json") ? JSON.stringify(a.where) : a.where,
                            headers: a.headers,
                            type: a.method,
                            dataType: "json",
                            contentType: a.contentType,
                            success: function (e) {
                                o(a.parseData ? a.parseData(e) : e)
                            },
                            error: function (e) {
                                o({code: e.status, msg: e.statusText, xhr: e})
                            }
                        })
                    } : a.data && (a.reqData = void 0, a.loadMore ? (e.renderLoadMore(), e.changeLoadMore(2), e.renderBody(a.data, 0, !1, !0), a.done && a.done(a.data, 1, a.data.length)) : a.page ? (a.page.count = a.data.length, a.page.jump = function (t, o) {
                        a.showLoading();
                        var i = (t.curr - 1) * a.page.limit, r = i + a.page.limit;
                        r > a.data.length && (r = a.data.length);
                        for (var n = [], l = i; l < r; l++) n.push(a.data[l]);
                        a.page.data = n, e.renderBody(n, (t.curr - 1) * t.limit, !1, !0), a.hideLoading(), 0 === a.data.length && a.showEmpty && a.showEmpty({}), a.done && a.done(n, t.curr, t.count)
                    }, e.renderPage()) : (e.renderBody(a.data, 0, !1, !0), 0 === a.data.length && a.showEmpty && a.showEmpty({}), a.done && a.done(a.data, 1, a.data.length))), a.reqData && (a.loadMore ? e.renderLoadMore().click((function () {
                        t(this).hasClass(d) || (a.loadMore.first ? a.loadMore.first = !1 : a.loadMore.curr++, e.changeLoadMore(1), a.reqData({
                            page: a.loadMore.curr,
                            limit: a.loadMore.limit
                        }, (function (t) {
                            if (0 != t.code) return e.changeLoadMore(3), void a.loadMore.curr--;
                            e.changeLoadMore(0), e.renderBody(t.data, (a.loadMore.curr - 1) * a.loadMore.limit, 1 !== a.loadMore.curr), a.done && a.done(t.data, a.loadMore.curr, t.count || t.data.length), (!t.data || t.data.length < a.loadMore.limit) && e.changeLoadMore(2)
                        })))
                    })).trigger("click") : a.page ? (a.showLoading(), a.reqData({
                        page: 1,
                        limit: a.page.limit
                    }, (function (t) {
                        return a.hideLoading(), "string" != typeof t && t.data ? 0 === t.data.length ? a.showEmpty && a.showEmpty(t) : (a.page.count = t.count, a.page.jump = function (t, o) {
                            o || (a.showLoading(), a.reqData({page: t.curr, limit: t.limit}, (function (o) {
                                return a.hideLoading(), "string" != typeof o && o.data ? 0 === o.data.length ? a.showEmpty && a.showEmpty(o) : (e.renderBody(o.data, (t.curr - 1) * t.limit), void (a.done && a.done(o.data, t.curr, t.count))) : a.showError && a.showError(o)
                            })))
                        }, e.renderPage(), e.renderBody(t.data), void (a.done && a.done(t.data, 1, t.count))) : a.showError && a.showError(t)
                    }))) : (a.showLoading(), a.reqData({}, (function (t) {
                        return a.hideLoading(), 0 != t.code ? a.showError && a.showError(t) : t.data && 0 !== t.data.length ? (e.renderBody(t.data), void (a.done && a.done(t.data, 1, t.data.length))) : a.showEmpty && a.showEmpty(t)
                    }))))
                }, h.prototype.bindEvents = function () {
                    var e = this, a = this.getComponents(), o = function (a) {
                        var o = t(this);
                        if (!o.hasClass(l)) {
                            var i = o.parent("." + l);
                            o = i.length > 0 ? i : o.parentsUntil("." + l).last().parent()
                        }
                        var r = o.data("index"), n = {
                            elem: o, data: e.getData(r), index: r, del: function () {
                                e.del(r)
                            }, update: function (t, a) {
                                e.update(r, t, a)
                            }
                        };
                        return t.extend(n, a)
                    };
                    a.$elem.off("click.item").on("click.item", ">." + l, (function () {
                        layui.event.call(this, r, "item(" + a.filter + ")", o.call(this, {}))
                    })), a.$elem.off("dblclick.itemDouble").on("click.itemDouble", ">." + l, (function () {
                        layui.event.call(this, r, "itemDouble(" + a.filter + ")", o.call(this, {}))
                    })), a.$elem.off("click.tool").on("click.tool", "[lay-event]", (function (e) {
                        layui.stope(e);
                        var i = t(this);
                        layui.event.call(this, r, "tool(" + a.filter + ")", o.call(this, {event: i.attr("lay-event")}))
                    })), i.on("radio(" + a.radioFilter + ")", (function (t) {
                        var o = e.getData(t.value);
                        o.LAY_CHECKED = !0, layui.event.call(this, r, "checkbox(" + a.filter + ")", {
                            checked: !0,
                            data: o
                        })
                    })), i.on("checkbox(" + a.checkboxFilter + ")", (function (t) {
                        var o = t.elem.checked, i = e.getData(t.value);
                        i.LAY_CHECKED = o, e.checkChooseAllCB(), layui.event.call(this, r, "checkbox(" + a.filter + ")", {
                            checked: o,
                            data: i
                        })
                    })), i.on("checkbox(" + a.checkAllFilter + ")", (function (o) {
                        var i = o.elem.checked, n = t(o.elem), l = n.next(".layui-form-checkbox");
                        if (!e.options.data || e.options.data.length <= 0) return n.prop("checked", !1), void l.removeClass("layui-form-checked");
                        a.$elem.find('input[name="' + a.checkboxFilter + '"]').each((function () {
                            var e = t(this);
                            e.prop("checked", i);
                            var a = e.next(".layui-form-checkbox");
                            i ? a.addClass("layui-form-checked") : a.removeClass("layui-form-checked")
                        }));
                        for (var d = 0; d < e.options.data.length; d++) e.options.data[d].LAY_CHECKED = i;
                        layui.event.call(this, r, "checkbox(" + a.filter + ")", {checked: i, type: "all"})
                    }))
                }, h.prototype.getComponents = function () {
                    var e = this, a = t(e.options.elem), o = a.attr("lay-filter");
                    return o || (o = e.options.elem.substring(1), a.attr("lay-filter", o)), {
                        $elem: a,
                        templetHtml: t(e.options.templet).html(),
                        $page: e.options.page && e.options.page.elem ? t("#" + e.options.page.elem) : void 0,
                        $loadMore: e.options.loadMore && e.options.loadMore.elem ? t("#" + e.options.loadMore.elem) : void 0,
                        filter: o,
                        checkboxFilter: "ew_tb_checkbox_" + o,
                        radioFilter: "ew_tb_radio_" + o,
                        checkAllFilter: "ew_tb_checkbox_all_" + o,
                        $checkAll: t(e.options.checkAllElem)
                    }
                }, h.prototype.renderBody = function (e, t, o, r) {
                    e || (e = []);
                    var n = this.options, l = this.getComponents();
                    t || (t = 0);
                    for (var d = [], c = 0; c < e.length; c++) {
                        var s = e[c];
                        if (s.LAY_INDEX = c, s.LAY_NUMBER = c + t + 1, s.LAY_CHECKBOX_ELEM = ['<input type="checkbox" lay-skin="primary"', ' name="', l.checkboxFilter, '"', ' lay-filter="', l.checkboxFilter, '"', s.LAY_CHECKED ? ' checked="checked"' : "", ' class="ew-datagrid-checkbox"', ' value="' + c + '" />'].join(""), s.LAY_RADIO_ELEM = ['<input type="radio"', ' name="', l.radioFilter, '"', ' lay-filter="', l.radioFilter, '"', s.LAY_CHECKED ? ' checked="checked"' : "", ' class="ew-datagrid-radio"', ' value="', c, '" />'].join(""), void 0 === l.templetHtml) return console.error("DataGrid Error: Template [" + n.templet + "] not found");
                        a(l.templetHtml).render(s, (function (e) {
                            d.push(e)
                        }))
                    }
                    o ? (r || (n.data = n.data.concat(e)), l.$elem.append(d.join(""))) : (r || (n.data = e), l.$elem.html(d.join(""))), this.initChildren(t), i.render("checkbox", l.filter), i.render("radio", l.filter), this.checkChooseAllCB()
                }, h.prototype.initChildren = function (e) {
                    e && this.options.page && this.options.page.data || (e = 0), this.getComponents().$elem.children().each((function (a) {
                        var o = t(this);
                        o.attr("data-index", a), o.attr("data-number", a + e + 1), o.addClass(l)
                    }))
                }, h.prototype.renderPage = function () {
                    var e = this.options, t = this.getComponents();
                    t.$elem.next(".ew-datagrid-page,.ew-datagrid-loadmore").remove(), e.page.elem = "ew-datagrid-page-" + e.elem.substring(1), t.$elem.after('<div class="ew-datagrid-page ' + (e.page.class || "") + '" id="' + e.page.elem + '"></div>'), o.render(e.page)
                }, h.prototype.renderLoadMore = function () {
                    var e = this.options, t = this.getComponents();
                    return t.$elem.next(".ew-datagrid-page,.ew-datagrid-loadmore").remove(), e.loadMore.elem = "ew-datagrid-page-" + e.elem.substring(1), t.$elem.after(['<div id="', e.loadMore.elem, '" ', 'class="ew-datagrid-loadmore ', e.loadMore.class || "", '">', "   <div>", '      <span class="ew-icon-loading">', '         <i class="layui-icon layui-icon-loading-1 layui-anim layui-anim-rotate layui-anim-loop"></i>', "      </span>", '      <span class="ew-loadmore-text">', e.loadMore.text, "</span>", "   </div>", "</div>"].join("")), t.$elem.next()
                }, h.prototype.changeLoadMore = function (e) {
                    var t = this.options, a = this.getComponents(), o = a.$loadMore.find(".ew-loadmore-text");
                    a.$loadMore.removeClass(d + " " + c), 0 === e ? o.html(t.loadMore.text) : 1 === e ? (o.html(t.loadMore.loadingText), a.$loadMore.addClass(d)) : 2 === e ? (o.html(t.loadMore.noMoreText), a.$loadMore.addClass(c)) : o.html(t.loadMore.errorText)
                }, h.prototype.update = function (e, o, i) {
                    var r = this, n = this.getComponents(), l = n.$elem.children('[data-index="' + e + '"]'),
                        d = l.data("number");
                    d - e != 1 ? t.extend(!0, this.options.data[d - 1], o) : t.extend(!0, this.options.data[e], o), 2 !== i && a(n.templetHtml).render(r.getData(e), (function (a) {
                        if (1 === i) return l.html(t(a).html());
                        l.before(a).remove(), r.initChildren(d - e - 1)
                    }))
                }, h.prototype.del = function (e) {
                    var t = this.getComponents().$elem.children('[data-index="' + e + '"]'), a = t.data("number");
                    t.remove(), a - e != 1 ? this.options.data.splice(a - 1, 1) : this.options.data.splice(e, 1), this.initChildren(a - e - 1)
                }, h.prototype.getData = function (e) {
                    if (void 0 === e) return this.options.data;
                    var t = this.getComponents().$elem.children('[data-index="' + e + '"]').data("number");
                    return t - e != 1 ? this.options.data[t - 1] : this.options.data[e]
                }, h.prototype.checkStatus = function () {
                    var e = this, a = this.getComponents(), o = a.checkboxFilter, i = a.radioFilter, r = [],
                        n = a.$elem.find('input[name="' + i + '"]');
                    if (n.length > 0) {
                        var l = n.filter(":checked").val();
                        if (void 0 !== l) {
                            var d = e.getData(l);
                            d && r.push(d)
                        }
                    } else a.$elem.find('input[name="' + o + '"]:checked').each((function () {
                        var a = t(this).val();
                        if (void 0 !== a) {
                            var o = e.getData(a);
                            o && r.push(o)
                        }
                    }));
                    return r
                }, h.prototype.checkChooseAllCB = function () {
                    for (var e = this.getComponents(), t = e.$checkAll.find('input[lay-filter="' + e.checkAllFilter + '"]'), a = 0 !== this.options.data.length, o = 0; o < this.options.data.length; o++) if (!this.options.data[o].LAY_CHECKED) {
                        a = !1;
                        break
                    }
                    a ? (t.prop("checked", !0), t.next(".layui-form-checkbox").addClass("layui-form-checked")) : (t.prop("checked", !1), t.next(".layui-form-checkbox").removeClass("layui-form-checked"))
                }, h.prototype.reload = function (e) {
                    e && (e.page ? (this.options.page ? e.page = t.extend({}, this.options.page, e.page) : e.page = t.extend({}, s, e.page), this.options.loadMore && (this.options.loadMore = void 0)) : e.loadMore && (this.options.loadMore ? e.loadMore = t.extend({}, this.options.loadMore, e.loadMore, {
                        first: !0,
                        curr: 1
                    }) : e.loadMore = t.extend({}, p, e.loadMore), this.options.page && (this.options.page = void 0)), t.extend(!0, this.options, e)), this.init()
                };
                var m = {
                    render: function (e) {
                        return e.onItemClick && m.onItemClick(e.elem, e.onItemClick), e.onToolBarClick && m.onToolBarClick(e.elem, e.onToolBarClick), new h(e)
                    }, on: function (e, t) {
                        return layui.onevent.call(this, r, e, t)
                    }, onItemClick: function (e, t) {
                        return 0 === e.indexOf("#") && (e = e.substring(1)), m.on("item(" + e + ")", t)
                    }, onToolBarClick: function (e, t) {
                        return 0 === e.indexOf("#") && (e = e.substring(1)), m.on("tool(" + e + ")", t)
                    }, autoRender: function (e) {
                        t(e || "[data-grid]").each((function () {
                            try {
                                var e = t(this), a = e.attr("id");
                                a || (a = "ew-datagrid-" + (t('[id^="ew-datagrid-"]').length + 1), e.attr("id", a));
                                var o = e.children("[data-grid-tpl]");
                                if (o.length > 0) {
                                    o.attr("id", a + "-tpl"), e.after(o);
                                    var i = function (e) {
                                        if (e) try {
                                            return new Function("return " + e)()
                                        } catch (t) {
                                            console.error("element property data- configuration item has a syntax error: " + e)
                                        }
                                    }(e.attr("lay-data"));
                                    i.elem = "#" + a, i.templet = "#" + a + "-tpl", m.render(i)
                                }
                            } catch (e) {
                                console.error(e)
                            }
                        }))
                    }
                };
                m.autoRender(), t("head").append(['<style id="ew-css-datagrid">', ".ew-datagrid-loadmore, .ew-datagrid-page {", "    text-align: center;", "}", ".ew-datagrid-loadmore {", "    color: #666;", "    cursor: pointer;", "}", ".ew-datagrid-loadmore > div {", "    padding: 12px;", "}", ".ew-datagrid-loadmore > div:hover {", "    background-color: rgba(0, 0, 0, .03);", "}", ".ew-datagrid-loadmore .ew-icon-loading {", "    margin-right: 6px;", "    display: none;", "}", ".ew-datagrid-loadmore.", c, " {", "    pointer-events: none;", "}", ".ew-datagrid-loadmore.", d, " .ew-icon-loading {", "    display: inline;", "}", ".", n, ":before {", '    content: "\\e63d";', "    font-family: layui-icon !important;", "    font-size: 32px;", "    color: #C3C3C3;", "    position: absolute;", "    left: 50%;", "    top: 50%;", "    margin-left: -16px;", "    margin-top: -16px;", "    z-index: 999;", "    -webkit-animatione: layui-rotate 1s linear;", "    animation: layui-rotate 1s linear;", "    -webkit-animation-iteration-count: infinite;", "    animation-iteration-count: infinite;", "}", ".ew-datagrid-checkbox + .layui-form-checkbox {", "   padding-left: 18px;", "}", ".ew-datagrid-radio + .layui-form-radio {", "   margin: 0;", "   padding: 0;", "   line-height: 22px;", "}", ".ew-datagrid-radio + .layui-form-radio .layui-icon {", "   margin-right: 0;", "}", "</style>"].join("")), e("dataGrid", m)
            }))
        }
    }, t = {};
    !function a(o) {
        var i = t[o];
        if (void 0 !== i) return i.exports;
        var r = t[o] = {exports: {}};
        return e[o](r, r.exports, a), r.exports
    }(543)
})();