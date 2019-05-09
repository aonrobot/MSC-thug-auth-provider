import React, { Component } from 'react';
import axios from 'axios'
import { Redirect } from 'react-router-dom';
import './style.css';

class Home extends Component {
  render() {
    let token = localStorage.getItem('fucking-token');
    if (token === null) {
      // Empty Token
      console.log('token empty')
      this.props.history.push('/login')
    } else {
      // Valid Token
      axios.get('http://172.16.6.74:8000/api').then((res) => {
        
      }).catch((error) => {
        if (error.response.status === 401) {
          console.log('token invalid')
          this.props.history.push('/login')
        }
      })
    }

    return (
      <div>
        <h1>Home Page</h1>
      </div>
    )
  }
}

export default Home;