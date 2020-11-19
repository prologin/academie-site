import React, { useState } from 'react';
import PropTypes from 'prop-types';

import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';

const Dropdown = ({
  title,
  items,
  variant,
  color,
  buttonProps = {},
  menuProps = {},
}) => {
  const [anchorEl, setAnchorEl] = useState(null);

  const handleOpen = (e) => {
    setAnchorEl(e.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleClick = (item) => {
    item.onClick();
    handleClose();
  };

  return (
    <>
      <Button
        variant={variant}
        color={color}
        onClick={handleOpen}
        {...buttonProps}
      >
        {title}
      </Button>
      <Menu
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
        getContentAnchorEl={null}
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'left',
        }}
        {...menuProps}
      >
        {items.map((item, index) => (
          <MenuItem onClick={() => handleClick(item)} key={`item-${index}`}>
            {item.content}
          </MenuItem>
        ))}
      </Menu>
    </>
  );
};

Dropdown.propTypes = {
  title: PropTypes.node.isRequired,
  items: PropTypes.arrayOf(
    PropTypes.shape({
      content: PropTypes.node.isRequired,
      onClick: PropTypes.func.isRequired,
    }),
  ).isRequired,
  variant: PropTypes.string,
  color: PropTypes.string,
  buttonProps: PropTypes.object,
  menuProps: PropTypes.object,
};

export default Dropdown;
