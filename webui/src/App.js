import React, { useState } from 'react';
import './index.css';

function App() {
  const [messages, setMessages] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const input = event.target.elements.message.value.trim();
  
    if (input === "/clear") {
      setMessages([]);
    } else {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      };
      const responseData = await fetch('http://localhost:5005/webhooks/rest/webhook', requestOptions);
      const chatbotResponse = await responseData.json();
      const responseText = chatbotResponse[0].text || "I don't understand. Please try again.";
      setMessages([...messages, `[User]: ${input}`, `[Bot]: ${responseText}`]);
    }
    event.target.elements.message.value = '';
  };
  
  return (
    <div className="App">
      <header class="App-header">
        <section class="logo">
          <img src='logo.png' alt="logo"></img>
          <h1>Ram Bot</h1>
        </section>
        <div class="chatbot-container">
          <div class="chatbot-messages">
            {messages.map((message, index) => (
              <div class="message" key={index}>
                {message}
              </div>
            ))}
          </div>
          <form class="form" onSubmit={handleSubmit}>
            <input class="text" type="text" name="message" placeholder="Enter your question about a WCU class or Professor. Enter &quot;/clear&quot; to clear the chat."></input>
            <input type="submit" class="submit" value="Send" hidden></input>
          </form>
        </div>
      </header>
    </div> 
  );
}

export default App;
