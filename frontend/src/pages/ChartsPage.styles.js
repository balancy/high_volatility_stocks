import { makeStyles } from "@material-ui/styles";

export const useStyles = makeStyles({
    container: {
        paddingLeft: 0,
        paddingRight: 0,
        marginTop: 0,
    },
    image: {
        marginBottom: 18,
        marginRight: 24,
        marginLeft: 0,
        marginTop: 0,
        border: "1px solid",
        width: 550,
    },
    link: {
        textDecoration: `none`,
        fontWeight: `600`,
        color: `inherit`,
        cursor: `pointer`,
        background: `none!important`,
        border: `none`,
        padding: `0!important`,
    },
});