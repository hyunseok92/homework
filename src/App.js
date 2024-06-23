import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [testok, setTestok] = useState('');
  const [latestItem, setLatestItem] = useState(null);
  const [error, setError] = useState(null);


  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(testok);
    try {
      const res = await axios.post('http://localhost:8000/add/', { testok });
  
    } catch (error) {
      console.error("There was an error adding the item!", error);
    }
  };

  const fetchLatestItem = async () => {
    try {
      const response = await fetch('http://localhost:8000/get/');
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      const data = await response.json();
      setLatestItem(data);
    } catch (error) {
      setError(error.message);
    }
  };

  const handleClick = () => {
    fetchLatestItem();
  }
  return (
    <>
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          문자열 입력:
          <input
            type="text"
            value={testok}
            onChange={(e) => setTestok(e.target.value)}
          />
        </label>
        <button type="submit">등록</button>
      </form>
    </div>
    <button onClick={handleClick}>최근값 반환</button>
    {latestItem && <div>최근 값: {latestItem.testok}</div>}
  </>
      
  );
}

export default App;
