import React from 'react';
import ReactDOM from 'react-dom';
import './css/index.css';
import {SideBar} from  './components/static.js'
import {EventList} from  './components/shows.js'
import {ActionList, CreateActionPopUp} from './components/event.js'



class App extends React.Component {
    constructor() {
        super();
        this.state = {
          event: false,
          show: true
        };
        this.page = React.createRef()
        this.actions = React.createRef()
    }
    getContent = () => {
        console.log(this.state.show)
       
    }
    handleClick = () => {
        if (this.state.show) {
            this.setState({ show : false, event: true});
            this.page.current.setEvent()
        } else {
            // we are in actions 
            console.log(this.actions.current.getEventJSON())
            this.setState({show: true, event:false})
            this.page.current.setShow()
        }       
    }
    render() {
        let content; 
        if (this.state.show) {
            content = (<EventList></EventList>)
        } else {
           content = (<ActionList ref={this.actions}  name="test"></ActionList>)
        }
        var button_class = "make-event" + (this.state.show ? " make-event-green" : " make-event-red")
        var button_text = this.state.show ? "New Event" : "Done"
        return (
            <div class="container"> 
                <div class={button_class} onClick={this.handleClick}>
                   <span>{button_text}</span>
                </div>
                <div class="page"> 
                    <SideBar ref={this.page}></SideBar>
                    {content}
                </div>
                <CreateActionPopUp></CreateActionPopUp>
            </div>
        )
    }
}

const app = <App />;
ReactDOM.render(
    app,
    document.getElementById('root')
);
