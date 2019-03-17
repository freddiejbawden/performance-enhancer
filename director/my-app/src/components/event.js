import React, { useState } from 'react';
import Dropdown from 'react-dropdown'

export class CreateActionPopUp extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            selected: "Light"
        }
        this.dropdown = React.createRef();
    }
    
    _onSelect = () => {
        this.setState({selected:this.dropdown.current.state.selected["label"]})
    }
    render() {
        var options = []
        console.log(this.state.selected)
        if (this.state.selected == "Light") {
            options.push(<div>Color Hex<input></input></div>)
        } else if (this.state.selected == "Sound") {
            options.push(<div>Sound File: <input id="sound-file" type="file" /></div>)
        } else if (this.state.selected == "Poll") {
            options.push(<div>
                <span>Option 1: <input></input></span>
                <span>Option 2: <input></input></span>
            </div>)
        }

        return(<div class="event-popup">
            <h2>Create Action</h2>
            <div class="dropdown-wrapper">
                <span>Action Type</span>
                <Dropdown
                    ref={this.dropdown}
                    className='spinner'
                    menuClassName='spinner-menu-item'
                    options={["Light","Sound","Poll"]} 
                    onChange={this._onSelect}
                    value={this.state.selected} 
                    placeholder="Select an option" />
            </div>
            {options}
            <div class="create-action"><span>Add</span></div>
        </div>)
    }
}

export class ActionList extends React.Component {
    constructor(props) {
        super(props)
        this.actions = []
        this.actionRefs = []
        for (var i = 0; i < 4; i++) {
            var n = `Light ${i}`
            this.actionRefs.push(React.createRef())
            this.actions.push(<Action name={n} color="green" time="10" ref={this.actionRefs[i]}></Action>)
        }
    }
    getEventJSON = () => {
        var event_json = []
        
        for(var i = 0; i < this.actionRefs.length; i++) {
            var id = `${this.props.name}_${i}`
            event_json.push({
                                "id":id,
                                "options":this.actionRefs[i].current.getOptions()
            })
        }
        return event_json
    }
   
    render() {
        return (
            <div>
                <h1>{this.props.name}</h1>
                {this.actions}
                <div class="add-button">Add Action</div>
            </div>
            )
    }
}

class Action extends React.Component {
    getOptions = () => {
        var options = {}
        if(this.props.color != "") {
            options["color"] = this.props.color
        }
        if(this.props.time != "") {
            options["time"] = parseInt(this.props.time)
        }
        return options
    }
    renderOptions = () => {
        var options_dict = this.getOptions()
        var options_span = []
        for(var option_key in options_dict) {
            options_span.push(<span class="option">{option_key}:{options_dict[option_key]}</span>)
        }
        return options_span
    }
    render() {
        return(<div class="action">
            <span>{this.props.name}</span>
            <div class="option-list">
                {this.renderOptions()}
            </div>
        </div>)
    }
}
