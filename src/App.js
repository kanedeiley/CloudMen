import React, { useState } from 'react';
import './index.css';

function App() {
  const [messages, setMessages] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    const input = event.target.elements.message.value;
    setMessages([...messages, input]);
    event.target.elements.message.value = '';
  };
  return (
    <div className="App">
      <header class="App-header">
      <div class="chatbot-container">
          <div class="chatbot-messages">
            {messages.map((message, index) => (
              <div class="message" key={index}>
                {message}
              </div>
            ))}
          </div>
        <form class="form" onSubmit={handleSubmit}>
        <input class="text" type="text" name="message"></input>
        <input type="submit" class="submit" value="Send"></input>
        </form>
        </div>
      </header>
    </div>
  );
}

export default App;
