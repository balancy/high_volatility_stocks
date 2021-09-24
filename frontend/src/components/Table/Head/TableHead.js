import { TableHead as MaterialTableHead, TableRow } from '@mui/material'
import { tableHeaders } from '../../../constants/table'

import { StyledTableCell } from './TableHead.styles'

const TableHead = () =>
    <MaterialTableHead>
        <TableRow>
            {
                tableHeaders.map((item) =>
                    <StyledTableCell key={item}>
                        {item}
                    </StyledTableCell>
                )
            }
        </TableRow>
    </MaterialTableHead>

export default TableHead
