// 定义一个立即执行的函数表达式（IIFE）来创建一个封闭的作用域。
(() => {
    // 定义一个对象a，它将存储模块及其定义，这里的键是模块ID。
    var a = {
        // 模块971的定义。
        971: () => {
            // 使用layui框架的define方法定义一个模块，依赖于layer, element, admin模块。
            layui.define(["layer", "element", "admin"], (function (a) {
                // 使用layui的jquery、layer、element、admin模块。
                var e = layui.jquery, i = layui.layer, t = layui.element, n = layui.admin, l = n.setter,
                    o = ".layui-layout-admin>.layui-header",
                    s = ".layui-layout-admin>.layui-side>.layui-side-scroll",
                    u = ".layui-layout-admin>.layui-body",
                    r = u + ">.layui-tab",
                    d = u + ">.layui-body-header",
                    c = "admin-pagetabs",
                    m = "admin-side-nav",
                    y = {},
                    h = !1,
                    // 定义对象b，包含网页的Tab和视图加载相关的方法和属性。
                    b = {
                        // homeUrl: 用于存储主页的URL。
                        // mTabPosition: 存储当前激活Tab的位置。
                        // mTabList: 一个数组，用于存储所有打开的Tab信息。
                        homeUrl: undefined,
                        mTabPosition: undefined,
                        mTabList: [],

                        // loadView方法: 用于加载指定路径的视图到Tab中。
                        // 参数a是一个对象，通常包含menuPath（要加载的视图的路径）和其他可选信息。
                        loadView: function (a) {
                            console.log(`loadView: function; menuPath = ${a.menuPath}`);
                            // 检查传入的参数是否包含menuPath，如果没有menuPath则显示错误消息并返回。
                            if (!a.menuPath) return i.msg("url不能为空", {icon: 2, anim: 6});

                            // 如果页面Tabs功能启用，执行以下逻辑。
                            if (l.pageTabs) {
                                var o;
                                // 遍历所有Tab标题，检查是否已存在一个Tab与当前要加载的路径相同。
                                e(r + ">.layui-tab-title>li").each((function () {
                                    e(this).attr("lay-id") === a.menuPath && (o = true)
                                }));

                                // 如果没有找到相同的Tab。
                                if (!o) {
                                    // 检查当前打开的Tab数量是否已达到最大限制。
                                    if (b.mTabList.length + 1 >= l.maxTabNum) return i.msg("最多打开" + l.maxTabNum + "个选项卡", {
                                        icon: 2,
                                        anim: 6
                                    }), n.activeNav(b.mTabPosition);

                                    // 标记新Tab的添加，并添加新Tab。
                                    h = true,
                                    t.tabAdd(c, {
                                        id: a.menuPath,
                                        title: '<span class="title">' + (a.menuName || "") + "</span>",
                                        content: '<iframe class="admin-iframe" lay-id="' + a.menuPath + '" src="' + a.menuPath + '" onload="layui.index.hideLoading(this);" frameborder="0"></iframe>'
                                    }),
                                    // 显示加载动画。
                                    n.showLoading({
                                        elem: e('iframe[lay-id="' + a.menuPath + '"]').parent(),
                                        size: ""
                                    }),
                                    // 如果当前路径不是主页路径，更新Tab列表。
                                    a.menuPath !== b.homeUrl && b.mTabList.push(a),
                                    // 如果启用Tab缓存，将当前Tab列表放入临时数据。
                                    l.cacheTab && n.putTempData("indexTabs", b.mTabList);
                                }
                                // 如果传入参数指示不更改当前Tab，则不切换Tab，否则切换到新Tab。
                                a.noChange || t.tabChange(c, a.menuPath);
                            } else {
                                // 如果页面Tabs功能未启用，激活导航到指定路径。
                                n.activeNav(a.menuPath);
                                // 检查是否存在iframe，如果不存在则创建一个新的iframe。
                                var d = e(u + ">div>.admin-iframe");
                                if (0 === d.length) {
                                    // 创建新的iframe并插入到页面中。
                                    e(u).html([
                                        '<div class="layui-body-header">',
                                        '   <span class="layui-body-header-title"></span>',
                                        '   <span class="layui-breadcrumb pull-right" lay-filter="admin-body-breadcrumb" style="visibility: visible;"></span>',
                                        "</div>",
                                        '<div style="-webkit-overflow-scrolling: touch;">',
                                        '   <iframe class="admin-iframe" lay-id="',
                                        a.menuPath, '" src="', a.menuPath, '"',
                                        '      onload="layui.index.hideLoading(this);" frameborder="0"></iframe>',
                                        "</div>"
                                    ].join("")),
                                    // 显示加载动画。
                                    n.showLoading({
                                        elem: e('iframe[lay-id="' + a.menuPath + '"]').parent(),
                                        size: ""
                                    });
                                } else {
                                    // 如果iframe已存在，更新其src属性。
                                    n.showLoading({
                                        elem: d.parent(),
                                        size: ""
                                    }),
                                    d.attr("lay-id", a.menuPath).attr("src", a.menuPath);
                                }
                                // 更新面包屑导航。
                                e('[lay-filter="admin-body-breadcrumb"]').html(b.getBreadcrumbHtml(a.menuPath));
                                // 重置Tab列表。
                                b.mTabList.splice(0, b.mTabList.length),
                                // 根据是否是主页路径，设置Tab标题或清除Tab位置。
                                a.menuPath === b.homeUrl ?
                                    (b.mTabPosition = undefined, b.setTabTitle(e(a.menuName).text() || e(s + ' [lay-href="' + b.homeUrl + '"]').text() || "主页"))
                                    : (b.mTabPosition = a.menuPath, b.mTabList.push(a), b.setTabTitle(a.menuName));
                                // 如果不缓存Tab，清除缓存数据。
                                if (!l.cacheTab) {
                                    n.putTempData("indexTabs", b.mTabList),
                                    n.putTempData("tabPosition", b.mTabPosition)
                                }
                            }
                            // 如果屏幕宽度小于768像素，执行菜单折叠操作。
                            n.getPageWidth() <= 768 && n.flexible(true);
                        },

                        // loadHome方法：用于加载主页视图。
                        // 参数a是一个对象，包含主页的路径（menuPath）和其他可选设置。
                        loadHome: function (a) {
                            console.log("loadHome: function")
                            // 从临时数据中获取已打开的Tab列表（e）和当前Tab的位置（i）。
                            var e = n.getTempData("indexTabs"),
                                i = n.getTempData("tabPosition"),
                                // 检查是否需要加载设置（a.loadSetting），并确认是否启用了缓存的Tab（l.cacheTab）和是否存在已打开的Tab。
                                t = (void 0 === a.loadSetting || a.loadSetting) && l.cacheTab && e && e.length > 0;

                            // 连续执行以下操作：
                            // 1. 设置主页URL为a.menuPath。
                            // 2. 根据i（当前Tab位置）和t的值设置a.noChange。如果i存在且t为true，则a.noChange为true。
                            // 3. 如果页面Tabs未启用且t为true，或者不管Tabs是否启用都调用loadView方法加载视图。
                            if (b.homeUrl = a.menuPath, a.noChange = !!i && t, !l.pageTabs && t || b.loadView(a), t) {
                                // 如果t为true，则遍历已打开的Tab列表。
                                for (var o = 0; o < e.length; o++) {
                                    // 为每个Tab设置noChange属性。如果Tab的menuPath不是当前Tab位置，则设置为true。
                                    e[o].noChange = e[o].menuPath !== i,
                                    // 如果noChange为false，或者页面Tabs功能启用且a.onlyLast不为true，则加载该Tab的视图。
                                    (!e[o].noChange || l.pageTabs && !a.onlyLast) && b.loadView(e[o]);
                                }
                            }
                            // 移除页面加载动画。
                            n.removeLoading(void 0, false)
                        },

                        // openTab方法: 用于打开一个新的Tab。
                        // 参数a是一个包含url、title和可能的end函数的对象。
                        openTab: function (a) {
                             console.log("openTab: function")
                            // 检查当前窗口是否不是顶层窗口，且当前窗口没有顶层管理权限，且顶层窗口有layui和layui.index对象。
                            // 如果这些条件都满足，则在顶层窗口中打开新的Tab。
                            if (window !== top && !n.isTop() && top.layui && top.layui.index)
                                return top.layui.index.openTab(a);

                            // 如果提供了end函数，将其存储在y对象中，键为a.url。
                            a.end && (y[a.url] = a.end);
                            // 调用loadView方法加载新的视图，使用a.url作为menuPath和a.title作为menuName。
                            b.loadView({menuPath: a.url, menuName: a.title})
                        },

                        /// setTabCache方法: 用于设置Tab的缓存状态。
                        // 参数a是一个布尔值，指示是否启用Tab缓存。
                        setTabCache: function (a) {
                            console.log("setTabCache: function")
                            // 判断当前窗口是否不是顶层窗口，且当前窗口没有顶层管理权限，
                            // 同时顶层窗口有layui和layui.index对象。
                            // 如果这些条件满足，则在顶层窗口中设置Tab缓存状态。
                            return window !== top && !n.isTop() && top.layui && top.layui.index
                                   ? top.layui.index.setTabCache(a)
                                   // 如果当前窗口是顶层窗口或不满足上述条件，则在当前窗口设置Tab缓存状态。
                                   : (n.putSetting("cacheTab", a),
                                      // 如果a为true（即启用缓存），则将当前打开的Tab列表和Tab位置存储在临时数据中。
                                      a ? (n.putTempData("indexTabs", b.mTabList),
                                          // 使用void操作符返回undefined，终止表达式的进一步执行。
                                          void n.putTempData("tabPosition", b.mTabPosition))
                                      // 如果a为false（即禁用缓存），则调用clearTabCache方法清除Tab缓存。
                                      : b.clearTabCache());
                        },

                        // clearTabCache方法: 用于清除Tab缓存。
                        clearTabCache: function () {
                            console.log("clearTabCache: function")
                            // 设置临时数据中的"indexTabs"为null，这表示清除存储的已打开的Tab列表。
                            n.putTempData("indexTabs", null),
                            // 设置临时数据中的"tabPosition"为null，这表示清除存储的当前Tab的位置信息。
                            n.putTempData("tabPosition", null)
                        },

                        // setTabTitle方法: 用于设置Tab的标题。
                        // 参数a是要设置的标题文本，i是Tab的标识符。
                        setTabTitle: function (a, i) {
                            console.log("setTabTitle: function")
                            // 检查当前窗口是否不是顶层窗口，且当前窗口没有顶层管理权限，
                            // 同时顶层窗口有layui和layui.index对象。
                            // 如果这些条件都满足，则在顶层窗口中设置Tab标题。
                            if (window !== top && !n.isTop() && top.layui && top.layui.index)
                                return top.layui.index.setTabTitle(a, i);

                            // 如果启用了页面Tabs功能。
                            l.pageTabs
                                ? ( // 如果i未提供，则获取当前激活的Tab的lay-id。i = layui.layer
                                    i || (i = e(r + ">.layui-tab-title>li.layui-this").attr("lay-id")),
                                    // 如果有i，则为指定的Tab设置标题。
                                    i && e(r + '>.layui-tab-title>li[lay-id="' + i + '"] .title').html(a || "")
                                  )
                                : ( // 如果未启用页面Tabs功能。
                                    // 如果提供了标题a，则设置标题并调整样式。
                                    a ? (e(d + ">.layui-body-header-title").html(a), e(d).addClass("show"), e(o).css("box-shadow", "0 1px 0 0 rgba(0, 0, 0, .03)"))
                                      // 如果未提供标题a，则移除标题显示。
                                      : (e(d).removeClass("show"), e(o).css("box-shadow", ""))
                                  );
                        },

                        // setTabTitleHtml方法: 用于设置Tab标题的HTML内容。
                        // 参数a是HTML字符串，用于设置Tab标题。
                        setTabTitleHtml: function (a) {
                            console.log("setTabTitleHtml: function")
                            // 检查当前窗口是否不是顶层窗口，且当前窗口没有顶层管理权限，
                            // 同时顶层窗口有layui和layui.index对象。
                            // 如果这些条件都满足，则在顶层窗口中设置Tab标题的HTML内容。
                            if (window !== top && !n.isTop() && top.layui && top.layui.index)
                                return top.layui.index.setTabTitleHtml(a);

                            // 如果未启用页面Tabs功能。
                            if (!l.pageTabs) {
                                // 如果未提供HTML内容a，则移除标题显示。
                                if (!a) return e(d).removeClass("show");
                                // 如果提供了HTML内容a，则设置标题并显示。
                                e(d).html(a), e(d).addClass("show");
                            }
                        },

                        // getBreadcrumb方法: 用于获取当前页面的面包屑导航路径。
                        // 参数a是当前页面的标识符，通常是一个URL或者路径。
                        getBreadcrumb: function (a) {
                            console.log("getBreadcrumb: function")
                            // 如果未提供标识符a，则尝试从当前活动的iframe中获取其lay-id作为标识符。
                            a || (a = e(u + ">div>.admin-iframe").attr("lay-id"));

                            // 初始化面包屑数组。
                            var i = [];
                            // 查找对应于标识符a的导航元素。
                            var t = e(s).find('[lay-href="' + a + '"]');

                            // 使用for循环来构建面包屑路径。
                            // 初始条件是检查t是否有长度（即找到了对应的导航元素），
                            // 循环条件是t的长度不为0，
                            // 每次迭代将t更新为它的父级导航元素。
                            for (t.length > 0 && i.push(t.text().replace(/(^\s*)|(\s*$)/g, ""));
                                 0 !== (t = t.parent("dd").parent("dl").prev("a")).length;) {
                                // 将父级导航元素的文本添加到面包屑数组的开始，并去除首尾空白。
                                i.unshift(t.text().replace(/(^\s*)|(\s*$)/g, ""));
                            }

                            // 返回面包屑数组，包含从当前页面到顶级导航的路径。
                            return i;
                        },

                        // getBreadcrumbHtml方法: 用于获取当前页面的面包屑导航的HTML表示。
                        // 参数a是当前页面的标识符，通常是一个URL或者路径。
                        getBreadcrumbHtml: function (a) {
                             console.log("getBreadcrumbHtml: function")
                            // 在for循环的初始化部分，调用getBreadcrumb方法获取当前页面的面包屑导航数组，
                            // 并初始化面包屑HTML字符串。如果当前页面是主页，则不添加主页的链接，否则添加主页的链接。
                            for (var e = b.getBreadcrumb(a), i = a === b.homeUrl ? "" : '<a ew-href="' + b.homeUrl + '">首页</a>', t = 0; t < e.length - 1; t++) {
                                // 如果i不为空，向i添加一个分隔符。
                                i && (i += '<span lay-separator="">/</span>');
                                // 向i添加当前面包屑元素的HTML表示。
                                i += "<a><cite>" + e[t] + "</cite></a>";
                            }

                            // 返回构建的面包屑HTML字符串。
                            return i;
                        },

                        // hideLoading方法: 用于隐藏加载动画。
                        // 参数a可以是一个字符串（表示lay-id）或者一个DOM元素。
                        hideLoading: function (a) {
                            console.log("hideLoading: function")
                            // 检查参数a的类型。如果a不是字符串（即是DOM元素），获取其lay-id属性。
                            // 这里使用逗号来分隔两个表达式：首先是类型检查和可能的赋值，其次是执行removeLoading函数。
                            "string" != typeof a && (a = e(a).attr("lay-id")),
                            // 调用removeLoading方法移除加载动画。
                            // 选择器定位到具有指定lay-id的iframe或者在容器u中的所有iframe的父元素，
                            // 然后对这些元素的父元素移除加载动画。
                            n.removeLoading(e('iframe[lay-id="' + a + '"],' + u + " iframe[lay-id]").parent(), false);
                        },

                    },
                    p = ".layui-layout-admin .site-mobile-shade";

                // 以下代码属于一个复杂的函数或方法定义，涉及多个功能的实现。
                // 检查并添加移动端遮罩层，如果不存在则创建一个。点击遮罩层时触发flexible方法，用于切换侧边栏展开或折叠状态。
                0 === e(p).length && e(".layui-layout-admin").append('<div class="site-mobile-shade"></div>'),
                e(p).click((function () {
                    n.flexible(true);
                }));

                // 如果启用了页面Tabs功能且不存在任何Tab，则在页面中创建Tab的HTML结构。
                l.pageTabs && 0 === e(r).length && (e(u).html(
                    ['<div class="layui-tab" lay-allowClose="true" lay-filter="',
                     c,
                     '" lay-autoRefresh="',
                     "true" == l.tabAutoRefresh,
                     '">',
                     '   <ul class="layui-tab-title"></ul><div class="layui-tab-content"></div>',
                     "</div>",
                     '<div class="layui-icon admin-tabs-control layui-icon-prev" ew-event="leftPage"></div>',
                     '<div class="layui-icon admin-tabs-control layui-icon-next" ew-event="rightPage"></div>',
                     '<div class="layui-icon admin-tabs-control layui-icon-down">',
                     '   <ul class="layui-nav" lay-filter="admin-pagetabs-nav">',
                     '      <li class="layui-nav-item" lay-unselect>',
                     '         <dl class="layui-nav-child layui-anim-fadein">',
                     '            <dd ew-event="closeThisTabs" lay-unselect><a>关闭当前标签页</a></dd>',
                     '            <dd ew-event="closeOtherTabs" lay-unselect><a>关闭其它标签页</a></dd>',
                     '            <dd ew-event="closeAllTabs" lay-unselect><a>关闭全部标签页</a></dd>',
                     "         </dl>",
                     "      </li>",
                     "   </ul>",
                     "</div>"].join("")),
                    t.render("nav", "admin-pagetabs-nav")),

                // 绑定导航条点击事件，用于打开新的Tab或执行JavaScript代码。
                t.on("nav(" + m + ")", (function (a) {
                    console.log("打开新的Tab");
                    var i = e(a), t = i.attr("lay-href");
                    if (t && "#" !== t) {
                        if (0 === t.indexOf("javascript:")) return new Function(t.substring(11))();
                        var n = i.attr("ew-title") || i.text().replace(/(^\s*)|(\s*$)/g, ""), l = i.attr("ew-end");
                        try {
                            l = l ? new Function(l) : void 0;
                        } catch (a) {
                            console.error(a);
                        }
                        b.openTab({url: t, title: n, end: l}), layui.event.call(this, "admin", "side({*})", {href: t});
                    }
                })),

                // 绑定Tab切换事件，更新Tab位置，激活导航，可能触发页面滚动和刷新。
                t.on("tab(" + c + ")", (function () {
                    console.log("更新Tab位置");
                    var a = e(this).attr("lay-id");
                    b.mTabPosition = a !== b.homeUrl ? a : void 0,
                    l.cacheTab && n.putTempData("tabPosition", b.mTabPosition),
                    n.activeNav(a),
                    n.rollPage("auto"),
                    "true" != e(r).attr("lay-autoRefresh") || h || n.refresh(a, true),
                    h = false,
                    layui.event.call(this, "admin", "tab({*})", {layId: a});
                })),

                // 绑定tabDelete事件，处理Tab的删除逻辑。
                t.on("tabDelete(" + c + ")", function (a) {
                    console.log("Tab的删除逻辑");
                    // 从Tab列表中获取被删除的Tab信息。
                    var i = b.mTabList[a.index - 1]
                    // 如果找到该Tab，则执行一系列操作。
                    i && (b.mTabList.splice(a.index - 1, 1),  // 从Tab列表中移除该Tab。
                          l.cacheTab && n.putTempData("indexTabs", b.mTabList), // 如果启用了Tab缓存，则更新缓存中的Tab列表。
                          y[i.menuPath] && y[i.menuPath].call(), // 如果为Tab定义了特定的回调函数，则执行该函数。
                          layui.event.call(this, "admin", "tabDelete({*})", {layId: i.menuPath})), // 触发Tab删除的事件。
                    // 如果当前没有激活的Tab，则激活最后一个Tab。
                    0 === e(r + ">.layui-tab-title>li.layui-this").length && e(r + ">.layui-tab-title>li:last").trigger("click")
                })


                // 绑定文档的点击事件，用于导航菜单的显示和隐藏。
                e(document).off("click.navMore").on("click.navMore", "[nav-bind]", (function () {
                    var a = e(this).attr("nav-bind");
                    console.log("Clicked nav-bind: ", a);
                    console.log("Hiding all sub-menus",m);
                    console.log("Removing 'layui-this' class from all main menu items",o);

                    e('ul[lay-filter="' + m + '"]').addClass("layui-hide"),
                    e('ul[nav-id="' + a + '"]').removeClass("layui-hide"),
                    e(o + ">.layui-nav .layui-nav-item").removeClass("layui-this"),
                    e(this).parent(".layui-nav-item").addClass("layui-this"),
                    n.getPageWidth() <= 768 && n.flexible(false),
                    layui.event.call(this, "admin", "nav({*})", {navId: a});
                })),

                // 如果启用了Tab上下文菜单和页面Tabs，初始化上下文菜单。
                l.openTabCtxMenu && l.pageTabs && layui.use("contextMenu", (function () {
                    layui.contextMenu && e(r + ">.layui-tab-title").off("contextmenu.tab").on("contextmenu.tab", "li", (function (a) {
                        var i = e(this).attr("lay-id");
                        return layui.contextMenu.show([{
                            icon: "layui-icon layui-icon-refresh",
                            name: "刷新当前",
                            click: function () {
                                t.tabChange(c, i), "true" != e(r).attr("lay-autoRefresh") && n.refresh(i);
                            }
                        }, {
                            icon: "layui-icon layui-icon-close-fill ctx-ic-lg",
                            name: "关闭当前",
                            click: function () {
                                n.closeThisTabs(i);
                            }
                        }, {
                            icon: "layui-icon layui-icon-unlink",
                            name: "关闭其他",
                            click: function () {
                                n.closeOtherTabs(i);
                            }
                        }, {
                            icon: "layui-icon layui-icon-close ctx-ic-lg",
                            name: "关闭全部",
                            click: function () {
                                n.closeAllTabs();
                            }
                        }], a.clientX, a.clientY), false;
                    }));
                })), a("index", b)




            }))
        }
    }, e = {}; // 定义一个对象e，用于存储模块的exports。

    // 定义一个函数i，用于加载并执行指定ID的模块。
    !function i(t) {
        var n = e[t];
        if (void 0 !== n) return n.exports; // 如果模块已加载，返回其exports。
        var l = e[t] = {exports: {}}; // 初始化模块的exports对象。
        // 调用模块的函数，传递模块的exports和require函数。
        return a[t](l, l.exports, i), l.exports; // 返回模块的exports。
    }(971) // 加载并执行模块971。
})(); // IIFE结束。
