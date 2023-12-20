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

    // 动态设置主题栏的字体大小
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
        links.forEach(function (link) {
            link.style.fontSize = contentFontSize + 'px';
        });
    }
}

window.onload = function () {
    adjustLayout(); // 你的布局调整函数

};

// window.onload = adjustLayout;
window.onresize = adjustLayout;
//点击做侧边栏的每个对话主题，向后台索取所有聊天信息


var currentSessionId = null;

function sendRequest(sessionId) {
    currentSessionId = sessionId;//存储当前的会话ID
    console.log("sendRequest called with sessionId:", sessionId);
    $.ajax({
        url: '/chat/thematic', // 替换为您的服务器端点
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({session_id: sessionId}),
        success: function (response) {
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
        error: function (xhr, status, error) {
            // 这里处理错误情况
            console.error('Error:', error);
        }
    });
}

//显示聊天信息
function displayMessages(data) {
    var chatContainer = document.getElementById('chat-container');
    chatContainer.innerHTML = ''; // 清空现有内容
    var userInfo = document.getElementById('userInfo');
    var avatarUrl = userInfo.getAttribute('data-avatar'); // 获取头像 URL
    data.messages.forEach(function (message) {
        var bubbleClass = message.sender === 'AI' ? 'bubble-right' : 'bubble-left';
        var avatarSrc = message.sender === 'AI' ? '/static/assets/images/ic_403.png' : avatarUrl;
        var avatarContainerClass = message.sender === 'AI' ? 'avatar-container-right' : 'avatar-container-left';
        // 媒体内容的 HTML
        var mediaHtml = '';
        if (message.media_type) {
            var mediaUrl = NGINX_URL + message.media_url;
            console.log(mediaUrl)
            if (message.media_type === 1) {
                mediaHtml = `<audio controls>
                            <source src="${mediaUrl}" type="audio/mpeg">
                            Your browser does not support the audio element.
                         </audio>`;
            } else if (message.media_type === 2) {
                // 图片
                mediaHtml = `<img src="${mediaUrl}" alt="Chat Image" style="max-width: 100%;" onclick="openModal('${mediaUrl}')">`;
                // mediaHtml = `<img src="${mediaUrl}" alt="Chat Image" style="max-width: 100%;">`;
            }
        }

        var html = `
            <div class="chat-message">
                <div class="${avatarContainerClass}">
                    <img src="${avatarSrc}" class="avatar"> <!-- 使用 avatarSrc -->
                </div>
                <div class="bubble ${bubbleClass}">
                    <div class="bubble-content">
                        ${mediaHtml} <!-- 媒体内容 -->
                        ${message.message_text}
                    </div>
                </div>
            </div>
        `;
        chatContainer.innerHTML += html;
        var chatContent = document.querySelector('.chat-content');
        chatContent.scrollTop = chatContent.scrollHeight;
    });
}

//将新加的对话主题添加到左侧栏显示
function addNewSessionToUI(sessionId) {
    var sessionsList = document.querySelector('.layui-nav-tree'); // 获取会话列表的UL元素
    var newSession = document.createElement('li'); // 创建一个新的LI元素
    newSession.className = 'layui-nav-item'; // 设置类名
    var sessionLink = document.createElement('a'); // 创建链接元素
    sessionLink.href = 'javascript:;';
    sessionLink.textContent = '新对话 '; // 这里可以设置为会话的实际名称或主题
    sessionLink.onclick = function () {
        sendRequest(sessionId);
    }; // 设置点击事件
    newSession.appendChild(sessionLink); // 把链接加到LI元素上
    // 将新会话插入到列表的最前面
    if (sessionsList.firstChild) {
        sessionsList.insertBefore(newSession, sessionsList.firstChild);
    } else {
        sessionsList.appendChild(newSession); // 如果列表为空，直接添加
    }

    setThematicFontSize();
    layui.use('element', function () {
        var element = layui.element;

        // 重新渲染导航栏
        element.render('nav', 'thematic');
    });
}

var isCreatingSession = false;
var hasActiveSession = false; // 新增变量跟踪是否有活跃会话
//点击加号,新加对话主题
function startConversation() {
    if (isCreatingSession || hasActiveSession) {
        // 如果正在创建会话或已有活跃会话，不执行操作
        console.log('Please use the active session or wait for the current process to finish.');
        return;
    }
    console.log("startConversation")
    isCreatingSession = true;
    // 显示加载动画或其他指示器给用户

    $.ajax({
        url: '/chat/thematic_add',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({info: '新建会话'}),
        success: function (response) {
            var sessionId = response.session_id;
            console.log(response)
            console.log("sessionId = ", sessionId)
            addNewSessionToUI(sessionId);
            hasActiveSession = true; // 标记为有活跃会话
            // 更新界面，如禁用新对话按钮
        },
        error: function (xhr, status, error) {
            console.error('Error creating new conversation:', error);
        },
        complete: function () {
            isCreatingSession = false;
        }
    });
}

//form表单向后台提交用户对话数据——后续被我换成websocket了，但是不想动页面布局，就沿用这个表单提交
layui.use("form", function () {
    var form = layui.form;

    form.on('submit(submitChat)', function (data) {
        var userInfo = document.getElementById('userInfo');
        var userID = userInfo.getAttribute('data-userid'); // 获取用户id
        // 阻止表单的默认提交行为
        event.preventDefault();
        // 检查 chat-text 是否为空
        if (!data.field['chat-text'] || data.field['chat-text'].trim() === '') {
            console.log('chat-text 为空，不提交到后台');
            event.preventDefault();
            return false;
        }
        //websocket发送请求
        socket.send(JSON.stringify({
            'chat-text': document.getElementById('chat-text').value,
            'session_id': currentSessionId,  // 包含 session_id
            'user_id': userID
        }));
        document.getElementById('chat-text').value = '';
        return false;  // 防止表单的默认提交行为
    });
});

function addMessageToChat(message) {
    var chatContainer = document.getElementById('chat-container');
    var chatContent = document.querySelector('.chat-content');
    var avatarUrl = document.getElementById('userInfo').getAttribute('data-avatar');

    var bubbleClass = message.sender === 'AI' ? 'bubble-right' : 'bubble-left';
    var avatarSrc = message.sender === 'AI' ? '/static/assets/images/ic_403.png' : avatarUrl;
    var avatarContainerClass = message.sender === 'AI' ? 'avatar-container-right' : 'avatar-container-left';

    var mediaHtml = '';
    if (message.media_type) {
        var mediaUrl = NGINX_URL + message.media_url;
        console.log(mediaUrl)
        if (message.media_type === 1) {
            mediaHtml = `<audio controls>
                            <source src="${mediaUrl}" type="audio/mpeg">
                            Your browser does not support the audio element.
                         </audio>`;
        } else if (message.media_type === 2) {
            // 图片
            mediaHtml = `<img src="${mediaUrl}" alt="Chat Image" style="max-width: 100%;" onclick="openModal('${mediaUrl}')">`;
            // mediaHtml = `<img src="${mediaUrl}" alt="Chat Image" style="max-width: 100%;">`;
        }
    }

    var html = `
        <div class="chat-message">
            <div class="${avatarContainerClass}">
                <img src="${avatarSrc}" class="avatar">
            </div>
            <div class="bubble ${bubbleClass}">
                <div class="bubble-content">
                    ${mediaHtml} <!-- 媒体内容 -->
                    ${message.message_text}
                </div>
            </div>
        </div>
    `;

    chatContainer.innerHTML += html;
    chatContent.scrollTop = chatContent.scrollHeight;
}

let socket = new WebSocket("ws://localhost:8000/chat/respon/");

socket.onopen = function (e) {
    console.log("[open] Connection established");
};


var tempBubble; // 用于临时存储AI回答的气泡
var tempText;
socket.onmessage = function (event) {
    var message = JSON.parse(event.data);
    if (message && message.code === 0) {
        if (message.msg === "save confirmation") {
            addMessageToChat(message.data);
            hasActiveSession = false;
        } else if (message.msg === "ai response") {
            switch (message.data.message_start_end) {
                case "start":
                    tempBubble = createAIBubble();
                    tempText = ''
                    break;
                case "message":
                    tempText = tempText + message.data.message;
                    updateAIBubble(tempBubble, tempText );
                    break;
                case "end":
                    finalizeAIBubble(tempBubble);
                    tempText = null;
                    tempBubble = null;
                    break;
            }
        } else {
            console.error("Unexpected message type or error from server");
        }
    }
};

socket.onerror = function (error) {
    console.error(`[error] ${error.message}`);
};

function createAIBubble() {
    var chatContainer = document.getElementById('chat-container');
    var bubble = document.createElement('div');
    bubble.className = "chat-message";
    chatContainer.appendChild(bubble);
    return bubble;
}

function updateAIBubble(bubble, text) {
    bubble.innerHTML = `
        <div class="avatar-container-right">
            <img src="/static/assets/images/ic_403.png" class="avatar">
        </div>
        <div class="bubble bubble-right">
            <div class="bubble-content">${text}</div>
        </div>
    `;
    var chatContent = document.querySelector('.chat-content');
    chatContent.scrollTop = chatContent.scrollHeight;
}

function finalizeAIBubble(bubble) {
    var chatContent = document.querySelector('.chat-content');
    chatContent.scrollTop = chatContent.scrollHeight;
}

