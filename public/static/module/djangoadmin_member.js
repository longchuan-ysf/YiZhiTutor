/**
 * 会员管理
 * @author 一米阳光
 * @since 2021/7/26
 */
layui.use(['func', 'form'], function () {
    var func = layui.func;

    if (A == 'index') {
        //【TABLE列数组】
        var cols = [
            {type: 'checkbox', fixed: 'left'}
            , {field: 'id', width: 80, title: 'ID', align: 'center', sort: true, fixed: 'left'}
            , {field: 'username', width: 200, title: '用户账号', align: 'center'}
            , {field: 'source', width: 100, title: '用户来源', align: 'center', templet(d) {
                    var cls = "";
                    if (d.source == 1) {
                        // 网站注册
                        cls = "layui-btn-normal";
                    } else if (d.source == 2) {
                        // 客户端注册
                        cls = "layui-btn-warm";
                    } else if (d.source == 3) {
                        // 小程序注册
                        cls = "layui-btn-danger";
                    } else if (d.source == 4) {
                        // 手机站注册
                        cls = "layui-btn-primary";
                    } else if (d.source == 5) {
                        // 后台添加
                        cls = "layui-btn-disabled";
                    }
                    return '<span class="layui-btn ' + cls + ' layui-btn-xs">'+d.source_name+'</span>';
                }}
            , {field: 'avatar', width: 100, title: '用户头像', align: 'center', templet: function (d) {
                    var avatarStr = "";
                    if (d.avatar) {
                        avatarStr = '<a href="' + d.avatar + '" target="_blank"><img src="' + d.avatar + '" height="26" /></a>';
                    }
                    return avatarStr;
                }
            }
            , {field: 'realname', width: 120, title: '用户姓名', align: 'center'}
            , {field: 'nickname', width: 120, title: '用户昵称', align: 'center'}
            , {
                field: 'gender', width: 100, title: '性别', align: 'center', templet(d) {
                    var cls = "";
                    if (d.gender == 1) {
                        // 男
                        cls = "layui-btn-normal";
                    } else if (d.gender == 2) {
                        // 女
                        cls = "layui-btn-warm";
                    } else if (d.gender == 3) {
                        // 保密
                        cls = "layui-btn-danger";
                    }
                    return '<span class="layui-btn ' + cls + ' layui-btn-xs">' + d.gender_name + '</span>';
                }
            }
            , {
                field: 'status', width: 100, title: '状态', align: 'center', templet: function (d) {
                    return '<input type="checkbox" name="status" value="' + d.id + '" lay-skin="switch" lay-text="正常|禁用" lay-filter="status" ' + (d.status == 1 ? 'checked' : '') + '>';
                }
            }
            , {field: 'email', width: 200, title: '电子邮箱', align: 'center'}
            , {field: 'create_time', width: 180, title: '注册时间', align: 'center',templet:'<div>{{ layui.util.toDateString(d.create_time*1000, "yyyy-MM-dd HH:mm:ss") }}</div>'}
            , {fixed: 'right', width: 150, title: '功能操作', align: 'left', toolbar: '#toolBar'}
        ];

        //【渲染TABLE】
        func.tableIns(cols, "tableList");

        //【设置弹框】
        func.setWin("会员用户");

        //【设置状态】
        func.formSwitch('status', null, function (data, res) {
            console.log("开关回调成功");
        });
    }
});
