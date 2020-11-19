import React, { useRef, useEffect } from 'react';
import PropTypes from 'prop-types';

import { markdownOptions } from '../config/markdown';
import 'highlight.js/styles/atom-one-dark.css';

import Markdown from 'markdown-to-jsx';
import hljs from 'highlight.js';

function HighlightedMarkdown({ children }) {
  const rootRef = useRef();

  useEffect(() => {
    rootRef.current.querySelectorAll('pre code').forEach((block) => {
      hljs.highlightBlock(block);
    });
  }, [children]);

  return (
    <div ref={rootRef}>
      <Markdown options={markdownOptions}>{children}</Markdown>
    </div>
  );
}

HighlightedMarkdown.propTypes = {
  children: PropTypes.node,
};

export default HighlightedMarkdown;
