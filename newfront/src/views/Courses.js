import { Grid, Typography } from '@mui/material';
import { useEffect, useRef } from 'react';

import { useDispatch, useSelector, getCourses } from '../config/store';
import CoursesNode from '../components/CoursesNode';

export default function Courses() {
  const mounted = useRef(false);
  const courses = useSelector(
    (state) => state.courses && state.courses.results,
  );
  const dispatch = useDispatch();

  useEffect(() => {
    if (!mounted.current) {
      mounted.current = true;
      dispatch(getCourses());
    }
    // eslint-disable-next-line
  }, []);

  return (
    <Grid container spacing={3}>
      <Grid xs={12} item>
        <Typography variant="h5">
          <b>Cours</b> en libre accès
        </Typography>
      </Grid>
      <CoursesNode courses={courses} />
    </Grid>
  );
}
