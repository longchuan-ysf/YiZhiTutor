function adjustLayout() {
    var parentHeight = document.querySelector('.chat-body').offsetHeight;

    document.querySelector('.chat-content').style.height = (parentHeight * 0.75) + 'px';
    document.querySelector('.chat-tolbar-container').style.height = (parentHeight * 0.05) + 'px';
    document.querySelectorAll('.chat-toolbar-icon').forEach(function (icon) {
        icon.style.fontSize = (parentHeight * 0.04) + 'px';
    });
    document.querySelector('.chat-toolbar-chatmain').style.height = (parentHeight * 0.20) + 'px';
}

window.onload = adjustLayout;
window.onresize = adjustLayout;

layui.use("form", function () {
    var form = layui.form;

    form.on('submit(demo1)', function (data) {
        var formElement = document.querySelector('.layui-form');
        console.log('提交地址:', formElement.action);
        console.log('提交方法:', formElement.method);
        console.log("提交的内容:", JSON.stringify(data.field))
        // 阻止表单的默认提交行为
        event.preventDefault();

        // Ajax 请求
        $.ajax({
            url: data.form.action,  // 提交地址
            method: data.form.method,  // 提交方法
            data: data.field,  // 表单数据
            success: function(response) {
                // 根据返回的code判断操作是否成功
                if(response.code === 0) {
                    console.log("操作成功");
                    // 可以在这里更新页面内容或显示成功消息
                } else {
                    console.log("操作失败");
                    // 显示错误信息或处理失败情况
                }
            },
            error: function(xhr, status, error) {
                // 处理请求错误
                console.error('提交失败:', error);
            }
        });

        return false;  // 防止表单的默认提交行为
    });

});

