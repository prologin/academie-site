import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { makeStyles, ThemeProvider } from '@material-ui/core/styles';
import { darkTheme } from '../config/theming';
import { indigo } from '@material-ui/core/colors';

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Tooltip from '@material-ui/core/Tooltip';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import LightIcon from '@material-ui/icons/Brightness7';
import DarkIcon from '@material-ui/icons/Brightness3';

import TrackProgress from './TrackProgress';
import UserMenu from './UserMenu';
import { toggleDarkTheme, useTracked } from '../config/store';

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
    display: 'flex',
    alignItems: 'center',
    marginRight: 60,
    '& img': {
      maxHeight: 46,
      marginRight: theme.spacing(2),
    },
  },
  appBar: {
    backgroundColor: indigo[600],
  },
  toolbar: theme.mixins.toolbar,
  container: theme.mixins.container,
  grow: {
    flexGrow: 1,
  },
  menu: {
    textAlign: 'right',
    justifyContent: "flex-end",
    alignItems: "center"
  },
  progress: {
    textAlign: 'center',
  },
}));

function Navigation({ children, problemProgress }) {
  const classes = useStyles();
  const [state, dispatch] = useTracked();
  const { darkTheme: prefersDarkTheme } = state;

  const handleClickTheme = () => {
    dispatch(toggleDarkTheme);
  };

  return (
    <div className={classes.root}>
      <ThemeProvider theme={darkTheme}>
        <AppBar position="fixed" elevation={2} className={classes.appBar}>
          <Toolbar>
            <Grid container justify="space-between" alignItems="center">
              <Grid item md={4}>
                <Link to="/" className={classes.logo}>
                  <img src="/images/logo_cube.png" alt="logo" />
                  <Typography variant="h6" className={classes.title}>
                    Academie Prologin
                  </Typography>
                </Link>
              </Grid>
              {problemProgress && (
                <Grid item md={4} className={classes.progress}>
                  <TrackProgress />
                </Grid>
              )}
              <Grid container item md={4} className={classes.menu}>
                <Grid item>
                  <Link to="/tracks">
                    <Button>Cursus</Button>
                  </Link>
                </Grid>
                <Grid item>
                  <IconButton onClick={handleClickTheme}>
                    {prefersDarkTheme ? (
                      <Tooltip title="Turn off dark theme">
                        <LightIcon />
                      </Tooltip>
                    ) : (
                      <Tooltip title="Turn on dark theme">
                        <DarkIcon />
                      </Tooltip>
                    )}
                  </IconButton>
                </Grid>
                <Grid item>
                  <UserMenu />
                </Grid>
              </Grid>
            </Grid>
          </Toolbar>
        </AppBar>
      </ThemeProvider>
      <div className={classes.toolbar} />
      <div className={classes.container}>{children}</div>
    </div>
  );
}

Navigation.propTypes = {
  children: PropTypes.node,
};

export default Navigation;
