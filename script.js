function sendMessage() {
    var messageInput = document.getElementById('message-input');
    var message = messageInput.value;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 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' // 여기에 API 키를 넣어주세요.
        },
        body: JSON.stringify({ 'message': message })
    })
    .then(response => response.json())
    .then(data => {
        displayMessage('User: ' + message);
        displayMessage('ChatGPT: ' + data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });

    messageInput.value = '';
}

