import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core';

import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCaretDown } from '@fortawesome/free-solid-svg-icons';

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
  const [anchorEl, setAnchorEl] = useState(null);

  const handleOpenExtraActionsMenu = (e) => {
    setAnchorEl(e.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleSave = () => {
    onSave();
    handleClose();
  };

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
      <Button
        variant="contained"
        color="primary"
        onClick={handleOpenExtraActionsMenu}
        className={classes.extraActionsButton}
      >
        <FontAwesomeIcon icon={faCaretDown} />
      </Button>
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
        getContentAnchorEl={null}
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'right',
        }}
        transformOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
      >
        <MenuItem onClick={handleSave}>Enregistrer le brouillon</MenuItem>
      </Menu>
    </div>
  );
};

export default SubmissionButton;
