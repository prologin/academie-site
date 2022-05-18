import React, { useEffect } from "react";
import "./App.css";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
  useLocation,
  Navigate,
} from "react-router-dom";

import { CssBaseline, ThemeProvider, createTheme } from "@mui/material";

import Navigation from "./components/Navigation";
import StateProvider from "./config/store";
import themeConfig from "./config/theming";
import Connection from "./views/Connection";
import Courses from "./views/Courses";
import Exercises from "./views/Exercises";
import Code from "./views/Code";

const AppRouter = () => {
  const navigate = useNavigate();
  const { pathname } = useLocation();

  useEffect(() => {
    if (pathname.slice(-1) !== "/") navigate(`${pathname}/`, {replace: true});
  });

  return (
    <>
      <CssBaseline />
      <Routes>
        <Route
          path="/"
          element={
            <Navigation>
              <Connection />
            </Navigation>
          }
        />
        <Route
          path="/courses"
          element={
            <Navigation>
              <Courses />
            </Navigation>
          }
        />
        <Route
          path="/exercises"
          element={
            <Navigation>
              <Exercises />
            </Navigation>
          }
        />
        <Route
          path="/code"
          element={
            <Navigation fullScreen>
              <Code />
            </Navigation>
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
