import React from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import { createMuiTheme, CssBaseline, ThemeProvider } from '@material-ui/core';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import SocialNetworks from './components/SocialNetworks';
import Navigation from './components/Navigation';
import Tracks from './components/Tracks';
import Track from './components/Track';
import Problem from './components/Problem';

function ComingSoon() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="/images/logo_cube.png" className="App-logo" alt="logo" />
        <h1>Coming soon !</h1>
        <p>
          Le lancement de ce site sera annoncé sur nos réseaux, alors si vous
          <br />
          souhaitez apprendre la programmation, suivez nous sur nos réseaux !
        </p>
        <SocialNetworks />
      </header>
    </div>
  );
}

function App() {
  // Get user's device theme mode (light/dark)
  const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');

  const theme = React.useMemo(
    () =>
      createMuiTheme({
        palette: {
          type: prefersDarkMode ? 'dark' : 'light',
        },
      }),
    [prefersDarkMode],
  );

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline/>
      <Router>
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
          <Route path="/track/:trackId/problem/:problemId">
            <Navigation>
              <Problem />
            </Navigation>
          </Route>
          <Route path="*">
            <ComingSoon />
          </Route>
        </Switch>
      </Router>
    </ThemeProvider>
  );
}

export default App;
