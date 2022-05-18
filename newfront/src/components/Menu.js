import { KeyboardArrowDown } from "@mui/icons-material";
import {
  Button,
  ClickAwayListener,
  Grow,
  MenuItem,
  MenuList,
  Paper,
  Popper,
} from "@mui/material";
import { useRef, useState } from "react";

export default function DropMenu({ onChange, name, value, values }) {
  const [open, setOpen] = useState(false);
  const anchorRef = useRef(null);

  const handleToggle = () => {
    setOpen((prevOpen) => !prevOpen);
  };

  const handleClick = (event) => {
    onChange(event.target.innerText);
    handleToggle();
  };

  return (
    <>
      <Button
        ref={anchorRef}
        id="composition-button"
        aria-controls={open ? "composition-menu" : undefined}
        aria-expanded={open ? "true" : undefined}
        aria-haspopup="true"
        onClick={handleToggle}
        variant="contained"
        sx={{ mx: 1 }}
        endIcon={<KeyboardArrowDown />}
      >
        {name} : {value}
      </Button>
      <Popper
        open={open}
        role={undefined}
        anchorEl={anchorRef.current}
        placement="bottom-start"
        transition
        disablePortal
        sx={{ zIndex: 10 }}
      >
        {({ TransitionProps, placement }) => (
          <Grow
            {...TransitionProps}
            style={{
              transformOrigin:
                placement === "bottom-start" ? "left top" : "left bottom",
            }}
          >
            <Paper>
              <ClickAwayListener onClickAway={handleToggle}>
                <MenuList
                  id="composition-menu"
                  aria-labelledby="composition-button"
                >
                  {values.map((val) => (
                    <MenuItem onClick={handleClick} key={val}>
                      {val}
                    </MenuItem>
                  ))}
                </MenuList>
              </ClickAwayListener>
            </Paper>
          </Grow>
        )}
      </Popper>
    </>
  );
}
