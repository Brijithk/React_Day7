import React, { useReducer } from 'react';
import './App.css';
import Header from './components/Header';
import CardGrid from './components/CardGrid';
import cardsData from './components/CardData';
import { gameReducer,initialState } from './components/GameReducer';
import { useMemo } from 'react';

function App() {
  const [cards] = React.useState<string[]>(cardsData);
  const [state, dispatch] = useReducer(gameReducer, initialState);

  const cardsLeft = useMemo(() => {
    return cards.length - state.matchedCards.length-1;
  }, [cards.length, state.matchedCards.length]);
    
  return (
    <>
        <Header cardsLeft={cardsLeft} points={state.points} />
 <CardGrid
  cards={cards}
  state={state}
  dispatch={dispatch}
  cardsLeft={cards.length - state.matchedCards.length}
/>
    </>
  );
}

export default App;
