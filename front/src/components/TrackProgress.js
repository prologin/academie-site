import React, { useEffect, useRef } from 'react';
import { Link, useParams } from 'react-router-dom';
import { makeStyles } from '@material-ui/core';
import { fetchProblems, useTracked } from '../config/store';

import LinearProgress from '@material-ui/core/LinearProgress';
import Button from '@material-ui/core/Button';
import Fade from '@material-ui/core/Fade';

const useStyles = makeStyles((theme) => ({
  container: {
    display: 'flex',
    alignItems: 'center',
  },
  grow: {
    flexGrow: 1,
  },
  navigationButton: {
    margin: `0 ${theme.spacing(1)}px`,
    borderRadius: 0,
    //backgroundColor: "grey"
  },
  disabled: {
    pointerEvents: 'none',
    cursor: 'default',
  },
}));

const TrackProgress = () => {
  const mounted = useRef(false);
  const classes = useStyles();
  const { trackId, problemId } = useParams();
  const [state, dispatch] = useTracked();
  const { problems } = state;

  useEffect(() => {
    const onComponentMount = () => {
      if (problems.length <= 1) {
        dispatch(fetchProblems(trackId));
      }
      mounted.current = true;
    };
    if (!mounted.current) onComponentMount();
  });

  const index = problems.findIndex(
    (problem) => problem.problem_id === problemId,
  );
  const prevId = index - 1 >= 0 && problems[index - 1].problem_id;
  const nextId = index + 1 < problems.length && problems[index + 1].problem_id;

  return (
    <Fade in>
      <div className={classes.container}>
        <Link
          to={`../${prevId}/`}
          className={!prevId ? classes.disabled : undefined}
        >
          <Button
            variant="contained"
            disableElevation
            className={classes.navigationButton}
            size="small"
            color="primary"
            disabled={!prevId}
          >
            Précédent
          </Button>
        </Link>
        <div className={classes.grow}>
          <small>
            {index + 1}/{problems.length}
          </small>
          <LinearProgress
            variant="determinate"
            value={(index / (problems.length - 1)) * 100}
          />
          <small>{index !== -1 && problems[index].properties.name}</small>
        </div>
        <Link to={nextId ? `../${nextId}/` : '../..'}>
          <Button
            variant="contained"
            disableElevation
            size="small"
            color="primary"
            className={classes.navigationButton}
          >
            {nextId ? 'Suivant' : 'Terminer'}
          </Button>
        </Link>
      </div>
    </Fade>
  );
};

export default TrackProgress;
