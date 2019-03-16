import React, { Component } from 'react';
import logo from './logo.svg';
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
    votes: []
  };

  componentDidMount() {
    this.setState({ votes: list });
  }
  handleEvent = voteId => {
    const updatedList = this.state.votes.map(vote => {
      if (vote.id === voteId) {
        return Object.assign({}, vote, {
          votes: vote.votes + 1
        });
      } else {
        return vote;
      }
    });
  
    this.setState({
      votes: updatedList
    });
  }


  render() {
    return this.state.votes.map(vote => (
      <Vote key={vote.id} id={vote.id} voteName={vote.voteName} votes={vote.votes} onVote={this.handleEvent} />
    ));
  }
}

class Vote extends Component {
  handleClick = () => this.props.onVote(this.props.id);

  render() {
    return <div className="App">{this.props.voteName}
    <button onClick={this.handleClick}>+</button>{this.props.votes}</div>;
  }
}

export default App;
