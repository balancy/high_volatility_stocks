import { AppBar, Toolbar } from '@mui/material'

import OutlinedButton from '../UI/buttons/OutlinedButton';
import { useHistory } from 'react-router';
import { useStyles } from './AppHeader.styles';

const AppHeader = () => {
    const styles = useStyles();
    const history = useHistory()

    return (
        <AppBar
            position="sticky"
            color="transparent"
            className={styles.appBar}
        >
            <Toolbar variant="regular" className={styles.toolBar}>
                <OutlinedButton
                    method={() => history.push("/")}
                    text="Stocks"
                />
                <div className={styles.space} />
                <OutlinedButton
                    method={() => history.push("/charts")}
                    text="Charts"
                />
            </Toolbar>
        </AppBar>
    )
}

export default AppHeader
