import React from 'react';
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
