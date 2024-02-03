import React from 'react'
import './assignment_mini.scss'
const Assgnment_mini = (props) => {
  console.log('vsfb')
  return (
    <div className="assignment_mini">
      <div className="details">
        <div className="title">
          {props.assignmentTitle}
        </div>
        <div className="description">{props.description}</div>
        <div>
          {props.assignmentDescription}
        </div>
        <div className="valid">
          Due Date: {props.duedate}
        </div>
      </div>
      </div>
  );
};

export default Assgnment_mini
