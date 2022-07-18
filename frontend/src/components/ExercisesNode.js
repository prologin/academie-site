import { Card, CardContent, Grid, Typography, Button } from '@mui/material';
import { Link } from 'react-router-dom';

export default function ExercisesNode({ exercises }) {
  return (
    <>
      {exercises &&
        exercises.map((exercise) => (
          <Grid sm={9} item key={exercise.id}>
            <Card>
              <CardContent>
                <Grid container spacing={2} alignItems="flex-end">
                  <Grid xs={12} item>
                    <Typography gutterBottom variant="h5" component="div">
                      <b>{exercise.title}</b>
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
        ))}
    </>
  );
}
