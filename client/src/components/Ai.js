import React, { useState } from 'react';
import openai from 'openai';

openai.api_key = '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';

function Chatbot() {
    const [input, setInput] = useState('');
    const [output, setOutput] = useState('');
  
    const generateResponse = async (input) => {
      const prompt = `User: ${input}\nChatbot:`;
      const response = await openai.complete({
        engine: 'text-davinci-002',
        prompt,
        maxTokens: 1024,
        n: 1,
        stop: '\n',
        temperature: 0.5,
      });
      setOutput(response.choices[0].text);
    };
  
    const handleSubmit = (e) => {
      e.preventDefault();
      generateResponse(input);
    };
  
    return (
      <div>
        <form onSubmit={handleSubmit}>
          <input type='text' value={input} onChange={(e) => setInput(e.target.value)} />
          <button type='submit'>Send</button>
        </form>
        {output && <div>{output}</div>}
      </div>
    );
  }
  
  export default Chatbot;