import React, { useState, useEffect, useRef } from 'react';
import { Link, useParams } from 'react-router-dom';
import { makeStyles } from '@material-ui/core';

import Container from '@material-ui/core/Container';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepButton from '@material-ui/core/StepButton';
import StepContent from '@material-ui/core/StepContent';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';

import { Typography } from '@material-ui/core';
import SubmissionStatus from './SubmissionStatus';
import {
  fetchProblems,
  fetchTrack,
  useDispatch,
  useSelector,
} from '../config/store';

const useStyles = makeStyles((theme) => ({
  root: {
    padding: 16,
  },
  title: {
    marginBottom: theme.spacing(1),
  },
  problemButton: {
    width: '100%',
    maxWidth: 270,
    alignSelf: 'center',
    marginTop: theme.spacing(2),
  },
  flex: {
    display: 'flex',
  },
}));

const ProblemNode = ({
  problem_id,
  properties,
  submission,
  expanded,
  ...props
}) => {
  const { name, description } = properties;
  const classes = useStyles();
  const [forceExpanded, setExpanded] = useState(false);

  let buttonContent;
  if (submission) {
    if (submission.passed) buttonContent = "Voir l'exercice";
    else if (submission.correction_date) buttonContent = 'Réessayer';
    else buttonContent = 'Continuer';
  } else buttonContent = "Commencer l'exercice";

  const handleClick = () => setExpanded(true);

  useEffect(() => {
    // reset force expanded on unmount
    return () => {
      setExpanded(false);
    };
  }, []);

  const finalExpanded =
    expanded || (submission && submission.passed) || forceExpanded;

  return (
    <Step expanded={finalExpanded} {...props}>
      <StepButton onClick={handleClick} disabled={finalExpanded}>
        {name}
      </StepButton>
      <StepContent>
        <Card variant="outlined">
          <CardContent>
            <Grid container spacing={2}>
              <Grid
                container
                item
                md={6}
                xs={12}
                direction="column"
                justify="space-between"
              >
                {description}
                <Link
                  to={`problem/${problem_id}/`}
                  className={classes.problemButton}
                >
                  <Button variant="contained" color="primary" fullWidth>
                    {buttonContent}
                  </Button>
                </Link>
              </Grid>
              <Grid item md={6} xs={12} className={classes.flex}>
                <SubmissionStatus variant="detailed" {...submission} />
              </Grid>
            </Grid>
          </CardContent>
        </Card>
      </StepContent>
    </Step>
  );
};

const Track = () => {
  const mounted = useRef(false);
  const classes = useStyles();
  const { trackId } = useParams();
  const dispatch = useDispatch();
  const { track, problems } = useSelector((state) => {
    const t = state.tracks.find((x) => x.id === trackId);
    return { track: t, problems: state.problems };
  });

  useEffect(() => {
    const onComponentMount = () => {
      dispatch(fetchProblems(trackId));
      dispatch(fetchTrack(trackId));
      mounted.current = true;
    };
    if (!mounted.current) onComponentMount();
  });

  const firstFailedIndex = problems.findIndex(
    (problem) => !(problem.submission && problem.submission.passed),
  );
  const activeStep =
    firstFailedIndex === -1 ? problems.length : firstFailedIndex;

  return (
    <Container maxWidth="md" className={classes.root}>
      <Typography variant="h4" className={classes.title}>
        {track && track.properties.full_name}
      </Typography>
      <Stepper activeStep={activeStep} orientation="vertical">
        {problems.map((problem, index) => (
          <ProblemNode
            {...problem}
            expanded={index <= activeStep}
            key={`problem-${index}`}
          />
        ))}
      </Stepper>
    </Container>
  );
};

export default Track;
