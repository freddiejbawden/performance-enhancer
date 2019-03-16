import React from 'react';
import {Show} from './shows.js'

export class SideBar extends React.Component {
    getShowList = () => {
        //Get shows
        var showList = []
        for (var i = 0; i < 3; i++) {
            var name = `Show ${i}`
            showList.push(<Show name={name}></Show>)
        }
        return showList
    }
    render() {
        return(
            <div class="sidebar-container">
                <h1>Logo</h1>
                {this.getShowList()}
            </div> 
        );
    }
}

