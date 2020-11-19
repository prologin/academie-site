import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    height: '100vh',
  },
  title: {
    flexGrow: 1,
  },
  logo: {
    color: 'inherit',
    textDecoration: 'inherit',
    display: 'inherit',
    alignItems: 'inherit',
    marginRight: 60,
    '& img': {
      maxHeight: 46,
      marginRight: 10,
    },
  },
  toolbar: theme.mixins.toolbar,
  container: theme.mixins.container,
}));

function Navigation({ children }) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="fixed" elevation={2}>
        <Toolbar>
          <Link to="/" className={classes.logo}>
            <img src="/images/logo_cube.png" alt="logo" />
            <Typography variant="h6" className={classes.title}>
              Academie Prologin
            </Typography>
          </Link>
        </Toolbar>
      </AppBar>
      <div className={classes.toolbar} />
      <div className={classes.container}>{children}</div>
    </div>
  );
}

Navigation.propTypes = {
  children: PropTypes.node,
};

export default Navigation;
