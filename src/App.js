import React, { useState } from 'react';
import './index.css';
import response from './response.json';

function App() {
  const [messages, setMessages] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    const input = event.target.elements.message.value.trim();
  
    if (input === "/clear") {
      setMessages([]);
    } else {
      const chatbotResponse = response[input] || "I don't understand. Please try again.";
      setMessages([...messages, `[User]: ${input}`, `[Bot]: ${chatbotResponse}`]);
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
