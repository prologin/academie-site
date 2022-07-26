import {
  Button,
  Checkbox,
  FormControlLabel,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import { makeStyles } from "@mui/styles";
import { Link } from "react-router-dom";
import { useState } from "react";
import { useDispatch } from "../config/store";
import { login } from "../config/reducers/user";

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
  const [remember, setRemember] = useState(true);

  const handleLogin = () => {
    dispatch(login(email, password, remember));
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
              <b>Se connecter à Académie Prologin</b>
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
          <Grid item xs={12} textAlign="right">
            <FormControlLabel
              control={
                <Checkbox
                  checked={remember}
                  onChange={(e) => setRemember(e.target.checked)}
                />
              }
              label="Rester connecté"
            />
            <Button
              styles={{ marginLeft: "auto" }}
              variant="contained"
              onClick={handleLogin}
            >
              Se connecter
            </Button>
          </Grid>
          <Grid item xs={12} textAlign="right">
            <Typography variant="caption">
              Pas encore de compte ? <Link to="/register">S'inscrire</Link> ici.
              <br />
            </Typography>{" "}
          </Grid>
        </Grid>
      </Grid>
    </>
  );
}
