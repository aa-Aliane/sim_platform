import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHouse } from "@fortawesome/free-solid-svg-icons";

const Nav = () => {
  return (
    <nav className="nav">
      <div className="nav__about">About</div>
      <div>Plagiarism detection in ASJP articles</div>
      <div className="nav__home">
        <FontAwesomeIcon className="fs-xl" icon={faHouse} />
        <p>Home</p>
      </div>
    </nav>
  );
};

export default Nav;
