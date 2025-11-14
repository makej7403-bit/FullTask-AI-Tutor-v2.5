import React, { useState } from 'react';
function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  async function submit() {
    const res = await fetch('/api/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: 'demo', prompt, subject: 'math' })
    });
    const data = await res.json();
    setResponse(data.answer);
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>FullTask AI Tutor 6.5</h1>
      <textarea rows={6} cols={60} value={prompt} onChange={e => setPrompt(e.target.value)} />
      <br/>
      <button onClick={submit}>Ask</button>
      <h3>Response</h3>
      <div style={{ whiteSpace: 'pre-wrap' }}>{response}</div>
    </div>
  );
}
export default App;
