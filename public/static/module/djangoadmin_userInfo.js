/**
 * 个人中心
 * @author 一米阳光
 * @since 2021/7/26
 */
layui.use(['form', 'element', 'admin', 'func'], function () {
    var $ = layui.jquery;
    var form = layui.form;
    var func = layui.func;

    /* 选择头像 */
    $('#userInfoHead').click(function () {
        return false;
    });

    /* 监听表单提交 */
    form.on('submit(userInfoSubmit)', function (data) {
        func.ajaxPost("/userInfo", JSON.stringify(data.field));
        return false;
    });

});
