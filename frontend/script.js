function appendMessage(msg, className) {
    const box = document.getElementById('chat-box');
    const msgDiv = document.createElement('div');
    msgDiv.className = className;
  
    if (className === 'bot-msg') {
      const typingSpan = document.createElement('span');
      typingSpan.classList.add('typing-text');
      msgDiv.appendChild(typingSpan);
      box.appendChild(msgDiv);
      box.scrollTop = box.scrollHeight;
  
      // simulate typing
      simulateTypingEffect(msg, typingSpan);
    } else {
      msgDiv.textContent = msg;
      box.appendChild(msgDiv);
      box.scrollTop = box.scrollHeight;
    }
  }
  
  function simulateTypingEffect(message, targetElement) {
    let index = 0;
    targetElement.innerHTML = '';
    const interval = setInterval(() => {
      if (index < message.length) {
        targetElement.innerHTML += message.charAt(index);
        index++;
      } else {
        clearInterval(interval);
      }
    }, 30);
  }
  
  async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (!message) return;
  
    appendMessage(message, 'user-msg');
  
    const response = await fetch(`http://127.0.0.1:5000/search?q=${encodeURIComponent(message)}`);
    const data = await response.json();
  
    if (data.length === 0) {
      appendMessage("😔 No matching products found.", 'bot-msg');
    } else {
      data.forEach(product => {
        appendMessage(`🛒 <b>${product.name}</b><br>₹${product.price}<br><i>${product.description}</i>`, 'bot-msg');
      });
    }
  
    input.value = "";
  }
  
  // Theme toggle
  document.getElementById('themeToggle').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    document.body.classList.toggle('light-mode');
  
    const themeBtn = document.getElementById('themeToggle');
    themeBtn.textContent = document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
  });
  