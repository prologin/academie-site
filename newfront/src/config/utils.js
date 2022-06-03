export const jwtToJson = (jwt) => JSON.parse(atob(jwt.split(".")[1]));
