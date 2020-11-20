import blue from '@material-ui/core/colors/blue';
import pink from '@material-ui/core/colors/pink';

const lightTheme = {
  palette: {
    type: 'light',
  },
  overrides: {
    MuiCssBaseline: {
      '@global': {
        '.hljs': {
          background: '#282a36',
        },
        code: {
          backgroundColor: 'gainsboro',
        },
      },
    },
  },
  mixins: {
    container: {
      height: 'calc(100vh - 56px)',
      '@media (min-width:0px) and (orientation: landscape)': {
        height: 'calc(100vh - 48px)',
      },
      '@media (min-width:600px)': { height: 'calc(100vh - 64px)' },
    },
  },
};

const darkTheme = {
  palette: {
    type: 'dark',
    primary: {
      main: blue[500],
    },
    secondary: {
      main: pink.A200,
    },
  },
  overrides: {
    MuiCssBaseline: {
      '@global': {
        '.hljs': {
          background: '#282a36',
        },
        code: {
          backgroundColor: '#282a36',
        },
      },
    },
  },
  mixins: {
    container: {
      height: 'calc(100vh - 56px)',
      '@media (min-width:0px) and (orientation: landscape)': {
        height: 'calc(100vh - 48px)',
      },
      '@media (min-width:600px)': { height: 'calc(100vh - 64px)' },
    },
  },
};

export const getMuiThemeConfig = (prefersDarkMode) => {
  return prefersDarkMode ? darkTheme : lightTheme;
};
