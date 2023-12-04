/**
 * 城市管理
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
            , {field: 'name', width: 200, title: '城市名称', align: 'left'}
            , {field: 'area_code', width: 150, title: '城市区号', align: 'center'}
            , {field: 'area_code', width: 150, title: '行政编码', align: 'center'}
            , {field: 'parent_code', width: 150, title: '父级编码', align: 'center'}
            , {field: 'level', width: 100, title: '城市级别', align: 'center', templet(d) {
                var cls = "";
                if (d.level == 1) {
                    // 省份
                    cls = "layui-btn-normal";
                } else if (d.level == 2) {
                    // 市区
                    cls = "layui-btn-danger";
                } else if (d.level == 3) {
                    // 区县
                    cls = "layui-btn-warm";
                } else if (d.platform == 4) {
                    // 街道
                    cls = "layui-btn-primary";
                }
				return '<span class="layui-btn ' + cls + ' layui-btn-xs">'+d.level_name+'</span>';
            }}
            , {field: 'zip_code', width: 100, title: '邮政编码', align: 'center'}
            , {field: 'short_name', width: 200, title: '城市简称', align: 'center'}
            , {field: 'pinyin', width: 150, title: '城市拼音', align: 'center'}
            , {field: 'create_time', width: 180, title: '添加时间', align: 'center', templet:"<div>{{layui.util.toDateString(d.create_time*1000, 'yyyy-MM-dd HH:mm:ss')}}</div>"}
            , {field: 'update_time', width: 180, title: '更新时间', align: 'center', templet:"<div>{{layui.util.toDateString(d.update_time*1000, 'yyyy-MM-dd HH:mm:ss')}}</div>"}
            , {width: 230, title: '功能操作', align: 'left', toolbar: '#toolBar'}
        ];

        //【渲染TABLE】
        func.treetable(cols, "tableList");

        //【设置弹框】
        func.setWin("城市",750, 450);

    }
});
