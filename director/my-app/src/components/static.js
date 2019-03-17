import React from 'react';
import {Show} from './shows.js'
import {EventTile} from './event.js'
export class SideBar extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            show: true,
            event: false
        }
    }
    getShowList = () => {
        var showList = []
        for (var i = 0; i < 3; i++) {
            var name = `Show ${i}`
            showList.push(<Show name={name}></Show>)
        }
        return showList
    }
    getEventTiles = () => {
        
    }
    setShow = () => {
        this.setState({show: true, event:false})
    }
    setEvent = () => {
        this.setState({show: false, event:true})
    }
    render() {
        var content;
        if (this.state.show) {
            content = this.getShowList()
        } else {
            content = <h1>h</h1>
        }
        return(
            <div class="sidebar-container">
                <h1>Logo</h1>
                {content}
            </div> 
        );
    }
}

