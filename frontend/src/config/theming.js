export const themeConfig = {
  components: {
    MuiAppBar: {
      defaultProps: {
        elevation: 0,
      },
    },
    MuiPaper: {
      defaultProps: {
        elevation: 0,
      },
    },
    MuiCard: {
      defaultProps: {
        elevation: 0,
      },
    },
    MuiGrid: {
      defaultProps: {
        xs: 12,
      },
    },
  },
  palette: {
    whiteBg: {
      main: "#FFF",
      contrastText: "#000",
    },
    black: {
      main: "#000",
    },
    background: {
      default: "#f2f3f3",
    },
  },
};

export default themeConfig;
