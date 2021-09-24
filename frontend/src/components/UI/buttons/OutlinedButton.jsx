import { Button } from '@mui/material'
import { useHistory } from 'react-router'
import { useStyles } from './OutlinedButton.styles'

const OutlinedButton = ({ path, text }) => {
    const styles = useStyles()
    const history = useHistory()

    return (
        < Button
            className={styles.button}
            variant="outlined"
            size="small"
            onClick={() => history.push(path)}
        >
            {text}
        </ Button>
    )

}

export default OutlinedButton
