import { useStyles } from './NumericField.styles'

const ColoredFieldValue = ({ value, field }) => {
    const styles = useStyles()

    let style;

    if (
        (field.direct_order && value < field.min_value) ||
        (!field.direct_order && value > field.max_value)
    ) {
        style = styles.green;
    } else if (
        (field.direct_order && value > field.max_value) ||
        (!field.direct_order && value < field.min_value)
    ) {
        style = styles.red;
    } else {
        style = styles.normal;
    }

    return (
        <span className={style}>{value}</span>
    )
}

export default ColoredFieldValue
