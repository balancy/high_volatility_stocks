import React from 'react'
import { StyledTableRow } from './styles'
import { TableBody } from '@mui/material'
import TableField from './TableField'
import { table_fields } from '../../../constants'

const DataTableBody = ({ data }) =>
    <TableBody>
        {data.map((item) => (
            <StyledTableRow key={item.id}>
                {
                    table_fields.map((field) =>
                        <TableField
                            item={item}
                            field={field}
                            key={field.name}
                        />
                    )
                }
            </StyledTableRow>
        ))}
    </TableBody>

export default DataTableBody
