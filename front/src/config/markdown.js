import Typography from '@material-ui/core/Typography';

export const markdownOptions = {
  overrides: {
    h1: {
      component: Typography,
      props: {
        gutterBottom: true,
        variant: 'h3',
      },
    },
    h2: {
      component: Typography,
      props: { gutterBottom: true, variant: 'h4' },
    },
    h3: {
      component: Typography,
      props: { gutterBottom: true, variant: 'h5', component: 'h5' },
    },
    h4: {
      component: Typography,
      props: { gutterBottom: true, variant: 'h6', paragraph: true },
    },
    a: {
      props: { rel: 'nofollow' },
    },
    p: { component: Typography, props: { paragraph: true } },
    img: { props: { style: { maxWidth: '100%' } } },
    strong: {
      component: Typography,
      props: {
        component: 'strong',
        style: {
          fontWeight: 500,
        },
      },
    },
  },
};
