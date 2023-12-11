/*
* 根据窗口的大小改编界面上面元素的大小
* */
function adjustLayout() {
    //------------------------聊天窗口的大小调整 -----------------------------------//
    var chatParentHeight = document.querySelector('.chat-body').offsetHeight;
    document.querySelector('.chat-content').style.height = (chatParentHeight * 0.75) + 'px';
    document.querySelector('.chat-tolbar-container').style.height = (chatParentHeight * 0.05) + 'px';
    document.querySelectorAll('.chat-toolbar-icon').forEach(function (icon) {
        icon.style.fontSize = (chatParentHeight * 0.04) + 'px';
    });
    document.querySelector('.chat-toolbar-chatmain').style.height = (chatParentHeight * 0.20) + 'px';
    // 获取chat-toolbar-chatmain的宽度
    var messageInputContainer_w = document.querySelector('.message-input-container').offsetWidth;
    var messageInputContainer_h = document.querySelector('.message-input-container').offsetHeight;
    // 调整textarea的大小
    var textarea = document.querySelector('.text-edit');
    textarea.style.width = (messageInputContainer_w * 0.83) + 'px';  // 例如，设置宽度为chat-toolbar-chatmain宽度的80%
    textarea.style.height = (messageInputContainer_h * 0.7) + 'px'; // 自动高度，或者也可以设置一个基于chatToolbarChatmainWidth的值
    // 调整submitChat图标的大小
    var submitChatIcon = document.querySelector('.submit-icon');
    submitChatIcon.style.fontSize = (messageInputContainer_w * 0.07) + 'px'; //messageInputContainer_w

     //------------------------主题窗口的大小调整 -----------------------------------//
    var thematicParentHeight = document.querySelector('.chat-thematic').offsetHeight;
    document.querySelector('.chat-thematic-header').style.height = (thematicParentHeight * 0.08) + 'px';
    document.querySelector('.chat-thematic-content').style.height = (thematicParentHeight * 0.80) + 'px';

    // 动态设置字体大小
    setThematicFontSize();


}
function setThematicFontSize() {
    // 计算并设置头部字体大小
    var thematicHeader = document.querySelector('.chat-thematic-header');
    if (thematicHeader) {
        var headerWidth = thematicHeader.offsetWidth;
        var headerFontSize = headerWidth * 0.08; // 字体大小为宽度的0.8%
        thematicHeader.style.fontSize = headerFontSize + 'px';
    }

    // 计算并设置内容字体大小
    var thematicContent = document.querySelector('.chat-thematic-content');
    if (thematicContent) {
        var contentWidth = thematicContent.offsetWidth;
        var links = thematicContent.querySelectorAll('.layui-nav-item a');
        var contentFontSize = contentWidth * 0.06; // 示例：字体大小为宽度的0.03%
        links.forEach(function(link) {
            link.style.fontSize = contentFontSize + 'px';
        });
    }
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

function startConversation() {
    // 开始对话的逻辑
}

function sendRequest(sessionId) {
    $.ajax({
        url: '/chat/thematic', // 替换为您的服务器端点
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ session_id: sessionId }),
        success: function(response) {
            // var data = JSON.parse(response.data);
            var data;
            if (typeof response.data === 'string') {
                // 如果是字符串，则解析为 JSON
                data = JSON.parse(response.data);
            } else {
                // 如果已经是对象，则直接使用
                data = response.data;
            }

            console.log("Processed data:", data);

            // 检查 data 对象是否包含 messages 属性
            if (data && data.data && data.data.messages) {
                displayMessages(data.data);
            } else {
                console.error('Data does not contain messages');
            }
        },
        error: function(xhr, status, error) {
            // 这里处理错误情况
            console.error('Error:', error);
        }
    });
}

function displayMessages(data) {
    var chatContainer = document.getElementById('chat-container');
    chatContainer.innerHTML = ''; // 清空现有内容
    var userInfo = document.getElementById('userInfo');
    var avatarUrl = userInfo.getAttribute('data-avatar'); // 获取头像 URL
    data.messages.forEach(function(message) {
        var bubbleClass = message.sender === 'AI' ? 'bubble-right' : 'bubble-left';
        var avatarSrc = message.sender === 'AI' ? '/static/assets/images/ic_403.png' : avatarUrl;
        var avatarContainerClass = message.sender === 'AI' ? 'avatar-container-right' : 'avatar-container-left';

        var html = `
            <div class="chat-message">
                <div class="${avatarContainerClass}">
                    <img src="${avatarSrc}" class="avatar"> <!-- 使用 avatarSrc -->
                </div>
                <div class="bubble ${bubbleClass}">
                    <div class="bubble-content">
                        ${message.message_text}
                    </div>
                </div>
            </div>
        `;
        chatContainer.innerHTML += html;
    });
}


