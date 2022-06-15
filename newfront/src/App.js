import React, { useEffect } from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
  useLocation,
  Navigate,
} from 'react-router-dom';

import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';

import Navigation from './components/Navigation';
import themeConfig from './config/theming';
import Login from './views/Login';
import Courses from './views/Courses';
import Exercises from './views/Exercises';
import Code from './views/Code';
import Register from './views/Register';

import StateProvider, { useSelector } from './config/store';

const Protected = ({ children }) => {
  const isAuthenticated = useSelector((state) => state.user.authenticated);
  const navigate = useNavigate();

  useEffect(() => {
    if (!isAuthenticated) navigate(`/`, { replace: true });
  });

  return isAuthenticated ? children : null;
};

const RedirectIfAuthenticated = ({ children }) => {
  const isAuthenticated = useSelector((state) => state.user.authenticated);
  const navigate = useNavigate();

  useEffect(() => {
    if (isAuthenticated) navigate(`/courses/`, { replace: true });
  });

  return !isAuthenticated ? children : null;
};

const AppRouter = () => {
  const navigate = useNavigate();
  const { pathname } = useLocation();

  useEffect(() => {
    if (pathname.slice(-1) !== '/') navigate(`${pathname}/`, { replace: true });
  });

  return (
    <>
      <CssBaseline />
      <Routes>
        <Route
          path="/"
          element={
            <RedirectIfAuthenticated>
              <Navigation>
                <Login />
              </Navigation>
            </RedirectIfAuthenticated>
          }
        />
        <Route
          path="/register"
          element={
            <RedirectIfAuthenticated>
              <Navigation>
                <Register />
              </Navigation>
            </RedirectIfAuthenticated>
          }
        />
        <Route
          path="/courses"
          element={
            <Protected>
              <Navigation>
                <Courses />
              </Navigation>
            </Protected>
          }
        />
        <Route
          path="/exercises"
          element={
            <Protected>
              <Navigation>
                <Exercises />
              </Navigation>
            </Protected>
          }
        />
        <Route
          path="/code"
          element={
            <Protected>
              <Navigation fullScreen>
                <Code />
              </Navigation>
            </Protected>
          }
        />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </>
  );
};

function App() {
  return (
    <StateProvider>
      <ThemeProvider theme={createTheme(themeConfig)}>
        <Router>
          <AppRouter />
        </Router>
      </ThemeProvider>
    </StateProvider>
  );
}

export default App;
