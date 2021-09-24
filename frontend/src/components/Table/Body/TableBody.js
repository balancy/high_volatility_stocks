import { StyledTableRow } from './TableBody.styles'
import { TableBody as MaterialTableBody } from '@mui/material'
import { tableFields } from '../../../constants/table'
import TableCell from '../Cell/TableCell'


const TableBody = ({ data }) =>
    <MaterialTableBody>
        {data.map((item) => (
            <StyledTableRow key={item.id}>
                {
                    tableFields.map((field) =>
                        <TableCell
                            item={item}
                            field={field}
                            key={field.name}
                        />
                    )
                }
            </StyledTableRow>
        ))}
    </MaterialTableBody>

export default TableBody
