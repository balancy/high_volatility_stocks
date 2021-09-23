import React from 'react'

const List = ({ data }) =>
    data.map((item) => {
        return (
            <p key={item.id}>{item.company}</p>
        )
    })

export default List
