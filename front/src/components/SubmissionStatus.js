import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core';

import Tooltip from '@material-ui/core/Tooltip';
import Alert from '@material-ui/lab/Alert';
import CircularProgress from '@material-ui/core/CircularProgress';

const useStyles = makeStyles((theme) => ({
  loader: {
    marginRight: theme.spacing(2),
    verticalAlign: 'middle',
  },
  alert: {
    paddingTop: 0,
    paddingBottom: 0,
  },
}));

const SubmissionStatus = ({
  submission_count,
  submission_date,
  correction_date,
  passed,
  loader,
}) => {
  const classes = useStyles();

  if (loader) return <CircularProgress size={25} className={classes.loader} />;

  if (correction_date) {
    const correctioDate = new Date(correction_date).toLocaleString();
    if (passed)
      return (
        <Tooltip
          title={`Tests réussis le ${correctioDate}`}
          arrow
        >
          <Alert severity="success" className={classes.alert}>
            Succès
          </Alert>
        </Tooltip>
      );
    return (
      <Tooltip
        title={`Tests échoués le ${correctioDate}`}
        arrow
      >
        <Alert severity="warning" className={classes.alert}>
          Echec
        </Alert>
      </Tooltip>
    );
  }

  if (submission_count)
    return (
      <Tooltip
        title={new Date(submission_date).toLocaleString()}
        arrow
      >
        <Alert severity="info" className={classes.alert}>
          Enregistré
        </Alert>
      </Tooltip>
    );
  return null;
};

SubmissionStatus.propTypes = {
  submission_count: PropTypes.number,
  submission_date: PropTypes.string,
  correction_date: PropTypes.string,
  passed: PropTypes.bool,
  loader: PropTypes.bool.isRequired,
};

export default SubmissionStatus;
