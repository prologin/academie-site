import React, { useState, useEffect, useRef } from 'react';
import { useParams } from 'react-router-dom';
import { Button, Container, makeStyles } from '@material-ui/core';

import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import Markdown from 'markdown-to-jsx';
import AceEditor from 'react-ace';
import { markdownOptions } from '../config/markdown';

import 'ace-builds/src-noconflict/mode-python';
import 'ace-builds/src-noconflict/snippets/python';
import 'ace-builds/src-noconflict/theme-dracula';

import TrackApi from '../api/trackApi';
import SubmissionButton from './SubmissionButton';
import SubmissionApi from '../api/submissionApi';
import SubmissionStatus from './SubmissionStatus';

const useStyles = makeStyles((theme) => ({
  root: {
    padding: 16,
  },
  editorHeader: {
    padding: 5,
  },
  submission: {},
}));

const newSubmission = (trackId, problemId) => ({
  track: trackId,
  problem_id: problemId,
  code: '',
});

const Problem = (props) => {
  const mounted = useRef(false);
  const classes = useStyles();
  const { trackId, problemId } = useParams();
  const [problem, setProblem] = useState(null);
  const [submission, setSubmission] = useState(
    newSubmission(trackId, problemId),
  );
  const [loader, setLoader] = useState(false);

  const onChange = (newValue) => {
    setSubmission({ ...submission, code: newValue });
  };

  const onSave = async (throwError = false) => {
    try {
      setLoader(true);
      const newSubmission = submission.id
        ? await SubmissionApi.updateSubmission(submission)
        : await SubmissionApi.newSubmission(submission);
      setSubmission(newSubmission);
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
      const startDate = Date.now();
      const newSubmission = await onSave(true);
      await SubmissionApi.runSubmission(newSubmission.id);
      let i = 0;
      const interval = setInterval(async () => {
        i++;
        try {
          const data = await SubmissionApi.getSubmission(newSubmission.id);
          if (
            (data.correction_date &&
              new Date(data.correction_date).getTime() > startDate) ||
            i > 60 // timeout after 60secs
          ) {
            setSubmission(data);
            setLoader(false);
            clearInterval(interval);
          }
        } catch {
          clearInterval(interval);
          setLoader(false);
        }
      }, 1000);
    } catch {
      console.log("Couldn't submit your code");
      setLoader(false);
    }
  };

  useEffect(() => {
    const onComponentMount = async () => {
      const data = await TrackApi.getProblem(trackId, problemId);
      setProblem(data);
      if (data && data.submission) {
        const submissionData = await SubmissionApi.getSubmission(
          data.submission,
        );
        setSubmission(submissionData);
      }
      mounted.current = true;
    };
    if (!mounted.current) onComponentMount();
  });

  return (
    <div className={classes.root}>
      <Grid container spacing={2}>
        <Grid item sm={12} md={6}>
          <Markdown options={markdownOptions}>
            {problem ? problem.subject : 'Not found.'}
          </Markdown>
        </Grid>
        <Grid item xs={12} md={6}>
          <Card variant="outlined">
            <Container maxWidth={false}>
              <Grid
                container
                justify="space-between"
                alignItems="center"
                className={classes.editorHeader}
              >
                <Grid item>
                  <Button>test</Button>
                </Grid>
                <Grid item>
                  <Grid
                    container
                    alignItems="center"
                    spacing={1}
                    className={classes.submission}
                  >
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
              theme="dracula"
              width="100%"
              onChange={onChange}
              fontSize={14}
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
