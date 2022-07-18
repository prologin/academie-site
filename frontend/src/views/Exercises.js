import { useRef, useEffect } from 'react';
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
import { Link, useParams } from 'react-router-dom';

import { useDispatch, getCourse, useSelector } from '../config/store';
import ExercisesNode from '../components/ExercisesNode';

const useStyles = makeStyles((theme) => ({
  fullWidth: {
    maxWidth: '100%',
    borderRadius: 10,
  },
}));

export default function Exercises() {
  const classes = useStyles();
  const { courseId } = useParams();
  const course = useSelector((state) => state.course);
  const dispatch = useDispatch();

  const mounted = useRef(false);

  useEffect(() => {
    if (!mounted.current) {
      mounted.current = true;
      dispatch(getCourse(courseId));
    }
    // eslint-disable-next-line
  }, []);

  return (
    <Grid container spacing={3}>
      {course.problems && (
        <>
          <Grid item>
            <Typography variant="h4">
              <b>{course.title}</b>
            </Typography>
          </Grid>
          <Grid item>
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
                        <b>Nombre de modules : </b>
                        {course.problems.length}
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
          </Grid>
          <Grid item>
            <Typography variant="h5">
              <b>Description</b>
            </Typography>
          </Grid>
          <Grid item>
            <Typography>{course.description}</Typography>
          </Grid>
          <Grid item>
            <Typography variant="h5">
              <b>Liste des exercices</b>
            </Typography>
          </Grid>
          <Grid sm={9} item>
            <Stepper activeStep={1} alternativeLabel>
              {course.problems &&
                course.problems.map((label, index) => (
                  <Step key={index + 1}>
                    <StepLabel />
                  </Step>
                ))}
            </Stepper>
          </Grid>
          <ExercisesNode exercises={course.problems} />
        </>
      )}
    </Grid>
  );
}
