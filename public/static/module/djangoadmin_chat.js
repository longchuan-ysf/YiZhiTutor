/*
* 根据窗口的大小改编界面上面元素的大小
* */

function adjustLayout() {
    //------------------------聊天窗口的大小调整 -----------------------------------//
    var chatParentHeight = document.querySelector('.chat-body').offsetHeight;
    document.querySelectorAll('.chat-toolbar-icon').forEach(function (icon) {
        icon.style.fontSize = (chatParentHeight * 0.04) + 'px';
    });
    // 获取chat-toolbar-chatmain的宽度
    var messageInputContainer_w = document.querySelector('.message-input-container').offsetWidth;
    // 调整submitChat图标的大小
    var submitChatIcon = document.querySelector('.submit-icon');
    submitChatIcon.style.fontSize = (messageInputContainer_w * 0.08) + 'px'; //messageInputContainer_w
    //调整textArea字体的大小
     var textArea = document.getElementById('chat-text');
     var width = textArea.offsetWidth;
     var fontSize = width*0.04;
     textArea.style.fontSize = fontSize + 'px';



    //------------------------主题窗口的大小调整 -----------------------------------//
    // 动态设置主题栏的字体大小
    setThematicFontSize();


}

function setThematicFontSize() {
    // 计算并设置头部字体大小
    var thematicHeader = document.querySelector('.chat-thematic-header');
    if (thematicHeader) {
        var headerHeight = thematicHeader.offsetHeight;
        var headerFontSize = headerHeight * 0.30; // 字体大小为宽度的0.8%
        thematicHeader.style.fontSize = headerFontSize + 'px';
    }

    // 计算并设置内容字体大小
    var thematicContent = document.querySelector('.chat-thematic-content');
    if (thematicContent) {
        // 获取所有的layui-nav-item类的元素
        var items = thematicContent.querySelectorAll('.layui-nav-item');
        items.forEach(function (item) {
            // 获取每个<li>元素的高度
            var itemHeight = item.offsetHeight;
            // 计算字体大小为高度的50%
            var fontSize = itemHeight * 0.25;
            // 设置该<li>内的<a>元素的字体大小
            var link = item.querySelector('a');
            if (link) {
                link.style.fontSize = fontSize + 'px';
            }
        });
    }
}


