import React, { useState } from 'react';

const AddDiploma = () => {
  const [formData, setFormData] = useState({
    diplomaId: '',
    ownerName: '',
    university: '',
    degree: '',
    date: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:5000/addDiploma', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const result = await response.json();
      alert(result.message || result.error);
    } catch (error) {
      alert('Error: ' + error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Diploma</h2>
      <input name="diplomaId" placeholder="Diploma ID" onChange={handleChange} />
      <input name="ownerName" placeholder="Owner Name" onChange={handleChange} />
      <input name="university" placeholder="University" onChange={handleChange} />
      <input name="degree" placeholder="Degree" onChange={handleChange} />
      <input name="date" placeholder="Date" onChange={handleChange} />
      <button type="submit">Add Diploma</button>
    </form>
  );
};

export default AddDiploma;
