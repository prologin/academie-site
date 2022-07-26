import {
  Button,
  Checkbox,
  FormControlLabel,
  FormGroup,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import { makeStyles } from "@mui/styles";
import { useState } from "react";
import { useDispatch } from "../config/store";
import { register } from "../config/reducers/user";

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

export default function Register() {
  const classes = useStyles();
  const dispatch = useDispatch();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirm, setPasswordConfirm] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [birthdate, setBirthdate] = useState(null);
  const [acceptNewsletter, setAcceptNewsletter] = useState(false);
  const [remember, setRemember] = useState(true);

  const handleRegister = () => {
    if (
      password &&
      password === passwordConfirm &&
      firstName &&
      lastName &&
      username &&
      birthdate
    )
      dispatch(
        register(
          email,
          password,
          username,
          firstName,
          lastName,
          birthdate,
          acceptNewsletter,
          remember
        )
      );
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
            src="/images/connection.svg"
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
              required
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              variant="outlined"
              type="text"
              label="Nom d'utilisateur"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              fullWidth
              required
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              variant="outlined"
              type="text"
              label="Prénom"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              fullWidth
              required
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              variant="outlined"
              type="text"
              label="Nom"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
              fullWidth
              required
            />
          </Grid>
          <Grid item xs={12}>
            <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                disableFuture
                label="Date de naissance"
                value={birthdate}
                onChange={(newValue) => {
                  setBirthdate(newValue);
                }}
                renderInput={(params) => (
                  <TextField {...params} fullWidth required />
                )}
              />
            </LocalizationProvider>
          </Grid>
          <Grid item xs={12}>
            <TextField
              variant="outlined"
              type="password"
              label="Mot de passe"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              fullWidth
              required
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              variant="outlined"
              type="password"
              label="Confirmation mot de passe"
              value={passwordConfirm}
              error={password !== passwordConfirm}
              onChange={(e) => setPasswordConfirm(e.target.value)}
              fullWidth
              required
            />
          </Grid>
          <Grid item xs={12}>
            <FormGroup>
              <FormControlLabel
                control={
                  <Checkbox
                    checked={acceptNewsletter}
                    onChange={(e) => setAcceptNewsletter(e.target.checked)}
                  />
                }
                label="S'inscrire à notre newsletter"
              />
            </FormGroup>
            <Typography variant="caption">
              Nous n'envoyons des e-mails que pour vous informer des news
              importantes sur nos activités.
              <br />
            </Typography>
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
              onClick={handleRegister}
            >
              S'inscrire
            </Button>
          </Grid>
          <Grid item xs={12}>
            <Typography variant="caption">
              En cliquant sur s’inscrire, j’accepte les conditions d’utilisation
              et la politique de confidentialité de l’association Prologin.
              <br />
            </Typography>
          </Grid>
        </Grid>
      </Grid>
    </>
  );
}
