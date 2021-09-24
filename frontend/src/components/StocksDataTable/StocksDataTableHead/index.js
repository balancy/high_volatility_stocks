import { TableHead, TableRow } from '@mui/material'

import React from 'react'
import { STOCKS_TABLE_HEADERS } from '../../../constants'
import { StyledTableCell } from '../styles'

const StocksDataTableHead = () =>
    <TableHead>
        <TableRow>
            {
                STOCKS_TABLE_HEADERS.map((item) =>
                    <StyledTableCell key={item}>
                        {item}
                    </StyledTableCell>
                )
            }
        </TableRow>
    </TableHead>

export default StocksDataTableHead
