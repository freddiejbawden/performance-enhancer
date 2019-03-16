import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {SideBar} from  './static.js'
import {EventList} from  './shows.js'




class App extends React.Component {
    constructor() {
        super();
        this.state = {
          event: false,
          show: true
        }
    }
    getContent = () => {
        console.log(this.state.show)
       
    }
    handleClick = () => {
        if (this.state.show) {
            this.setState({ show : false, event: true});
        } else {
            this.setState({show: true, event:false})
        }
        
    }
    render() {
        let content; 
        if (this.state.show) {
            content = (<EventList></EventList>)
        } else {
           content = (<h1>hello</h1>)
        }
        var button_class = "make-event" + (this.state.show ? " make-event-green" : " make-event-red")
        var button_text = this.state.show ? "New Event" : "Done"
        return (
            <div class="container"> 
                <div class={button_class} onClick={this.handleClick}>
                   <span>{button_text}</span>
                </div>
                <div class="page"> 
                    <SideBar></SideBar>
                    {content}
                </div>
            </div>
        )
    }
}

const app = <App />;
ReactDOM.render(
    app,
    document.getElementById('root')
);
