import React from "react";
import "../css/Header.css";

type HeaderProps = {
  cardsLeft: number;
  points: number;
};

const Header: React.FC<HeaderProps> = ({ cardsLeft, points }) => {
  return (
    <header className="header">
      <div className="left">
        <h1>Memory Game</h1>
      </div>
      <div className="right">
        <div className="info">Cards Left: {cardsLeft}</div>
        <div className="info">Points: {points}</div>
      </div>
    </header>
  );
};

export default Header;
