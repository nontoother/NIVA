import { Component, useState } from 'react'
import AudioAnalyser from './AudioAnalyser';
import logo from '../../resources/logo.svg';
import './voice.css';

export default class voice extends Component {
    constructor(props) {
        super(props);
        this.state = {
          audio: null
        };
        this.toggleMicrophone = this.toggleMicrophone.bind(this);
      }

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
              <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                  NIVA is ready to start...
                </p>
                <div className="controls">
                    <button onClick={this.toggleMicrophone}>
                    {this.state.audio ? 'Stop microphone' : 'Get microphone input'}
                    </button>
                </div>
                {this.state.audio ? <AudioAnalyser audio={this.state.audio} /> : ''}

              </header>
            </div>
          );
    }

}

