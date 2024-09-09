import React, { useState } from 'react';
import './App.css';
// import logo from'../public/IBM LOGO.svg'
function App() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState({
      obligation: false,
      frequency: false,
      missingControls: false,
      problemInControl: false,
  });
    const sendMessage1 = async () => {
      setLoading({ ...loading, obligation: true });
      try {
          const response = await fetch('http://127.0.0.1:8000/generateControls', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ message: input }),
          });
          const data = await response.json();
          setMessages([...messages, { user: input, bot: data.response}]);
          setInput('');
      } catch (error) {
          console.error('Error:', error);
      } finally {
          setLoading({ ...loading, obligation: false });
      }
    };

    const sendMessage2=async ()=>{
      setLoading({ ...loading, frequency: true });
      try {
          const response = await fetch('http://127.0.0.1:8000/checkfrequency', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ message: input }),
          });
          const data = await response.json();
          setMessages([...messages, { user: input, bot: data.response }]);
          setInput('');
      } catch (error) {
          console.error('Error:', error);
      } finally {
          setLoading({ ...loading, frequency: false });
      }
    }

    const sendMessage3=async ()=>{
      setLoading({ ...loading, missingControls: true });
      try {
          const response = await fetch('http://127.0.0.1:8000/missingControls', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ message: input }),
          });
          const data = await response.json();
          setMessages([...messages, { user: input, bot: data.response }]);
          setInput('');
      } catch (error) {
          console.error('Error:', error);
      } finally {
          setLoading({ ...loading, missingControls: false });
      }
    }

    const sendMessage4=async ()=>{
      setLoading({ ...loading,problemInControl: true });
      try {
          const response = await fetch('http://127.0.0.1:8000/problemIncontrol', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ message: input }),
          });
          const data = await response.json();
          setMessages([...messages, { user: input, bot: data.response }]);
          setInput('');
      } catch (error) {
          console.error('Error:', error);
      } finally {
          setLoading({ ...loading, problemInControl: false });
      }
    }
    return (
      <div className="chat-app-container">
        <header className="chat-app-header">
            <img src='./IBM_LOGO.svg'></img>
            <h2>REGULUS BANK</h2>
        </header>
        
        <div className="Input_wrapper">
          <div className="chat-input-container">
              <textarea
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  className="chat-input"
                  placeholder="User Input..."
                  rows="1"
                  disabled={loading.obligation || loading.frequency || loading.missingControls || loading.problemInControl}
              />
          </div>
          <div className="Button">
            <button onClick={sendMessage1} className="send-button" disabled={loading.obligation}>{loading.obligation ? 'Loading...' : 'Check obligation'}</button>
            <button onClick={sendMessage2} className="send-button" disabled={loading.frequency}>{loading.frequency?'Loading...':'Check frequency'}</button>
            <button onClick={sendMessage3} className='send-button' disabled={loading.missingControls}>{loading.missingControls ? 'Loading...' : 'Missing Controls'}</button>
            <button onClick={sendMessage4} className='send-button' disabled={loading.problemInControl}>{loading.problemInControl?'Loading...':'Problem in controls'}</button>
          </div>
        </div>
        
        <div className="chat-history">
          {messages.length > 0 && (
              <div className="message-block">
                  <p className="user-message">You: </p>
                  <div className="User-block">
                    
                    <div className='User-input'>{messages[messages.length - 1].user}</div>
                  </div>
                  <p className="bot-message">Assistant: </p>
                  <div class="assitant-block">
                    
                    <div className='assistant-response'>{messages[messages.length - 1].bot}</div>
                  </div>
              </div>
          )}
        </div>

        
      </div>
    );
}

export default App;
