import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
// GET /api/things -> Array JSON
// 

class Light extends Component {
  constructor(props) {
    super(props)
    this.state = {
      switched: false,
      button_color: "#8e1818",
      text_color: "black"
    }
  }
  generateColor = () => {
    return '#' +  Math.random().toString(16).substr(-6);
  }
  toggleSwitch = () => {
    if (this.state.switched) {
      this.setState({button_color: '#8e1818', text_color: "black", switched: false})
    } else {
      this.setState({button_color: '#2ba551', text_color: "white", switched: true})
    }
    var url = `http://10.42.0.27:5000/api/things/${this.props.id}/on`
    axios.put(url, {
      on: !this.state.switched
    })
    .then(function (response) {
      console.log(response);
    })
  }
  componentDidMount() {
    this.toggleSwitch()
  }
  render() {
    
    return(
      <div class="thing" style={{backgroundColor:this.state.button_color}} onClick={this.toggleSwitch}>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style={{fill:this.state.text_color}}><path d="M19 6.734c0 4.164-3.75 6.98-3.75 10.266h-1.992c.001-2.079.997-3.826 1.968-5.513.912-1.585 1.774-3.083 1.774-4.753 0-3.108-2.517-4.734-5.004-4.734-2.483 0-4.996 1.626-4.996 4.734 0 1.67.862 3.168 1.774 4.753.971 1.687 1.966 3.434 1.967 5.513h-1.991c0-3.286-3.75-6.103-3.75-10.266 0-4.343 3.498-6.734 6.996-6.734 3.502 0 7.004 2.394 7.004 6.734zm-4 11.766c0 .276-.224.5-.5.5h-5c-.276 0-.5-.224-.5-.5s.224-.5.5-.5h5c.276 0 .5.224.5.5zm0 2c0 .276-.224.5-.5.5h-5c-.276 0-.5-.224-.5-.5s.224-.5.5-.5h5c.276 0 .5.224.5.5zm-1.701 3.159c-.19.216-.465.341-.753.341h-1.093c-.288 0-.562-.125-.752-.341l-1.451-1.659h5.5l-1.451 1.659z"/></svg>
        <h1 style={{color:this.state.text_color}}>{this.props.id}</h1>
      </div>
    )
  }
}
class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      things: []
    }
  }
  componentDidMount() {
    this.getThings()
  }
  getThings = () => {
    axios.get('http://10.42.0.27:5000/api/things')
    .then(response => {
      console.log(response)
      this.setState({things: response.data})
    })
   
  }

  render() {
   
    console.log(this.state.things)
    var thing_dom = []
    for(var i = 0; i < this.state.things.length; i++) {
      
      thing_dom.push(<Light id={this.state.things[i].id}></Light>)
    }
    return (
      <div class="app">
        <h1>Devices in Underbelly Theatre</h1>
         {thing_dom}
      </div>
     
    );
  }
}

export default App;
