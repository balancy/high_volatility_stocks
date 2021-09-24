import { TableHead, TableRow } from '@mui/material'

import React from 'react'
import { StyledTableCell } from '../styles'
import { table_headers } from '../../../constants'

const StocksDataTableHead = () =>
    <TableHead>
        <TableRow>
            {
                table_headers.map((item) =>
                    <StyledTableCell key={item}>
                        {item}
                    </StyledTableCell>
                )
            }
        </TableRow>
    </TableHead>

export default StocksDataTableHead
