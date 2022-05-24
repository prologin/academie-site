import { Button, Grid, TextField, Typography } from "@mui/material";
import { makeStyles } from "@mui/styles";
import { useState } from "react";
import { register, useDispatch } from "../config/store";

const useStyles = makeStyles((theme) => ({
  leftPanel: {
    marginTop: "10% !important",
  },
  text: {
    marginTop: "20%",
  },
  form: {
    alignContent: "center",
  },
  img: {
    maxWidth: "100%",
    marginTop: -70,
  },
}));

export default function Connection() {
  const classes = useStyles();
  const dispatch = useDispatch();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = () => {
    dispatch(register(email, password));
  };

  return (
    <>
      <Grid container spacing={3}>
        <Grid sm={7} item className={classes.leftPanel}>
          <Typography variant="h3" className={classes.text}>
            <b>Apprenez</b> les bases de l'informatique
          </Typography>
          <Typography variant="h4">
            avec Académie <b>Prologin</b>
          </Typography>
          <img
            src="images/connection.svg"
            alt="connection"
            className={classes.img}
          />
        </Grid>
        <Grid spacing={2} container sm={5} item className={classes.form}>
          <Grid item xs={12}>
            <Typography variant="h6">
              <b>Créer votre compte</b>
            </Typography>
            <Typography variant="caption">
              Pour commencer votre apprentissage
            </Typography>
          </Grid>
          <Grid item xs={12}>
            <TextField
              variant="outlined"
              type="email"
              label="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              fullWidth
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              variant="outlined"
              type="password"
              label="Mot de passe"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              fullWidth
            />
          </Grid>
          <Grid item xs={12}>
            <Typography variant="caption">
              En cliquant sur s’inscrire, j’accepte les conditions d’utilisation
              et la politique de confidentialité de l’association Prologin.
              <br />
            </Typography>
          </Grid>
          <Grid item xs={12} textAlign="right">
            <Button
              styles={{ marginLeft: "auto" }}
              variant="contained"
              onClick={handleRegister}
            >
              S'inscrire
            </Button>
          </Grid>
        </Grid>
      </Grid>
    </>
  );
}
