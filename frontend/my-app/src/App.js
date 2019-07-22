import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class UsersComponent extends React.Component {    
  constructor(props) {
    super(props);
  }
    componentDidMount() {
        axios.get(`http://localhost:8000/movies/tags/`)
            .then(response => response.json())
            .then(json => this.setState({ users: json.data, done: true }))
    }    
    
    render() {   
        if(!this.state.done) {
            return (
                <div>
                    Users Loading 
                </div>
            )
        } else {
            return (
                <div>
                    Users: {this.state.tags}            
                </div>
            )
        }
    }
}

export default UsersComponent;
