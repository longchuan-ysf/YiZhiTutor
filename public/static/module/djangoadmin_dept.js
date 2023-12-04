/**
 * 部门管理
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
              {field: 'id', width: 80, title: 'ID', align: 'center', sort: true}
            , {field: 'name', width: 300, title: '部门名称', align: 'left'}
            , {field: 'code', width: 150, title: '部门编码', align: 'center'}
            , {field: 'type', width: 100, title: '类型', align: 'center', templet(d) {
                if (d.type == 1) {
                    // 公司
                    return '<span class="layui-btn layui-btn-normal layui-btn-xs">公司</span>';
                } else if (d.type == 2) {
                    // 子公司
                    return '<span class="layui-btn layui-btn-warm layui-btn-xs">子公司</span>';
                } else if (d.type == 3) {
                    // 部门
                    return '<span class="layui-btn layui-btn-danger layui-btn-xs">部门</span>';
                } else if (d.type == 4) {
                    // 小组
                    return '<span class="layui-btn layui-btn-primary layui-btn-xs">小组</span>';
                }
            }}
            , {field: 'note', width: 250, title: '备注', align: 'center'}
            , {field: 'sort', width: 80, title: '排序', align: 'center'}
            , {field: 'create_time', width: 180, title: '添加时间', align: 'center', templet:"<div>{{layui.util.toDateString(d.create_time*1000, 'yyyy-MM-dd HH:mm:ss')}}</div>"}
            , {field: 'update_time', width: 180, title: '更新时间', align: 'center', templet:"<div>{{layui.util.toDateString(d.update_time*1000, 'yyyy-MM-dd HH:mm:ss')}}</div>"}
            , {width: 220, title: '功能操作', align: 'left', toolbar: '#toolBar'}
        ];

        //【渲染TABLE】
        func.treetable(cols, "tableList");

        //【设置弹框】
        func.setWin("部门", 600, 480);

    }
});
