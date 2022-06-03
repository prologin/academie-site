import React from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import { makeStyles } from "@mui/styles";

import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import MuiLink from "@mui/material/Link";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    height: "100vh",
  },
  title: {
    flexGrow: 1,
    fontFamily: "Noto Sans",
  },
  logo: {
    color: "inherit",
    textDecoration: "inherit",
    display: "flex",
    alignItems: "center",
    marginRight: 60,
    "& img": {
      maxHeight: 46,
      marginRight: theme.spacing(2),
    },
  },
  appBar: {
    backgroundColor: "#FFF",
  },
  toolbar1: {
    maxWidth: 1000,
    width: "100%",
    margin: "auto",
    color: "#000",
  },
  toolbar: theme.mixins.toolbar,
  container: {
    ...theme.mixins.container,
    maxWidth: 1200,
    margin: "auto",
    padding: 30,
  },
  grow: {
    flexGrow: 1,
  },
  menu: {
    justifyContent: "center",
    alignItems: "center",
    display: "inline-flex",
  },
}));

function Navigation({ children, fullScreen }) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar
        position="fixed"
        elevation={2}
        className={classes.appBar}
        color="whiteBg"
        sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}
      >
        <Toolbar className={classes.toolbar1}>
          <Grid container alignItems="center" className={classes.spaceAround}>
            <Grid item md={2}>
              <Link to="/" className={classes.logo}>
                <img src="/images/logo_cube.png" alt="logo" />
              </Link>
            </Grid>
            <Grid item md={8} className={classes.menu}>
              <Link to="/courses/">
                <Button variant="text" color="black">
                  Voir les cours
                </Button>
              </Link>
              <MuiLink underline="none" href="https://prologin.org">
                <Button variant="text" color="black">
                  Concours
                </Button>
              </MuiLink>
              <MuiLink underline="none" href="https://linktr.ee/prologin">
                <Button variant="text" color="black">
                  Communauté
                </Button>
              </MuiLink>
            </Grid>
            <Grid container item md={2} className={classes.menu}>
              <Link to="/">
                <Button variant="text" color="black">
                  <b>Se connecter</b>
                </Button>
              </Link>
            </Grid>
          </Grid>
        </Toolbar>
      </AppBar>
      <div className={classes.toolbar} />
      {fullScreen ? (
        <>{children}</>
      ) : (
        <div className={classes.container}>{children}</div>
      )}
    </div>
  );
}

Navigation.propTypes = {
  children: PropTypes.node,
};

export default Navigation;
