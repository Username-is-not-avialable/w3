import React, { useState } from 'react';

const GetDiploma = () => {
  const [diplomaId, setDiplomaId] = useState('');
  const [diploma, setDiploma] = useState(null);

  const fetchDiploma = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/getDiploma/${diplomaId}`);
      const result = await response.json();
      if (result.error) throw new Error(result.error);
      setDiploma(result);
    } catch (error) {
      alert('Error: ' + error.message);
    }
  };

  return (
    <div>
      <h2>Get Diploma</h2>
      <input placeholder="Diploma ID" onChange={(e) => setDiplomaId(e.target.value)} />
      <button onClick={fetchDiploma}>Fetch Diploma</button>
      {diploma && (
        <div>
          <p>Owner Name: {diploma.ownerName}</p>
          <p>University: {diploma.university}</p>
          <p>Degree: {diploma.degree}</p>
          <p>Date: {diploma.date}</p>
        </div>
      )}
    </div>
  );
};

export default GetDiploma;
