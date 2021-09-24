import { useStyles } from "./TickerField.styles"

export const TickerField = ({ ticker }) => {
    const styles = useStyles()

    return (
        <a href={ticker} className={styles.link}>{ticker}</a>
    )
}