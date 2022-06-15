import {
  Button,
  Card,
  CardContent,
  Grid,
  Step,
  StepLabel,
  Stepper,
  Typography,
} from '@mui/material';
import { makeStyles } from '@mui/styles';
import { Link } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
  fullWidth: {
    maxWidth: '100%',
    borderRadius: 10,
  },
}));

export default function Exercises() {
  const classes = useStyles();

  return (
    <Grid container spacing={3}>
      <Grid item>
        <Typography variant="h4">
          <b>Introduction aux bases de l'informatique</b>
        </Typography>
      </Grid>
      <Grid item>
        <Card>
          <CardContent>
            <Grid container spacing={2}>
              <Grid item sm={3}>
                <img
                  src="/images/temp.jpg"
                  alt="cover"
                  className={classes.fullWidth}
                />
              </Grid>
              <Grid item sm={9} container alignContent="center">
                <Grid sm={6} item>
                  <Typography variant="subtitle1">
                    <b>Difficulté :</b>
                  </Typography>
                </Grid>
                <Grid sm={6} item>
                  <Typography variant="subtitle1">
                    <b>Préréquis :</b>
                  </Typography>
                </Grid>
                <Grid sm={6} item>
                  <Typography variant="subtitle1">
                    <b>Nombre de modules :</b>
                  </Typography>
                </Grid>
                <Grid sm={6} item>
                  <Typography variant="subtitle1">
                    <b>Langages disponibles :</b>
                  </Typography>
                </Grid>
              </Grid>
            </Grid>
          </CardContent>
        </Card>
      </Grid>
      <Grid item>
        <Typography variant="h5">
          <b>Description</b>
        </Typography>
      </Grid>
      <Grid item>
        <Typography>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut rhoncus
          elit et sapien semper, at imperdiet metus hendrerit. Aenean blandit
          tellus a nibh varius, volutpat iaculis enim dignissim. Morbi congue
          pretium neque nec vulputate. Praesent venenatis felis sapien, accumsan
          pulvinar ipsum imperdiet vitae. Donec elementum sem ac viverra
          efficitur. Proin dictum ex nec odio ultrices, ut venenatis tellus
          ornare. Nulla sodales lobortis tincidunt. In egestas lectus sit amet
          nisi aliquam, ac tempus leo volutpat. Phasellus porta nunc vel dapibus
          imperdiet. Integer vitae dictum velit. Fusce nec justo justo.
        </Typography>
      </Grid>
      <Grid item>
        <Typography variant="h5">
          <b>Liste des exercices</b>
        </Typography>
      </Grid>
      <Grid sm={9} item>
        <Stepper activeStep={1} alternativeLabel>
          {[0, 1, 2].map((label) => (
            <Step key={label}>
              <StepLabel />
            </Step>
          ))}
        </Stepper>
      </Grid>
      <Grid sm={9} item>
        <Card>
          <CardContent>
            <Grid container spacing={2} alignItems="flex-end">
              <Grid xs={12} item>
                <Typography gutterBottom variant="h5" component="div">
                  <b>Les variables</b>
                </Typography>
              </Grid>
              <Grid item container spacing={1} sm={6}>
                <Grid sm={12} item>
                  <Typography variant="subtitle1">
                    <b>Difficulté :</b>
                  </Typography>
                </Grid>
                <Grid sm={12} item>
                  <Typography variant="subtitle1">
                    <b>Préréquis :</b>
                  </Typography>
                </Grid>
              </Grid>
              <Grid sm={6} item textAlign="right">
                <Link to="/code/">
                  <Button variant="contained">Continuer</Button>
                </Link>
              </Grid>
            </Grid>
          </CardContent>
        </Card>
      </Grid>
    </Grid>
  );
}
