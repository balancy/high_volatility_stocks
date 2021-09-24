import { TableCell, tableCellClasses } from '@mui/material';

import styled from '@mui/material/styles/styled';

export const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
        backgroundColor: theme.palette.common.black,
        color: theme.palette.common.white,
    },
}));