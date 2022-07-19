import Markdown from 'markdown-to-jsx';

import { Typography, Link } from '@mui/material';

const markdownOptions = {
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
      component: Link,
      props: { rel: 'nofollow' },
    },
    p: { component: Typography, props: { paragraph: true } },
    img: { props: { style: { maxWidth: '100%' } } },
    strong: {
      component: Typography,
      props: {
        variant: 'p',
        style: {
          fontWeight: 500,
        },
      },
    },
    //figure: { component: PostFigure },
  },
};

const MarkdownWrapped = (props) => (
  <Markdown options={markdownOptions} {...props} />
);

export default MarkdownWrapped;
