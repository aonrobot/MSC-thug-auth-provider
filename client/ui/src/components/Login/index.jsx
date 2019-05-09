import React, { Component } from 'react';
import './style.css';

class Login extends Component {

    inputUser = React.createRef();
    inputPass = React.createRef();
    login = () => {
        let user = this.inputUser.current.value
        let pass = this.inputPass.current.value

        
    }
    render() {
        return (
            <div>
                <h1>Login Page</h1>
                Username : <input type="text" name="pwd" id="pwd" ref={this.inputUser}/>
                Password : <input type="text" name="usr" id="usr" ref={this.inputPass}/>
                <button onClick={() => this.login()}>Login</button>
            </div>
        )
    }
}

export default Login;