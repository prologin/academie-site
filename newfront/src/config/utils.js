import { useEffect, useRef } from 'react';

export const jwtToJson = (jwt) => JSON.parse(atob(jwt.split('.')[1]));

export const usePrevious = (value) => {
  const ref = useRef();
  useEffect(() => {
    ref.current = value;
  }, [value]);
  return ref.current;
};
