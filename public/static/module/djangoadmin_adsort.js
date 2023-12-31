/**
 * 广告位描述
 * @author 一米阳光
 * @since 2021/7/26
 */
layui.use(['func'], function () {

    //声明变量
    var func = layui.func
        , $ = layui.$;

    if (A == 'index') {
        //【TABLE列数组】
        var cols = [
            {type: 'checkbox', fixed: 'left'}
            , {field: 'id', width: 80, title: 'ID', align: 'center', sort: true, fixed: 'left'}
            , {field: 'name', width: 200, title: '广告位名称', align: 'center'}
            , {field: 'item_name', width: 150, title: '所属站点', align: 'center'}
            , {field: 'cate_name', width: 200, title: '所属栏目', align: 'center'}
            , {field: 'loc_id', width: 120, title: '广告页面位置', align: 'center'}
            , {field: 'platform', width: 100, title: '所属平台', align: 'center', templet(d) {
                    var cls = "";
                    if (d.platform == 1) {
                        // PC网站
                        cls = "layui-btn-normal";
                    } else if (d.platform == 2) {
                        // WAP手机站
                        cls = "layui-btn-danger";
                    } else if (d.platform == 3) {
                        // 微信小程序
                        cls = "layui-btn-warm";
                    } else if (d.platform == 4) {
                        // APP移动端
                        cls = "layui-btn-primary";
                    }
                    return '<span class="layui-btn ' + cls + ' layui-btn-xs">' + d.platform_name + '</span>';
                }
            }
            , {field: 'description', width: 200, title: '广告位描述', align: 'center'}
            , {field: 'sort', width: 100, title: '排序号', align: 'center'}
            , {field: 'create_time', width: 180, title: '添加时间', align: 'center', templet:"<div>{{layui.util.toDateString(d.create_time*1000, 'yyyy-MM-dd HH:mm:ss')}}</div>"}
            , {field: 'update_time', width: 180, title: '更新时间', align: 'center', templet:"<div>{{layui.util.toDateString(d.update_time*1000, 'yyyy-MM-dd HH:mm:ss')}}</div>"}
            , {fixed: 'right', width: 150, title: '功能操作', align: 'center', toolbar: '#toolBar'}
        ];

        //【渲染TABLE】
        func.tableIns(cols, "tableList");

        //【设置弹框】
        func.setWin("广告位描述",700, 450);

    }
});
