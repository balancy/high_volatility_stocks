import { CircularProgress, Typography } from '@mui/material'

import AppRouter from '../routers/AppRouter'

const AppBody = ({ content }) => {
    return (
        <div>
            {content.isError &&
                <Typography variant="subtitle2" align="center">
                    Something went wrong during fetching...
                </Typography>
            }

            {content.isLoading
                ? <CircularProgress align="center" size="20%" />
                : <AppRouter data={content.data} />
            }
        </div>
    )
}

export default AppBody
