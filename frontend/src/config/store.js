import { useReducer } from 'react';
import { createContainer } from 'react-tracked';
import { usePrevious } from './utils';
import {combReducer, combState} from './reducers'
import {getProfile} from './reducers/user'

// ============ REACT-TRACKED elements =================
const useMiddleware = (state, dispatch) => {
  const prevState = usePrevious(state);

  console.log(state);
  if (prevState && prevState.user.authenticated !== state.user.authenticated) {
    if (state.user.authenticated) {
      dispatch(getProfile());
    }
  }
};

const useValue = () => {
  const [state, dispatch] = useReducer(combReducer, combState);
  const dispatchWithCallback = (dispatcher) => {
    if (typeof dispatcher === 'function') dispatcher(dispatchWithCallback);
    else dispatch(dispatcher);
  };

  useMiddleware(state, dispatchWithCallback);
  return [state, dispatchWithCallback];
};

const {
  Provider,
  useTracked,
  useSelector,
  useTrackedState,
  useUpdate: useDispatch,
} = createContainer(useValue);

const StateProvider = ({ children }) => <Provider>{children}</Provider>;

export {
  useTracked,
  useDispatch,
  useSelector,
  useTrackedState,
};

export default StateProvider;