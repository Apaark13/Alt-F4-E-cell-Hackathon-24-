import React from 'react';
import './assignment.scss';

const Assignment = () => {
  return (
    <div className='assignment'>
      <div className='heading'>
        <h1>Heading</h1>
      </div> 
      <div className='a1'>
        <h3>Assignment 1</h3>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Id iure recusandae rerum voluptates dolorum, laborum harum fugiat magni fugit facere voluptatum non obcaecati tempore tenetur consequatur earum? Magni placeat illo ullam eveniet dignissimos deleniti maiores sapiente natus eum odit fugiat doloribus repellendus, incidunt qui autem. Aspernatur sit laudantium numquam unde.
        </p>
      </div>
      <div className='labeldiv'>
      <label htmlFor="inputField" className='label'>Upload</label>
      <input type="file" id="inputField" style={{ display: 'none' }} />
      </div>
    </div>
  );
};

export default Assignment;