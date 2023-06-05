function submitQuestion() {
    const userInput = document.getElementById('user-input').value;
    const chatContainer = document.getElementById('chat-container');

    // Clear input field
    document.getElementById('user-input').value = '';

    // Display user question
    const userQuestion = document.createElement('p');
    userQuestion.innerHTML = `<strong>You:</strong> ${userInput}`;
    chatContainer.appendChild(userQuestion);

    // Make API request to GPT API
    fetch('/api/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            question: userInput,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Display response from GPT API
        const chatbotResponse = document.createElement('p');
        chatbotResponse.innerHTML = `<strong>Chatbot:</strong> ${data.answer}`;
        chatContainer.appendChild(chatbotResponse);
    });
}
