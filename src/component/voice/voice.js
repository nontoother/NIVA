import { Component, useState } from 'react'
import axios from "axios";
import AudioAnalyser from './AudioAnalyser';
import logo from '../../resources/logo2.svg';
import Waiting from '../text/Waiting';
import './voice.css';

export default class voice extends Component {
    constructor(props) {
        super(props);
        this.state = {
          audio: null,
          profileData: null
        };
        this.toggleMicrophone = this.toggleMicrophone.bind(this);
      }


    // API
    getData() {
      axios({
        method: "GET",
        url:"/profile",
      })
      .then((response) => {
        const res =response.data
        this.setState({profileData: {
          profile_name: res.name,
          about_me: res.about}})
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      })}
    

    async getMicrophone() {
        const audio = await navigator.mediaDevices.getUserMedia({
            audio: true,
            video: false
        });
        this.setState({ audio });
    }

    stopMicrophone() {
        this.state.audio.getTracks().forEach(track => track.stop());
        this.setState({ audio: null });
    }

    toggleMicrophone() {
        if (this.state.audio) {
          this.stopMicrophone();
        } else {
          this.getMicrophone();
        }
      }

    render() {
        return (
            <div className="App">
                <img src={logo} className="App-logo" alt="logo" />
                {!this.state.audio && <Waiting/>}
                <div className="controls">
                    <button onClick={this.toggleMicrophone}>
                    {this.state.audio ? 'Stop microphone' : 'Get microphone input'}
                    </button>
                </div>
                {this.state.audio ? <AudioAnalyser audio={this.state.audio} /> : ''}

            </div>
          );
    }

}

