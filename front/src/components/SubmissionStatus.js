import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core';

import Tooltip from '@material-ui/core/Tooltip';
import Alert from '@material-ui/lab/Alert';
import CircularProgress from '@material-ui/core/CircularProgress';
import Divider from '@material-ui/core/Divider';

import SuccessOutlinedIcon from '@material-ui/lab/internal/svg-icons/SuccessOutlined';
import ReportProblemOutlinedIcon from '@material-ui/lab/internal/svg-icons/ReportProblemOutlined';
import InfoOutlinedIcon from '@material-ui/lab/internal/svg-icons/InfoOutlined';

const useStyles = makeStyles((theme) => ({
  loader: {
    marginRight: theme.spacing(2),
    verticalAlign: 'middle',
  },
  alert: {
    paddingTop: 0,
    paddingBottom: 0,
    display: 'inline-flex',
  },
  statusIcon: {
    alignSelf: 'center',
    marginRight: theme.spacing(2),
  },
  successIcon: {
    color: '#4caf50',
  },
  warningIcon: {
    color: '#ff9800',
  },
  infoIcon: {
    color: '#2196f3',
  },
  notTreated: {
    flexGrow: 1,
    textAlign: 'center',
    alignSelf: 'center',
  },
}));

const SubmissionStatus = ({
  submission_count,
  correction_count,
  submission_date,
  correction_date,
  passed,
  variant,
  loader,
}) => {
  const classes = useStyles();

  if (loader) return <CircularProgress size={25} className={classes.loader} />;

  if (correction_date) {
    const correctioDate = new Date(correction_date).toLocaleString();
    // Submission success
    if (passed) {
      if (variant === 'consise')
        return (
          <Tooltip title={`Exercice réussi le ${correctioDate}`} arrow>
            <Alert severity="success" className={classes.alert}>
              Succès
            </Alert>
          </Tooltip>
        );
      return (
        <>
          <Tooltip title="Succès">
            <SuccessOutlinedIcon
              className={`${classes.statusIcon} ${classes.successIcon}`}
            />
          </Tooltip>
          <Divider orientation="vertical" />
          <ul>
            <li>Exercice réussi !</li>
            <li>
              Date de correction : {new Date(correction_date).toLocaleString()}
            </li>
            <li>Nombre de Soumissions : {correction_count}</li>
          </ul>
        </>
      );
    }

    // Submission failure
    else {
      if (variant === 'consise')
        return (
          <Tooltip title={`Exercice raté le ${correctioDate}`} arrow>
            <Alert severity="warning" className={classes.alert}>
              Échec
            </Alert>
          </Tooltip>
        );
      return (
        <>
          <Tooltip title="Échec">
            <ReportProblemOutlinedIcon
              className={`${classes.statusIcon} ${classes.warningIcon}`}
            />
          </Tooltip>
          <Divider orientation="vertical" />
          <ul>
            <li>Exercice raté !</li>
            <li>
              Date de correction : {new Date(correction_date).toLocaleString()}
            </li>
            <li>Nombre de Soumissions : {correction_count}</li>
          </ul>
        </>
      );
    }
  }

  // Submission saved
  if (submission_count) {
    if (variant === 'consise')
      return (
        <Tooltip title={new Date(submission_date).toLocaleString()} arrow>
          <Alert severity="info" className={classes.alert}>
            Enregistré
          </Alert>
        </Tooltip>
      );
    return (
      <>
        <Tooltip title="Brouillon">
          <InfoOutlinedIcon
            className={`${classes.statusIcon} ${classes.infoIcon}`}
          />
        </Tooltip>
        <Divider orientation="vertical" />
        <ul>
          <li>Exercice commencé</li>
          <li>
            Date d'enregistrement : {new Date(submission_date).toLocaleString()}
          </li>
        </ul>
      </>
    );
  }

  // No submission yet
  return variant === 'consise' ? null : (
    <>
      <Tooltip title="Pas commencé">
        <InfoOutlinedIcon
          className={`${classes.statusIcon} ${classes.infoIcon}`}
        />
      </Tooltip>
      <Divider orientation="vertical" />
      <div className={classes.notTreated}>Tu n'as pas encore commencé !</div>
    </>
  );
};

SubmissionStatus.propTypes = {
  submission_count: PropTypes.number,
  submission_date: PropTypes.string,
  correction_date: PropTypes.string,
  passed: PropTypes.bool,
  variant: PropTypes.oneOf(['consise', 'detailed']),
  loader: PropTypes.bool,
};
SubmissionStatus.defaultProps = {
  variant: 'consise',
  loader: false,
};

export default SubmissionStatus;
