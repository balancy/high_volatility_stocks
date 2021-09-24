import NumericField from '../Fields/NumericField'
import { StyledTableCell } from './TableCell.styles'
import { TickerField } from '../Fields/TickerField'

const TableCell = ({ item, field }) => {
    return (
        <StyledTableCell>
            {
                "direct_order" in field
                    ? <NumericField value={item[field.name]} field={field} />
                    : field.name === "ticker"
                        ? <TickerField ticker={item[field.name]} />
                        : item[field.name]
            }
        </StyledTableCell>
    )
}

export default TableCell
