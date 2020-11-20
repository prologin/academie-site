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

import TrackApi from '../api/trackApi';
import { Typography } from '@material-ui/core';
import SubmissionStatus from './SubmissionStatus';

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
  const [forceExpanded, setExpanded] = useState(
    expanded || (submission && submission.passed),
  );

  let buttonContent;
  if (submission) {
    if (submission.passed) buttonContent = "Voir l'exercice";
    else if (submission.correction_date) buttonContent = 'Réessayer';
    else buttonContent = 'Continuer';
  } else buttonContent = "Commencer l'exercice";

  const handleClick = () => setExpanded(true);

  return (
    <Step expanded={forceExpanded} {...props}>
      <StepButton onClick={handleClick} disabled={forceExpanded}>
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
                  component={({ href }) => (
                    <Button
                      variant="contained"
                      color="primary"
                      href={href}
                      className={classes.problemButton}
                    >
                      {buttonContent}
                    </Button>
                  )}
                />
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
  const [track, setTrack] = useState(null);
  const [problems, setProblems] = useState([]);

  useEffect(() => {
    const onComponentMount = async () => {
      const trackData = await TrackApi.getTrack(trackId);
      mounted.current = true;
      setTrack(trackData);
      const problemsData = await TrackApi.getProblems(trackId);
      setProblems(problemsData);
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
