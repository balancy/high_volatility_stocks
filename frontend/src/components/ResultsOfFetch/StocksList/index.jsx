import { STOCKS_TABLE_FIELDNAMES, STOCKS_TABLE_HEADERS } from '../../../constants'
import { StyledTableCell, StyledTableRow } from './styles'

import Paper from '@mui/material/Paper'
import React from 'react'
import Table from '@mui/material/Table'
import TableBody from '@mui/material/TableBody'
import TableContainer from '@mui/material/TableContainer'
import TableHead from '@mui/material/TableHead'
import TableRow from '@mui/material/TableRow'

const StocksList = ({ data }) => {
    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} size="small">
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
            </Table>
        </TableContainer>
    )
}

export default StocksList
