import { StyledTableCell, StyledTableRow } from '../styles'

import React from 'react'
import { STOCKS_TABLE_FIELDNAMES } from '../../../constants'
import { TableBody } from '@mui/material'

const StocksDataTableBody = ({ data, fieldnames }) =>
    <TableBody>
        {data.map((item) => (
            <StyledTableRow key={item.id}>
                {
                    STOCKS_TABLE_FIELDNAMES.map((field) =>
                        <StyledTableCell>
                            {item[field]}
                        </StyledTableCell>
                    )
                }
            </StyledTableRow>
        ))}
    </TableBody>

export default StocksDataTableBody
