import { CircularProgress, Typography } from '@mui/material'

import React from 'react'
import SiteBodyData from '../SiteBodyData'

const SiteBody = ({ content }) => {
    return (
        <div>
            {content.isError &&
                <Typography variant="subtitle2" align="center">
                    Something went wrong during fetching...
                </Typography>
            }

            {content.isLoading
                ? <CircularProgress align="center" size="20%" />
                : <SiteBodyData data={content.data} />
            }
        </div>
    )
}

export default SiteBody
