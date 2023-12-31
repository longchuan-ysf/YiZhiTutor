/**
 * 字典管理
 * @author 一米阳光
 * @since 2021/7/26
 */
layui.use(['layer', 'form', 'table', 'util', 'admin'], function () {
    var $ = layui.jquery;
    var layer = layui.layer;
    var form = layui.form;
    var table = layui.table;
    var util = layui.util;
    var admin = layui.admin;
    var selObj;  // 左表选中数据

    /* 渲染表格 */
    var insTb = table.render({
        elem: '#dictTable',
        url: '/dict/list',
        height: 'full-100',
        method: 'get',
        toolbar: ['<p>',
            '<button lay-event="add" class="layui-btn layui-btn-sm icon-btn"><i class="layui-icon">&#xe654;</i>添加</button>&nbsp;',
            '<button lay-event="edit" class="layui-btn layui-btn-sm layui-btn-warm icon-btn"><i class="layui-icon">&#xe642;</i>修改</button>&nbsp;',
            '<button lay-event="del" class="layui-btn layui-btn-sm layui-btn-danger icon-btn"><i class="layui-icon">&#xe640;</i>删除</button>',
            '</p>'].join(''),
        defaultToolbar: [],
        cols: [[
            {field: 'id', width: 80, title: 'ID', align: 'center'}
            ,{field: 'name', title: '字典名称'}
        ]],
        done: function (res, curr, count) {
            $('#dictTable+.layui-table-view .layui-table-body tbody>tr:first').trigger('click');
        }
    });

    /* 表格搜索 */
    form.on('submit(dictTbSearch)', function (data) {
        insTb.reload({where: data.field});
        return false;
    });

    /* 表格头工具栏点击事件 */
    table.on('toolbar(dictTable)', function (obj) {
        if (obj.event === 'add') { // 添加
            showEditModel();
        } else if (obj.event === 'edit') { // 修改
            showEditModel(selObj.data, selObj);
        } else if (obj.event === 'del') { // 删除
            doDel(selObj);
        }
    });

    /* 监听行单击事件 */
    table.on('row(dictTable)', function (obj) {
        selObj = obj;
        obj.tr.addClass('layui-table-click').siblings().removeClass('layui-table-click');
        insTb2.reload({where: {dict_id: obj.data.id}, page: {curr: 1}, url: '/dictdata/list'});
    });

    /* 显示表单弹窗 */
    function showEditModel(mData, obj) {
        admin.open({
            type: 1,
            title: (mData ? '修改' : '添加') + '字典',
            content: $('#dictEditDialog').html(),
            success: function (layero, dIndex) {
                // 回显表单数据
                form.val('dictEditForm', mData);
                // 表单提交事件
                form.on('submit(dictEditSubmit)', function (data) {
                    var loadIndex = layer.load(2);
                    $.post(mData ? '/dict/update' : '/dict/add', JSON.stringify(data.field), function (res) {
                        layer.close(loadIndex);
                        if (0 === res.code) {
                            layer.close(dIndex);
                            layer.msg(res.msg, {icon: 1});
                            if (obj) {
                                obj.update(data.field);
                            } else {
                                insTb.reload();
                            }
                        } else {
                            layer.msg(res.msg, {icon: 2});
                        }
                    }, 'json');
                    return false;
                });
            }
        });
    }

    /* 删除 */
    function doDel(obj) {
        layer.confirm('确定要删除此字典吗？', {
            skin: 'layui-layer-admin',
            shade: .1
        }, function (i) {
            layer.close(i);
            // 网络请求删除数据
            var index = null;
            $.ajax({
                type: "delete",
                url: '/dict/delete/' + obj.data.id,
                data: {},
                dataType: "json",
                contentType: false,
                processData: false,
                beforeSend: function () {
                    index = layer.msg("处理中,请稍后...", {
                        icon: 16
                        , shade: 0.01
                        , time: 0
                    });
                },
                success: function (res) {
                    if (res.code == 0) {
                        //0.5秒后关闭
                        layer.msg(res.msg, {icon: 1, time: 500}, function () {
                            layer.close(index);
                            obj.del();
                            $('#dictTable+.layui-table-view .layui-table-body tbody>tr:first').trigger('click');
                        });
                    } else {
                        layer.close(index);
                        layer.msg(res.msg, {icon: 5});
                        return false;
                    }
                },
                error: function () {
                    layer.close(index);
                    layer.msg("AJAX请求异常", {icon: 2});
                }
            });

        });
    }

    /* 渲染表格2 */
    var insTb2 = table.render({
        elem: '#dictDataTable',
        data: [],
        height: 'full-100',
        method: 'get',
        page: true,
        toolbar: ['<p>',
            '<button lay-event="add" class="layui-btn layui-btn-sm icon-btn"><i class="layui-icon">&#xe654;</i>添加</button>&nbsp;',
            '<button lay-event="del" class="layui-btn layui-btn-sm layui-btn-danger icon-btn"><i class="layui-icon">&#xe640;</i>删除</button>&nbsp;',
            '</p>'].join(''),
        cellMinWidth: 100,
        cols: [[
            {type: 'checkbox', fixed: 'left'}
            , {field: 'id', width: 80, title: 'ID', align: 'center', sort: true, fixed: 'left'}
            , {field: 'name', width: 150, title: '字典项名称', align: 'center'}
            , {field: 'value', width: 150, title: '字典项编码', align: 'center'}
            , {field: 'sort', width: 100, title: '排序号', align: 'center'}
            , {field: 'note', width: 200, title: '备注', align: 'center'}
            , {field: 'create_time', width: 180, title: '添加时间', align: 'center', templet:"<div>{{layui.util.toDateString(d.create_time*1000, 'yyyy-MM-dd HH:mm:ss')}}</div>"}
            , {field: 'update_time', width: 180, title: '更新时间', align: 'center', templet:"<div>{{layui.util.toDateString(d.update_time*1000, 'yyyy-MM-dd HH:mm:ss')}}</div>"}
            , {title: '操作', toolbar: '#dictDataTbBar', align: 'center', width: 120, minWidth: 120, fixed: 'right'}
        ]]
    });

    /* 表格2搜索 */
    form.on('submit(dictDataTbSearch)', function (data) {
        insTb2.reload({where: data.field, page: {curr: 1}});
        return false;
    });

    /* 表格2工具条点击事件 */
    table.on('tool(dictDataTable)', function (obj) {
        if (obj.event === 'edit') { // 修改
            showEditModel2(obj.data);
        } else if (obj.event === 'del') { // 删除
            doDel2(obj);
        }
    });

    /* 表格2头工具栏点击事件 */
    table.on('toolbar(dictDataTable)', function (obj) {
        if (obj.event === 'add') { // 添加
            showEditModel2();
        } else if (obj.event === 'del') { // 删除
            var checkRows = table.checkStatus('dictDataTable');
            if (checkRows.data.length === 0) {
                layer.msg('请选择要删除的数据', {icon: 2});
                return;
            }
            var ids = checkRows.data.map(function (d) {
                return d.id;
            });
            doDel2({ids: ids});
        }
    });

    /* 显示表单弹窗2 */
    function showEditModel2(mData) {
        admin.open({
            type: 1,
            title: (mData ? '修改' : '添加') + '字典项',
            content: $('#dictDataEditDialog').html(),
            success: function (layero, dIndex) {
                // 回显表单数据
                form.val('dictDataEditForm', mData);
                // 表单提交事件
                form.on('submit(dictDataEditSubmit)', function (data) {
                    data.field.dict_id = selObj.data.id;
                    var loadIndex = layer.load(2);
                    $.post(mData ? '/dictdata/update' : '/dictdata/add', JSON.stringify(data.field), function (res) {
                        layer.close(loadIndex);
                        if (0 === res.code) {
                            layer.close(dIndex);
                            layer.msg(res.msg, {icon: 1});
                            insTb2.reload({page: {curr: 1}});
                        } else {
                            layer.msg(res.msg, {icon: 2});
                        }
                    }, 'json');
                    return false;
                });
            }
        });
    }

    /* 删除2 */
    function doDel2(obj) {
        layer.confirm('确定要删除选中数据吗？', {
            skin: 'layui-layer-admin',
            shade: .1
        }, function (i) {
            layer.close(i);
            var ids = []
            if (obj.data) {
                ids = [obj.data.id]
            } else if (obj.ids) {
                ids = obj.ids;
            }
            // 网络请求删除数据
            var index = null;
            $.ajax({
                type: "delete",
                url: "/dictdata/delete/" + ids.join(","),
                data: {},
                dataType: "json",
                contentType: false,
                processData: false,
                beforeSend: function () {
                    index = layer.msg("处理中,请稍后...", {
                        icon: 16
                        , shade: 0.01
                        , time: 0
                    });
                },
                success: function (res) {
                    if (res.code == 0) {
                        //0.5秒后关闭
                        layer.msg(res.msg, {icon: 1, time: 500}, function () {
                            layer.close(index);
                            // 刷新数据
                            insTb2.reload({page: {curr: 1}});
                        });
                    } else {
                        layer.close(index);
                        layer.msg(res.msg, {icon: 5});
                        return false;
                    }
                },
                error: function () {
                    layer.close(index);
                    layer.msg("AJAX请求异常", {icon: 2});
                }
            });

        });
    }

});
