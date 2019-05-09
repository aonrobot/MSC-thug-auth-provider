const express = require('express');
const path = require('path');

const axios = require('axios');

const app = express();

const PORT = 9000;
const CLIENT_ID = 'xOb8myo2EemTsbMNr1BXTT0KWNkoQ1f6';
const CLIENT_SECRET = 'T9H5WQl1bz7t5lbMS8BHdSWSyOwLrpSd';

const buildPath = path.resolve(__dirname, '..', 'ui', 'build')

app.use(express.static(buildPath));
app.use(express.urlencoded());
app.use(express.json());

app.post('/login', (req, res) => {
    let username = req.body.username;
    let password = req.body.password;

    let data = {
        username,
        password,
        client_id: CLIENT_ID,
        client_secret: CLIENT_SECRET
    }

    axios.post('http://127.0.0.1:8000/oauth/login', data).then((response) => {
        if (response.data.login) {
            let code = response.data.data.split('?code=')[1]

            let data = {
                client_id: CLIENT_ID,
                client_secret: CLIENT_SECRET,
                code
            }

            axios.post('http://127.0.0.1:8000/oauth/token', data).then((response) => {
                console.log('token ', response.data)
                res.json({'data': response.data.data})
            }).catch((e) => {
                console.log(e)
                res.json("Get token error")
            })
        } else {
            res.json({'message': 'Password wrong', 'data': undefined})
        }

    }).catch((e) => {
        res.json("Get code error")
    })
})

app.post('/oauth/refresh', (req, res) => {

    let refresh_token = req.body.refresh_token;

    let data = {
        client_id: CLIENT_ID,
        client_secret: CLIENT_SECRET,
        refresh_token
    }

    console.log(data)
    
    axios.post('http://127.0.0.1:8000/oauth/refresh', data).then((response) => {
        console.log('token ', response.data)
        if (response.data.data === undefined) {
            res.json({'data': response.data})
        } else {
            res.json({'data': response.data.data})
        }
    }).catch((e) => {
        console.log(e)
        res.json("Get token error")
    })
})

app.get('/oauth', (req, res) => {
    console.log(req.query.code)
    if(req.query.code === undefined) {
        
    } else {
        res.json({message: 'take code'})
    }
})

app.get('*', (req, res) => {
    res.sendFile(buildPath + '/index.html')
})

app.listen(PORT,'0.0.0.0', () => {
    console.log('client listen in port 9000')
})

