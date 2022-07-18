import { Card, CardContent, Grid, Typography } from '@mui/material';
import { Link } from 'react-router-dom';
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
  fullWidth: {
    maxWidth: '100%',
    borderRadius: 10,
  },
}));

export default function CoursesNode({ courses }) {
  const classes = useStyles();

  return (
    <>
      {courses &&
        courses.map((course) => (
          <Grid xs={12} item key={course.id}>
            <Link to={`/exercises/${course.title}/`}>
              <Card>
                <CardContent>
                  <Grid container spacing={2}>
                    <Grid item sm={3}>
                      <img
                        src={course.image}
                        alt="cover"
                        className={classes.fullWidth}
                      />
                    </Grid>
                    <Grid item sm={9} container>
                      <Grid xs={12} item>
                        <Typography gutterBottom variant="h5" component="div">
                          <b>{course.title}</b>
                        </Typography>
                      </Grid>
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
                          <b>Nombre de modules : </b>
                          {course.count}
                        </Typography>
                      </Grid>
                      <Grid sm={6} item>
                        <Typography variant="subtitle1">
                          <b>Langages disponibles : </b>
                          {course.languages_list.join(', ')}
                        </Typography>
                      </Grid>
                    </Grid>
                  </Grid>
                </CardContent>
              </Card>
            </Link>
          </Grid>
        ))}
    </>
  );
}
