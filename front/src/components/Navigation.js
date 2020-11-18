import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import { Link } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
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
    marginLeft: 33,
    '& img': {
      maxHeight: 46,
      marginRight: 10,
    },
  },
  toolbar: theme.mixins.toolbar,
}));

function Navigation({ children }) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="fixed">
        <Toolbar>
          <Link to="/" className={classes.logo}>
            <img src="/images/logo_cube.png" alt="logo" />
            <Typography variant="h6" className={classes.title}>
              Prologin
            </Typography>
          </Link>
        </Toolbar>
      </AppBar>
      <div className={classes.toolbar} />
      {children}
    </div>
  );
}

export default Navigation;
