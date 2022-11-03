import { Component, useState } from 'react'
import axios from "axios";
import AudioAnalyser from '../voice/AudioAnalyser'
import logo from '../../resources/logo2.svg';
import Waiting from '../text/Waiting';
import Notification from '../modal/Notification';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';

import './Home.css';

export default function Home() {

    const [audio, setAudio] = useState(null)
    const [access, setAccess] = useState(false)
    const {
        transcript,
        listening,
        resetTranscript,
        browserSupportsSpeechRecognition,
        isMicrophoneAvailable
      } = useSpeechRecognition();

    async function getMicrophone() {
        const audio = await navigator.mediaDevices.getUserMedia({
            audio: true,
            video: false
        });
        SpeechRecognition.startListening({ continuous: true })
        setAudio(audio)
    }

    function stopMicrophone() {
        SpeechRecognition.stopListening()
        audio.getTracks().forEach(track => track.stop());
        setAudio(null)
        resetTranscript()
    }

    function toggleMicrophone() {
        if (audio) {
          stopMicrophone();
        } else {
          getMicrophone();
        }
      }

    navigator.permissions.query({ name: 'microphone' }).then(function(permissionStatus){
        // granted, denied, prompt
        if(permissionStatus.state === 'granted'){
            console.log('sss')
            setAccess(true)
        }
    })

    if (!isMicrophoneAvailable) {
        return <span>Browser doesn't support speech recognition.</span>;
    }
    return (
        <div className="App">
            <Notification status={access}/>
            <img src={logo} className="App-logo" alt="logo" />
            {!audio && <Waiting/>}
            {audio ? <AudioAnalyser audio={audio} /> : ''}
            <p id='transcript'>{transcript}</p>          
            <div className="controls">
                <button onClick={toggleMicrophone}>
                {audio ? 'Stop microphone' : 'Get microphone input'}
                </button>
            </div>
        </div>
        );

}

