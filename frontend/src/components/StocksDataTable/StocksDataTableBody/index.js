import { StyledTableCell, StyledTableRow } from '../styles'

import React from 'react'
import { TableBody } from '@mui/material'
import { table_fieldnames } from '../../../constants'

const StocksDataTableBody = ({ data }) =>
    <TableBody>
        {data.map((item) => (
            <StyledTableRow key={item.id}>
                {
                    table_fieldnames.map((field) =>
                        <StyledTableCell>
                            {item[field]}
                        </StyledTableCell>
                    )
                }
            </StyledTableRow>
        ))}
    </TableBody>

export default StocksDataTableBody
