import React, { useEffect } from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useHistory,
  useLocation,
} from 'react-router-dom';

import { CssBaseline, ThemeProvider } from '@material-ui/core';
import { getMuiThemeConfig } from './config/theming';

import Navigation from './components/Navigation';
import Tracks from './components/Tracks';
import Track from './components/Track';
import Problem from './components/Problem';
import StateProvider, { useTrackedState } from './config/store';

const AppRouter = () => {
  const history = useHistory();
  const { pathname } = useLocation();
  const { darkTheme } = useTrackedState();

  useEffect(() => {
    if (pathname.substr(-1) !== '/') history.replace(`${pathname}/`);
  });

  return (
    <ThemeProvider theme={getMuiThemeConfig(darkTheme)}>
      <CssBaseline />
      <Switch>
        <Route path="/tracks">
          <Navigation>
            <Tracks />
          </Navigation>
        </Route>
        <Route exact path="/track/:trackId">
          <Navigation>
            <Track />
          </Navigation>
        </Route>
        <Route exact path="/track/:trackId/problem/:problemId">
          <Navigation problemProgress>
            <Problem />
          </Navigation>
        </Route>
        <Route path="*">
          <Tracks />
        </Route>
      </Switch>
    </ThemeProvider>
  );
};

function App() {
  return (
    <StateProvider>
      <Router>
        <AppRouter />
      </Router>
    </StateProvider>
  );
}

export default App;
