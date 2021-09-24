import { Route, Switch } from 'react-router'

import ChartsPage from '../pages/ChartsPage'
import StocksTablePage from '../pages/StocksTablePage'

const AppRouter = ({ data }) => {
    return (
        <Switch>
            <Route exact path="/">
                <StocksTablePage data={data} />
            </Route>
            <Route exact path="/charts">
                <ChartsPage data={data} />
            </Route>
        </Switch>
    )
}

export default AppRouter
