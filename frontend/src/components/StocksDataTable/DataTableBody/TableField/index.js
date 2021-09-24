import ColoredFieldValue from './ColoredFieldValue'
import React from 'react'
import { StyledTableCell } from './styles'
import TickerField from './TickerField'

const TableField = ({ item, field }) => {
    return (
        <StyledTableCell>
            {
                "direct_order" in field
                    ? <ColoredFieldValue value={item[field.name]} field={field} />
                    : field.name === "ticker"
                        ? <TickerField ticker={item[field.name]} />
                        : item[field.name]
            }
        </StyledTableCell>
    )
}

export default TableField
