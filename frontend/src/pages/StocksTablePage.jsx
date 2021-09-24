import Paper from '@mui/material/Paper'
import Table from '@mui/material/Table'
import TableContainer from '@mui/material/TableContainer'
import TableHead from '../components/Table/Head/TableHead'
import TableBody from '../components/Table/Body/TableBody'


const StocksTablePage = ({ data }) => {
    return (
        <TableContainer component={Paper}>
            <Table size="small">
                <TableHead />
                <TableBody data={data} />
            </Table>
        </TableContainer>
    )
}

export default StocksTablePage
