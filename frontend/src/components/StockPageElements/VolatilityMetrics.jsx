import { Paper, Table, TableCell, TableContainer, TableRow, TableBody } from '@mui/material';

import React from 'react'
import { useStyles } from './VolatilityMetrics.styles';

const VolatilityMetrics = ({ data }) => {
    const metrics = Object.keys(data)
    const values = Object.values(data)

    const styles = useStyles()

    return (
        <TableContainer component={Paper} className={styles.table}>
            <Table>
                <TableBody>
                    <TableRow>
                        {
                            metrics.map((metric) =>
                                <TableCell
                                    className={styles.tableHeader}
                                    key={metric}
                                >
                                    {metric}
                                </TableCell>
                            )
                        }
                    </TableRow>
                    <TableRow>
                        {
                            values.map((value) =>
                                <TableCell
                                    className={styles.tableBody}
                                >
                                    {
                                        value ? value : <span>null</span>
                                    }
                                </TableCell>
                            )
                        }
                    </TableRow>
                </TableBody>
            </Table>
        </TableContainer>
    )
}

export default VolatilityMetrics
