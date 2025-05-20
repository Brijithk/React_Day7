import React from "react";
import "../css/CardGrid.css";

type Props = {
  cards: string[];
  state: any;
  dispatch: React.Dispatch<any>;
  cardsLeft: number;
};

const CardGrid: React.FC<Props> = ({ cards, state, dispatch, cardsLeft }) => {
  const handleCardClick = (index: number) => {
    if (
      state.selectedCards.includes(index) ||
      state.matchedCards.includes(index)
    )
      return;

    dispatch({ type: "CARD_CLICKED", index });

    const newSelected = [...state.selectedCards, index];
    if (newSelected.length === 2) {
      const [firstIndex, secondIndex] = newSelected;

      if (cards[firstIndex] === cards[secondIndex]) {
        setTimeout(() => {
          dispatch({ type: "ADD_MATCHED" });
        }, 500);
      } else {
        setTimeout(() => {
          dispatch({ type: "RESET_SELECTION" });
        }, 500);
      }
    }
  };

  const isGameComplete = state.matchedCards.length === cards.length;

  return (
    <>
      <div className="card-grid">
        {cards.map((card, index) => {
          const isSelected = state.selectedCards.includes(index);
          const isMatched = state.matchedCards.includes(index);

          return (
            <div
              key={index}
              className={`card ${isSelected ? "selected" : ""} ${
                isMatched ? "matched" : ""
              }`}
              onClick={() => handleCardClick(index)}
            >
              {isSelected || isMatched ? card : "?"}
            </div>
          );
        })}
      </div>

     {cardsLeft === 1 && (
  <div className="congrats-overlay">
    🎉 Congratulations! You matched all the cards! 🎉
  </div>
)}
    </>
  );
};

export default CardGrid;
