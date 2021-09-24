import { makeStyles } from "@material-ui/styles";

export const useStyles = makeStyles({
    appBar: {
        border: `none`,
        boxShadow: `none`,
        backgroundColor: `white`,
    },
    toolBar: {
        padding: 0,
        marginBottom: 12,
    },
    button: {
        minWidth: 200,
        border: `2px solid`,
        marginRight: 12,
        marginLeft: 0,
        variant: `contained`,
    },
});