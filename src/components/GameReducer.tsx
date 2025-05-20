type State = {
  selectedCards: number[];
  matchedCards: number[];
  points: number;
};

type Action = {
  type: string;
  index?: number;
};

export const initialState: State = {
  selectedCards: [],
  matchedCards: [],
  points: 0,
};

export function gameReducer(state: State, action: Action): State {
  switch (action.type) {
    case "CARD_CLICKED": {
      if (state.selectedCards.length === 2) return state;
      return { ...state, selectedCards: [...state.selectedCards, action.index!] };
    }

    case "ADD_MATCHED":
      return {
        ...state,
        matchedCards: [...state.matchedCards, ...(state.selectedCards)],
        points: state.points + 10,
        selectedCards: [],
      };

    case "RESET_SELECTION":
      return { ...state, selectedCards: [] };

    default:
      return state;
  }
}
