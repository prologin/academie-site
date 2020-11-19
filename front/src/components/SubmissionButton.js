import React from 'react';
import { makeStyles } from '@material-ui/core';

import Button from '@material-ui/core/Button';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCaretDown } from '@fortawesome/free-solid-svg-icons';

import Dropdown from './Dropdown';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  submissionButton: {
    borderTopRightRadius: 0,
    borderBottomRightRadius: 0,
  },
  extraActionsButton: {
    borderTopLeftRadius: 0,
    borderBottomLeftRadius: 0,
    minWidth: 'unset',
  },
}));

const SubmissionButton = ({ onSubmit, onSave }) => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Button
        variant="contained"
        color="primary"
        className={classes.submissionButton}
        onClick={onSubmit}
      >
        Corriger
      </Button>
      <Dropdown
        variant="contained"
        color="primary"
        items={[{ content: 'Enregistrer le brouillon', onClick: onSave }]}
        title={<FontAwesomeIcon icon={faCaretDown} />}
        buttonProps={{ className: classes.extraActionsButton }}
        menuProps={{
          anchorOrigin: {
            vertical: 'bottom',
            horizontal: 'right',
          },
          transformOrigin: {
            vertical: 'top',
            horizontal: 'right',
          },
        }}
      />
    </div>
  );
};

export default SubmissionButton;
