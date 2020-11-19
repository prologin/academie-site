import React, { useEffect, useRef, useState } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';

import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

import TrackApi from '../api/trackApi';
import { Container } from '@material-ui/core';

const useStyles = makeStyles({
  root: {
    padding: 16,
  },
});

const TrackNode = ({ id, properties }) => {
  const { description, full_name: title } = properties;
  return (
    <Card variant="outlined">
      <CardContent>
        <Typography variant="h5">{title}</Typography>
        <Typography variant="body2">{description}</Typography>
      </CardContent>
      <CardActions>
        <Link to={`/track/${id}`}>
          <Button variant="contained" color="primary">
            Commencer les exercices
          </Button>
        </Link>
      </CardActions>
    </Card>
  );
};

TrackNode.propTypes = {
  id: PropTypes.number.isRequired,
  properties: PropTypes.object.isRequired,
};

const Tracks = () => {
  const mounted = useRef(false);
  const classes = useStyles();
  const [tracks, setTracks] = useState(null);

  useEffect(() => {
    const onComponentMount = async () => {
      const data = await TrackApi.getTracks();
      setTracks(data);
      mounted.current = true;
    };
    if (!mounted.current) onComponentMount();
  });

  const TrackList = () =>
    tracks && tracks.length ? (
      tracks.map((track, index) => (
        <Grid item xs={12} key={`track-${index}`}>
          <TrackNode {...track} />
        </Grid>
      ))
    ) : (
      <Typography variant="h5">Aucun cursus pour l'instant.</Typography>
    );

  return (
    <Container maxWidth="md" className={classes.root}>
      <Grid container justify="center" spacing={2}>
        <TrackList />
      </Grid>
    </Container>
  );
};

export default Tracks;
