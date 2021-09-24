import Paper from '@mui/material/Paper'
import React from 'react'
import StocksDataTableBody from './StocksDataTableBody'
import StocksDataTableHead from './StocksDataTableHead'
import Table from '@mui/material/Table'
import TableContainer from '@mui/material/TableContainer'

const StocksDataTable = ({ data }) => {
    return (
        <TableContainer component={Paper}>
            <Table size="small">
                <StocksDataTableHead />
                <StocksDataTableBody data={data} />
            </Table>
        </TableContainer>
    )
}

export default StocksDataTable
