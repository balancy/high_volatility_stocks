import { TableCell, tableCellClasses } from '@mui/material';

import styled from '@mui/material/styles/styled';

export const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.body}`]: {
        fontSize: 13,
        borderLeft: "1px solid rgba(224, 224, 224, 1)"
    },
}));
