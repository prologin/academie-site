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

import useMediaQuery from '@material-ui/core/useMediaQuery';
import SocialNetworks from './components/SocialNetworks';
import Navigation from './components/Navigation';
import Tracks from './components/Tracks';
import Track from './components/Track';
import Problem from './components/Problem';
import StateProvider from './config/store';


const AppRouter = () => {
  const history = useHistory();
  const { pathname } = useLocation();

  useEffect(() => {
    if (pathname.substr(-1) !== '/') history.replace(`${pathname}/`);
  });

  return (
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
  );
};

function App() {
  // Get user's device theme mode (light/dark)
  const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');

  const theme = React.useMemo(() => getMuiThemeConfig(prefersDarkMode), [
    prefersDarkMode,
  ]);

  return (
    <StateProvider>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Router>
          <AppRouter />
        </Router>
      </ThemeProvider>
    </StateProvider>
  );
}

export default App;
