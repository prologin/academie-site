import React from 'react';
import { useParams } from 'react-router-dom';

const Track = () => {
  const { trackId } = useParams();

  return trackId;
};

export default Track;
