import React, { useState } from 'react';
// import SummaryDisplay from './Components/summary_display';
const App = () => {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState('');

  const ShareButton = ({ summary }) => {
    const handleShareClick = () => {
      // Construct the WhatsApp message
      const whatsappMessage = encodeURIComponent(summary);
  
      // Open WhatsApp with the message
      // window.open(`https://wa.me/?text=${whatsappMessage}`);
      // const whatsappMessage = encodeURIComponent(summary);

  // Open WhatsApp application with the message
      window.location.href = `whatsapp://send?text=${whatsappMessage}`;
    };
  
    return (
      <div>
        <button onClick={handleShareClick}>Share via WhatsApp</button>
      </div>
    );
  };
  const handleFileChange = (e) => {
    console.log(e.target.files[0]);
    setFile(e.target.files[0]);
  };
  const SummaryDisplay = ({ summary }) => {
    return (
      <div>
        <p>{summary}</p>
      </div>
    );
  };
  const handleSummarize = async () => {
    try {
      console.log(typeof(file));
      console.log(file);
      const formData = new FormData();
      formData.append('file', file);
      // formData.append('file2', "hari");
      console.log(file);
  
      const response = await fetch('http://127.0.0.1:5000/summarize', {
        method: 'POST',
        body: file,
      });
  
      if (!response.ok) {
        const errorData = await response.json();
        console.error('Error summarizing PDF:', errorData.error);
        throw new Error('Failed to summarize PDF');
      }
  
      const result = await response.json();
      setSummary(result.summary);
      console.log('Summary:', result.summary);
    } catch (error) {
      console.error('Error handling summarize request:', error);
    }
  };
  

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSummarize}>Summarize PDF</button>
      {summary && <div>
      <h1>Summary</h1>
      <SummaryDisplay summary={summary} />
      <ShareButton summary={summary} />
    </div>}
    </div>
  );
};

export default App;