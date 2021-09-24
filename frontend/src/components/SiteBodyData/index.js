import { Route, Switch } from 'react-router'

import React from 'react'
import StocksCharts from '../StocksCharts'
import StocksDataTable from '../StocksDataTable'

const SiteBodyData = ({ data }) => {
    return (
        <Switch>
            <Route exact path="/">
                <StocksDataTable data={data} />
            </Route>
            <Route exact path="/charts">
                <StocksCharts data={data} />
            </Route>
        </Switch>
    )
}

export default SiteBodyData
