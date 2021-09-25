import { useHistory } from "react-router"
import { useStyles } from "./TickerField.styles"

export const TickerField = ({ ticker }) => {
    const styles = useStyles()
    const history = useHistory()

    return (
        <button
            onClick={() => { history.push(`/stocks/${ticker}`) }}
            className={styles.link}
        >
            {ticker}
        </button>
    )
}