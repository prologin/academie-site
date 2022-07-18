import {
  Box,
  Collapse,
  Drawer,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Typography,
} from "@mui/material";
import {
  Article,
  ExpandLess,
  ExpandMore,
  Lightbulb,
  MenuBook,
} from "@mui/icons-material";
import { useState } from "react";
import Editor from "../components/Editor";

export default function Code() {
  const [descriptionOpen, setDescriptionOpen] = useState();
  const [exerciseOpen, setExerciseOpen] = useState();
  const [tipOpen, setTipOpen] = useState();

  const drawerWidth = 300;

  return (
    <Box sx={{ display: "flex" }}>
      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: {
            width: drawerWidth,
            boxSizing: "border-box",
          },
        }}
      >
        <Toolbar />
        <List
          sx={{
            width: "100%",
            height: "100%",
            maxWidth: 360,
            bgcolor: "background.paper",
          }}
          component="nav"
        >
          <ListItemButton onClick={() => setDescriptionOpen(!descriptionOpen)}>
            <ListItemIcon>
              <MenuBook />
            </ListItemIcon>
            <ListItemText primary="Description" />
            {descriptionOpen ? <ExpandLess /> : <ExpandMore />}
          </ListItemButton>
          <Collapse in={descriptionOpen} timeout="auto" unmountOnExit>
            <Typography sx={{ px: 4, py: 2 }}>
              Ceci est une description
            </Typography>
          </Collapse>
          <ListItemButton onClick={() => setExerciseOpen(!exerciseOpen)}>
            <ListItemIcon>
              <Article />
            </ListItemIcon>
            <ListItemText primary="Exercice" />
            {exerciseOpen ? <ExpandLess /> : <ExpandMore />}
          </ListItemButton>
          <Collapse in={exerciseOpen} timeout="auto" unmountOnExit>
            <Typography sx={{ px: 4, py: 2 }}>Ceci est l'exercice</Typography>
          </Collapse>
          <ListItemButton onClick={() => setTipOpen(!tipOpen)}>
            <ListItemIcon>
              <Lightbulb />
            </ListItemIcon>
            <ListItemText primary="Indice" />
            {tipOpen ? <ExpandLess /> : <ExpandMore />}
          </ListItemButton>
          <Collapse in={tipOpen} timeout="auto" unmountOnExit>
            <Typography sx={{ px: 4, py: 2 }}>Ceci est un indice</Typography>
          </Collapse>
        </List>
      </Drawer>
      <Box sx={{ flexGrow: 1 }}>
        <Editor />
      </Box>
    </Box>
  );
}
