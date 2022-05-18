import { Card, CardContent, Grid, Typography } from "@mui/material";
import { makeStyles } from "@mui/styles"
import { Link } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
    fullWidth: {
        maxWidth: "100%",
        borderRadius: 10
    }
}))

export default function Courses() {
    const classes = useStyles();

    return (
      <Grid container spacing={3}>
        <Grid xs={12} item>
          <Typography variant="h5">
            <b>Cours</b> en libre accès
          </Typography>
        </Grid>
        <Grid xs={12} item>
          <Link to="/exercises/">
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
                  <Grid item sm={9} container>
                    <Grid xs={12} item>
                      <Typography gutterBottom variant="h5" component="div">
                        <b>Introduction aux bases de l'informatique</b>
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
          </Link>
        </Grid>
      </Grid>
    );
}