import React from 'react';

export class Show extends React.Component {
    render() {
        return(
            <span>{this.props.name}</span>
        )
    }
}

class Event extends React.Component {
    render() {
        return(
            <div 
            class="event">
                <span>{this.props.eventname}</span>
                <span>{this.props.description}</span>
                <div class="event-edit"></div>
            </div>
        )
    }
}
export  class EventList extends React.Component {
    createEventList = () => {
        //TODO perform get request to server 
        var events = []
        for (var i = 0; i < 2; i++) {
            var name = `Option ${i}`
            var desc = `Cheese ${i}`
            events.push(<Event eventname={name} description={desc}></Event>)
        } 
        return events
    }
    render() {
        var show = "Freddie's Amazing Show"
        return(
            <div class="event-list">
                <h1>Events for {show}</h1>
                {this.createEventList()}
            </div>
            
        )
    }
}
