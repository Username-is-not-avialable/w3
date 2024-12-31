import React, { useState } from 'react';

const AuthorizeUniversity = () => {
  const [address, setAddress] = useState('');

  const handleAuthorize = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/authorizeUniversity', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ universityAddress: address })
      });
      const result = await response.json();
      alert(result.message || result.error);
    } catch (error) {
      alert('Error: ' + error.message);
    }
  };

  return (
    <div>
      <h2>Authorize University</h2>
      <input placeholder="University Address" onChange={(e) => setAddress(e.target.value)} />
      <button onClick={handleAuthorize}>Authorize</button>
    </div>
  );
};

export default AuthorizeUniversity;
