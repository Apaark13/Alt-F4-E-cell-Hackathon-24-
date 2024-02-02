import './App.scss';
import React, { useState } from 'react';

function App() {
  const [assignment, setAssignment] = useState({
    assignmentTitle: '',
    assignmentDescription: '',
    dueDate: '',
    file: null,
  });

  const handleChange = (e) => {
    setAssignment({
      ...assignment,
      [e.target.name]: e.target.value,
    });
  };

  const handleFileChange = (e) => {
    setAssignment({
      ...assignment,
      file: e.target.files[0],
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Handle form submission (e.g., send data to server using Fetch)

    try {
      const formData = new FormData();
      formData.append('assignmentTitle', assignment.assignmentTitle);
      formData.append('assignmentDescription', assignment.assignmentDescription);
      formData.append('dueDate', assignment.dueDate);
      formData.append('file', assignment.file);

      await fetch('http://localhost:5000/api/assignments', {
        method: 'POST',
        body: formData,
      });

      // Handle success (e.g., show a success message)
    } catch (error) {
      // Handle error (e.g., show an error message)
    }
  };

  return (
    <div className="App">
      <h1>Online Assignment Submission</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="assignmentTitle">Assignment Title:</label>
        <input
          type="text"
          id="assignmentTitle"
          name="assignmentTitle"
          value={assignment.assignmentTitle}
          onChange={handleChange}
          required
        />

        <label htmlFor="assignmentDescription">Assignment Description:</label>
        <textarea
          id="assignmentDescription"
          name="assignmentDescription"
          value={assignment.assignmentDescription}
          onChange={handleChange}
          rows="4"
          required
        ></textarea>

        <label htmlFor="dueDate">Due Date:</label>
        <input
          type="date"
          id="dueDate"
          name="dueDate"
          value={assignment.dueDate}
          onChange={handleChange}
          required
        />

        <label htmlFor="fileUpload">Upload Assignment File:</label>
        <input
          type="file"
          id="fileUpload"
          name="fileUpload"
          onChange={handleFileChange}
          required
        />

        <button type="submit">Submit Assignment</button>
      </form>
    </div>
  );
}

export default App;
