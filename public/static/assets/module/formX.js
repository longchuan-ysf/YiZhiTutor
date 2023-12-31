(() => {
    var t = {
        101: () => {
            layui.define(["form"], (function (t) {
                var e = layui.jquery, i = layui.form, n = {
                    phoneX: "请输入正确的手机号",
                    emailX: "邮箱格式不正确",
                    urlX: "链接格式不正确",
                    numberX: "只能填写数字",
                    dateX: "日期格式不正确",
                    identityX: "请输入正确的身份证号",
                    psw: "密码必须5到12位，且不能出现空格",
                    equalTo: "两次输入不一致",
                    digits: "只能输入整数",
                    digitsP: "只能输入正整数",
                    digitsN: "只能输入负整数",
                    digitsPZ: "只能输入正整数和0",
                    digitsNZ: "只能输入负整数和0",
                    minlength: "最少输入{minlength}个字符",
                    maxlength: "最多输入{maxlength}个字符",
                    min: "值不能小于{min}",
                    max: "值不能大于{max}"
                }, a = {
                    phoneX: function (t, e) {
                        if (t && !/^1\d{10}$/.test(t)) return n.phoneX
                    }, emailX: function (t, e) {
                        if (t && !/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(t)) return n.emailX
                    }, urlX: function (t, e) {
                        if (t && !/(^#)|(^http(s*):\/\/[^\s]+\.[^\s]+)/.test(t)) return n.urlX
                    }, numberX: function (t, e) {
                        if (t && isNaN(t)) return n.numberX
                    }, dateX: function (t, e) {
                        if (t && !/^(\d{4})[-\/](\d{1}|0\d{1}|1[0-2])([-\/](\d{1}|0\d{1}|[1-2][0-9]|3[0-1]))*$/.test(t)) return n.dateX
                    }, identityX: function (t, e) {
                        if (t && !/(^\d{15}$)|(^\d{17}(x|X|\d)$)/.test(t)) return n.identityX
                    }, psw: function (t, e) {
                        if (t && !/^[\S]{5,12}$/.test(t)) return n.psw
                    }, equalTo: function (t, i) {
                        if (t != e(e(i).attr("lay-equalTo")).val()) return e(i).attr("lay-equalToText") || n.equalTo
                    }, digits: function (t, e) {
                        if (t && !/^-?\d+$/.test(t)) return n.digits
                    }, digitsP: function (t, e) {
                        if (t && !/^[1-9]\d*$/.test(t)) return n.digitsP
                    }, digitsN: function (t, e) {
                        if (t && !/^-[1-9]\d*$/.test(t)) return n.digitsN
                    }, digitsPZ: function (t, e) {
                        if (t && !/^\d+$/.test(t)) return n.digitsPZ
                    }, digitsNZ: function (t, e) {
                        if (t && !/^-[1-9]\d*|0/.test(t)) return n.digitsNZ
                    }, h5: function (t, i) {
                        if (t) {
                            var a = e(i).attr("minlength"), r = e(i).attr("maxlength"), d = e(i).attr("min"),
                                l = e(i).attr("max");
                            if (a && t.length < a) return n.minlength.replace(/{minlength}/g, a);
                            if (r && t.length > r) return n.maxlength.replace(/{maxlength}/g, r);
                            if (d && 1 * t < 1 * d) return n.min.replace(/{min}/g, d);
                            if (l && 1 * t > 1 * l) return n.max.replace(/{max}/g, l)
                        }
                    }
                }, r = {
                    init: function () {
                        i.verify(a)
                    }, formVal: function (t, e) {
                        r.val(t, e)
                    }, val: function (t, n) {
                        e('.layui-form[lay-filter="' + t + '"]').each((function () {
                            var t = e(this);
                            for (var i in n) if (n.hasOwnProperty(i)) {
                                var a = t.find('[name="' + i + '"]');
                                if (a.length > 0) {
                                    var r = a[0].type;
                                    "checkbox" === r ? a[0].checked = n[i] : "radio" === r ? a.each((function () {
                                        this.value == n[i] && (this.checked = !0)
                                    })) : a.val(n[i])
                                }
                            }
                        })), i.render(null, t)
                    }, renderSelect: function (t) {
                        if ("string" == typeof (t = e.extend({
                            elem: void 0,
                            data: [],
                            name: void 0,
                            value: void 0,
                            hint: "请选择",
                            initValue: void 0,
                            method: "get",
                            where: void 0,
                            headers: void 0,
                            async: !0,
                            done: void 0,
                            error: void 0
                        }, t)).data) e.ajax({
                            url: t.data,
                            type: t.method,
                            data: t.where,
                            dataType: "json",
                            headers: t.header || t.headers,
                            async: t.async,
                            success: function (e, i, n) {
                                e.data ? (t.data = e.data, r.renderSelect(t)) : t.error && t.error(n, e)
                            },
                            error: t.error
                        }); else {
                            for (var n = t.hint ? '<option value="">' + t.hint + "</option>" : "", a = 0; a < t.data.length; a++) t.name && t.value ? n += '<option value="' + t.data[a][t.value] + '"' + (t.data[a][t.value] == t.initValue ? " selected" : "") + ">" + t.data[a][t.name] + "</option>" : n += '<option value="' + t.data[a] + '"' + (t.data[a] == t.initValue ? " selected" : "") + ">" + t.data[a] + "</option>";
                            e(t.elem).html(n);
                            var d = e(t.elem).parent(".layui-form");
                            0 === d.length && (d = e(t.elem).parentsUntil(".layui-form").last().parent()), i.render("select", d.attr("lay-filter")), t.done && t.done(t.data)
                        }
                    }, startTimer: function (t, i, n) {
                        i || (i = 60), n || (n = function (t) {
                            return t + "s"
                        }), r.timers[t] && clearInterval(r.timers[t]);
                        var a = e(t).html();
                        e(t).html(n(i)), e(t).prop("disabled", !0), e(t).addClass("layui-btn-disabled");
                        var d = setInterval((function () {
                            --i <= 0 ? (clearInterval(d), e(t).html(a), e(t).removeProp("disabled"), e(t).removeClass("layui-btn-disabled")) : e(t).html(n(i))
                        }), 1e3);
                        r.timers[t] = d
                    }, timers: {}, formUpdatedField: function (t, e) {
                        for (var n in "string" == typeof t && (t = i.val(t)), t) t.hasOwnProperty(n) && t[n] === e[n] && delete t[n];
                        if (Object.keys(t).length > 0) return t
                    }
                };
                r.init(), t("formX", r)
            }))
        }
    }, e = {};
    !function i(n) {
        var a = e[n];
        if (void 0 !== a) return a.exports;
        var r = e[n] = {exports: {}};
        return t[n](r, r.exports, i), r.exports
    }(101)
})();