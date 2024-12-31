import os

# Структура проекта
project_structure = {
    "diploma-frontend": {
        "public": {},
        "src": {
            "components": {
                "AddDiploma.js": """import React, { useState } from 'react';

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
""",
                "GetDiploma.js": """import React, { useState } from 'react';

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
""",
                "AuthorizeUniversity.js": """import React, { useState } from 'react';

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
"""
            },
            "App.js": """import React from 'react';
import AddDiploma from './components/AddDiploma';
import GetDiploma from './components/GetDiploma';
import AuthorizeUniversity from './components/AuthorizeUniversity';

function App() {
  return (
    <div>
      <h1>Diploma Registry</h1>
      <AddDiploma />
      <GetDiploma />
      <AuthorizeUniversity />
    </div>
  );
}

export default App;
""",
            "index.js": """import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
"""
        }
    }
}

def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

if __name__ == "__main__":
    base_dir = os.getcwd()
    create_project_structure(base_dir, project_structure)
    print("Project structure created!")
