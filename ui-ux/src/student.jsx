import React from "react";
import Assgnment_mini from "./assgnment_mini";
import "./student.scss"
const assignmentData = [
  {
    assignmentTitle: "Math Homework",
    duedate:"26-04-2024",
    assignmentDescription: "Complete exercises 1-10 in the algebra textbook. Focus on solving equations and simplifying expressions."
  },
  {
    assignmentTitle: "History Essay",
    duedate:"26-04-2024",
    assignmentDescription: "Write a 3-page essay on the causes and effects of World War II. Include key events, leaders, and their impact on the world."
  },
  {
    assignmentTitle: "Science Experiment",
    duedate:"26-04-2024",
    assignmentDescription: "Conduct a simple experiment to demonstrate the principles of photosynthesis. Record observations and analyze the results in a lab report."
  }
];

const Student = () => {

  const assign = assignmentData.map((item) => {
    const handleClick = () => {
        console.log(item);
    };
    return <Assgnment_mini  {...item} onClick={handleClick} />;
  });
  return (
    <div className="user">
      <div className="user-profile">
        <div className="pic">
          <img src="/assets/user.png" alt="" />
        </div>
        <div className="details">
          <h3>Dummy User</h3>
          <div>
            <ul>
              <li>
                <span>4</span>Sent
              </li>
              <li>
                <span>12</span>Received
              </li>
              <li>
                <span>23</span>Coupons
              </li>
            </ul>
          </div>
          <section>
            bio - Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Inventore dolores distinctio deserunt enim eaque aperiam quo
            cupiditate aliquam! Vero possimus deserunt adipisci earum saepe
            enim!
          </section>
        </div>
      </div>
      <hr />

      <div className="user-coupons">
      {assign}  
      </div>
    </div>
  );
};

export default Student;
