import React, { useState, useEffect, useRef } from 'react';
import { useParams } from 'react-router-dom';
import { makeStyles } from '@material-ui/core';
import { useTheme } from '@material-ui/core/styles';

import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import Container from '@material-ui/core/Container';
import AceEditor from 'react-ace';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFont, faPaintBrush } from '@fortawesome/free-solid-svg-icons';

import SubmissionButton from './SubmissionButton';
import SubmissionStatus from './SubmissionStatus';
import Dropdown from './Dropdown';
import HighlightedMarkdown from './Markdown';
import submissionApi from '../api/submissionApi';

import {
  changeSubmission,
  useDispatch,
  useSelector,
  fetchSubmissionUntilCorrectionEnds,
  fetchProblem,
} from '../config/store';

import 'ace-builds/src-noconflict/mode-python';
import 'ace-builds/src-noconflict/snippets/python';
import { usePrevious } from '../utils/utils';

const themes = [
  'dracula',
  'monokai',
  'github',
  'tomorrow',
  'kuroir',
  'twilight',
  'xcode',
  'textmate',
  'solarized_dark',
  'solarized_light',
  'terminal',
];

themes.forEach((theme) => require(`ace-builds/src-noconflict/theme-${theme}`));

const sizes = [12, 14, 16, 18, 20, 24, 30];

const useStyles = makeStyles((theme) => ({
  root: {
    height: '100%',
    overflow: 'auto',
  },
  container: {
    height: 'inherit',
  },
  subject: {
    overflowY: 'auto',
    maxHeight: '100%',
    padding: theme.spacing(4),
  },
  editor: {
    height: '100%',
  },
  editorHeader: {
    padding: 5,
  },
  textIcon: {
    marginRight: theme.spacing(1),
  },
  optionDropdown: {
    marginRight: 5,
  },
}));

const newSubmission = (trackId, problemId) => ({
  track: trackId,
  problem_id: problemId,
  code: '',
});

const Problem = () => {
  const mounted = useRef(false);
  const theme = useTheme();
  const classes = useStyles();
  const { trackId, problemId } = useParams();
  const dispatch = useDispatch();

  const [editorTheme, setEditorTheme] = useState(
    theme.palette.type === 'dark' ? 'dracula' : 'xcode',
  );
  const [fontSize, setFontSize] = useState(20);
  const [loader, setLoader] = useState(false);
  const { problem, submission } = useSelector((state) => {
    const prob = state.problems.find((p) => p.problem_id === problemId);
    let sub;
    if (prob && prob.submission) sub = prob.submission;
    else if (prob)
      sub = { ...newSubmission(trackId, problemId), code: prob.scaffold };
    else sub = newSubmission(trackId, problemId);
    return { problem: prob, submission: sub };
  });
  const prevSubmission = usePrevious(submission);

  const onChange = (newValue) => {
    dispatch(changeSubmission({ ...submission, code: newValue }));
  };

  const onSave = async (throwError = false) => {
    try {
      setLoader(true);
      const newSubmission = submission.id
        ? await submissionApi.updateSubmission(submission)
        : await submissionApi.newSubmission(submission);
      dispatch(changeSubmission(newSubmission));
      if (!throwError) setLoader(false);
      return newSubmission;
    } catch {
      console.log("Couldn't submit your code");
      setLoader(false);
      if (throwError) throw new Error();
    }
  };

  const onSubmit = async () => {
    try {
      setLoader(true);
      const newSubmission = await onSave(true);
      await submissionApi.runSubmission(newSubmission.id);
      dispatch(fetchSubmissionUntilCorrectionEnds(newSubmission.id));
    } catch {
      console.log("Couldn't submit your code");
      setLoader(false);
    }
  };

  useEffect(() => {
    const onComponentMount = () => {
      dispatch(fetchProblem(trackId, problemId));
      mounted.current = true;
    };
    if (!mounted.current) onComponentMount();
  });

  useEffect(() => {
    if (
      prevSubmission &&
      submission &&
      prevSubmission.correction_date !== submission.correction_date
    )
      setLoader(false);
  }, [prevSubmission, submission]);

  return (
    <div className={classes.root}>
      <Grid container className={classes.container}>
        <Grid item sm={12} md={6} className={classes.subject}>
          <HighlightedMarkdown>
            {(problem && problem.subject) || 'Not found.'}
          </HighlightedMarkdown>
        </Grid>
        <Grid item xs={12} md={6} className={classes.container}>
          <Card square className={classes.editor}>
            <Container maxWidth={false}>
              <Grid
                container
                justify="space-between"
                alignItems="center"
                className={classes.editorHeader}
              >
                <Grid item>
                  <Dropdown
                    title={
                      <>
                        <FontAwesomeIcon
                          icon={faPaintBrush}
                          className={classes.textIcon}
                        />
                        {editorTheme}
                      </>
                    }
                    items={themes.map((t) => ({
                      content: t,
                      onClick: () => setEditorTheme(t),
                    }))}
                    variant="contained"
                    buttonProps={{ className: classes.optionDropdown }}
                  />
                  <Dropdown
                    title={
                      <>
                        <FontAwesomeIcon
                          icon={faFont}
                          className={classes.textIcon}
                        />
                        {fontSize}px
                      </>
                    }
                    items={sizes.map((t) => ({
                      content: t,
                      onClick: () => setFontSize(t),
                    }))}
                    variant="contained"
                    buttonProps={{ className: classes.optionDropdown }}
                  />
                </Grid>
                <Grid item>
                  <Grid container alignItems="center" spacing={1}>
                    <Grid item>
                      <SubmissionStatus loader={loader} {...submission} />
                    </Grid>
                    <Grid>
                      <SubmissionButton onSubmit={onSubmit} onSave={onSave} />
                    </Grid>
                  </Grid>
                </Grid>
              </Grid>
            </Container>
            <AceEditor
              mode="python"
              theme={editorTheme}
              width="100%"
              height="calc(100% - 46px)"
              onChange={onChange}
              fontSize={fontSize}
              showPrintMargin={true}
              showGutter={true}
              highlightActiveLine={true}
              value={submission.code}
              setOptions={{
                showLineNumbers: true,
                tabSize: 4,
              }}
            />
          </Card>
        </Grid>
      </Grid>
    </div>
  );
};

export default Problem;
