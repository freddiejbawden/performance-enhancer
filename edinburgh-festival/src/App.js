import React, { Component } from 'react';
import './App.css';


// Edit this list to show the different votes that can be made
// Assign each element in list to numerical id ({1,2,3,...} is probably easiest)

const list = [
  {
    id: 1,
    voteName: 'Great',
    votes: 0
  },
  {
    id: 2,
    voteName: 'Nope',
    votes: 0
  }
];

class App extends Component {

  state = {
    opts: []
  };

  componentDidMount() {
    this.setState({ opts: list });
  }

  handleEvent = voteId => {
    this.state.opts.map(opt => {
      if (opt.id === voteId) {
        opt.votes++
        this.setState({opts: [opt]});
        // server request :  I voted
        // console.log(this.state)
        var xhttp = new XMLHttpRequest();
        var url = ""; // add url here
        xhttp.open("POST", url, true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        // xhttp.send("fname=Henry&lname=Ford");
      } 
    });
  }


  render() {
      return this.state.opts.map(option => {
        if (option.votes > 0) {
          return <div className="App" key={option.voteName}>Thanks for voting!</div>; 
        } else {          
          return <Vote key={option.id} id={option.id} voteName={option.voteName} votes={option.votes} onVote={this.handleEvent} />;        
        }
      })
    }
}

class Vote extends Component {
  handleClick = () => this.props.onVote(this.props.id);

  render() {
    return <div className="App">
    <button key={this.props.voteName} onClick={this.handleClick}>{this.props.voteName}</button></div>;
  }
}


export default App;