window.onload = adjustLayout; // 你的布局调整函数
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
            if (data && data.data) {
                displayMessages(data.data.messages);
                updateSummary(data.data.summary);
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

function updateSummary(summary) {
    var container = $('.container'); // 获取容器
    container.empty(); // 清空现有内容

    // 遍历summary数组，为每个项创建HTML元素
    summary.forEach(function (item, index) {
        var panelClass = index === 0 ? 'panel active' : 'panel';
        var panel = $('<div class="' + panelClass + '">');
        panel.append('<div class="title-describe">' + item.title + '</div>');
        panel.append('<div class="content-describe">' + item.content + '</div>');
        container.append(panel); // 将新的panel添加到容器中
    });

    // 在添加新内容后重新绑定事件
    bindPanelClickEvents();
}

// 重新绑定点击事件到所有.panel元素
function bindPanelClickEvents() {
    const panels = document.querySelectorAll('.panel');
    panels.forEach((panel) => {
        panel.addEventListener('click', () => {
            removeActiveClasses(panels);
            panel.classList.add('active');
            console.log("click panel");
        });
    });
}

// 去除所有.panel元素的'active'类
function removeActiveClasses(panels) {
    panels.forEach((panel) => {
        panel.classList.remove('active');
    });
}

//显示聊天信息
function displayMessages(messages) {
    var chatContainer = document.getElementById('chat-container');
    chatContainer.innerHTML = ''; // 清空现有内容
    var userInfo = document.getElementById('userInfo');
    var avatarUrl = userInfo.getAttribute('data-avatar'); // 获取头像 URL
    messages.forEach(function (message) {
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
                    <div class="bubble-content">${mediaHtml}${message.message_text}</div>
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
    sessionLink.setAttribute('onclick', 'sendRequest(' + sessionId + ')');
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
    sessionLink.click();
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
        }
    }

    var html = `
        <div class="chat-message">
            <div class="${avatarContainerClass}">
                <img src="${avatarSrc}" class="avatar">
            </div>
            <div class="bubble ${bubbleClass}">
                <div class="bubble-content">${mediaHtml}${message.message_text}</div>
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
                    updateAIBubble(tempBubble, tempText);
                    break;
                case "end":
                    finalizeAIBubble(tempBubble);
                    tempText = null;
                    tempBubble = null;
                    break;
            }
        } else if (message.msg === "thematic change") {
            console.log(message.data)
            var newThematic = message.data.newThematic;
            var sessionId = message.data.sessionId;

            // 检查是否是当前活跃的会话
            if (sessionId === currentSessionId) {
                // 找到对应的会话链接并更新主题
                var sessionLinks = document.querySelectorAll('.chat-thematic-content a');
                sessionLinks.forEach(function (link) {
                    if (link.getAttribute('onclick').includes(sessionId)) {
                        link.textContent = newThematic;
                    }
                });
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

var imageUrl = ''; // 初始化图片URL变量
// 定义关闭图片预览的函数
function closeImagePreview() {
    console.log("closeImagePreview");
    imageUrl = '';

    var imgContainer = document.querySelector('.chat-form-image');
    var chatFormText = document.querySelector('.chat-form-text');
    var chatContent = document.querySelector('.chat-content');
    var chatForm = document.querySelector('.chat-form');
    var textArea = document.getElementById('chat-text'); // 获取textarea

    textArea.value  = '';
    chatContent.style.height = '75%'; // 将聊天内容区域高度改回75%
    chatForm.style.height = '20%'; // 将聊天表单区域高度改回20%
    // 隐藏图片容器并重置宽度
    imgContainer.style.display = 'none';
    imgContainer.style.height = '0%';
    // 重新调整文本区域的宽度
    chatFormText.style.height = '100%';
}


//form表单向后台提交用户对话数据——后续被我换成websocket了，但是不想动页面布局，就沿用这个表单提交
layui.use(["form", "croppers"], function () {
    var form = layui.form;
    var croppers = layui.croppers;
    croppers.render({
        elem: '#image_select', // Bind the cropper to the icon
        area: '750px', // Cropper window size or make it dynamic based on parameters
        url: '/upload/uploadImage', // Server URL to send the cropped image
        name: 'ChatImage',
        cancel: function (name) {
            $('.showImgEdit_ChatImage').hide();
        },
        done: function (url) {  // Callback after cropping and uploading
            imageUrl = url; // 初始化图片URL变量
            console.log("cropped image url:", url)
            //----------------------页面调整部分------------------------------------------------
            $('.showImgEdit_ChatImage').hide();
            // 显示图片和调整布局
            var imgContainer = document.querySelector('.chat-form-image');
            var img = imgContainer.querySelector('img');
            var chatFormText = document.querySelector('.chat-form-text');
            var chatContent = document.querySelector('.chat-content');
            var chatForm = document.querySelector('.chat-form');

            chatContent.style.height = '65%'; // 将聊天内容区域高度改为65%
            chatForm.style.height = '30%'; // 将聊天表单区域高度改为30%
            imgContainer.style.display = 'block'; // 显示图片容器
            img.src = imageUrl; // 设置图片路径

            // 设置图片和文本输入框的高度比为1:1
            imgContainer.style.height = '50%';
            chatFormText.style.height = '50%';

            //----------------------OCR图片识别部分------------------------------------------------
            $('.submit-icon').css('color', 'grey').prop('disabled', true);//开始前禁止提交按钮
            $.post("/chat/ocr_request", {imageUrl: url}, function (response) {
                console.log(response)
                if (response.code === 0) { // 判断OCR识别是否成功
                    // 显示数据在textarea
                    $('#chat-text').val(response.data);
                    // 恢复submit-icon的颜色并启用点击
                    $('.submit-icon').css('color', '#1E9FFF').prop('disabled', false);
                } else {
                    // 处理失败情况，可以根据需要设置
                    console.log("OCR failed: " + response.msg);
                    // 可以选择保持禁用或给出错误信息
                }
            });
        }
    });

    form.on('submit(submitChat)', function (data) {
        var userInfo = document.getElementById('userInfo');
        var userID = userInfo.getAttribute('data-userid'); // 获取用户id
        // 阻止表单的默认提交行为
        event.preventDefault();
        // console.log(data)
        //当发送信息不包含图片时，必需保证发送的内容不为空
        if (imageUrl.trim() === '') {
            // 检查 chat-text 是否为空(本身是否为空或者去掉首位空字符后是否为空)
            if (!data.field['chat-text'] || data.field['chat-text'].trim() === '') {
                console.log('chat-text 为空，不提交到后台');
                event.preventDefault();
                return false;
            }
        }
        var messageData = {
            'chat-text': document.getElementById('chat-text').value,
            'session_id': currentSessionId,
            'user_id': userID,
            'image_url':imageUrl
        };

        //websocket发送请求
        socket.send(JSON.stringify(messageData));
        document.getElementById('chat-text').value = '';
        if (imageUrl) {
            closeImagePreview();
        }
        return false;  // 防止表单的默认提交行为
    });
});