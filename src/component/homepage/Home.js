import React, { useState } from 'react'
import axios from 'axios'
import AudioAnalyser from '../voice/AudioAnalyser'
import logo from '../../resources/logo2.svg'
import Waiting from '../text/Waiting'
import Notification from '../modal/Notification'
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
import './Home.css'

export default function Home () {

  const [audio, setAudio] = useState(null)
  const [access, setAccess] = useState(false)
  const [questionAudio, setQuestionAudio] = useState(null)

  const {
    transcript,
    resetTranscript
  } = useSpeechRecognition()

  function sendQuestion (question) {
    axios.post('http://127.0.0.1:5000/profile', null, { params: {
      questionText: question
    }})
      .then((response) => {
        const res = response.data
        console.log(res)
        setQuestionAudio(res.questionText)
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
        }
      })
  }

  function checkPermissions () {
    const permissions = navigator.mediaDevices.getUserMedia({audio: true, video: false})
    permissions.then((stream) => {
      setAccess(!access)
    })
      .catch((err) => {
        setAccess(false)
        console.log(`${err.name} : ${err.message}`)
      })
  }

  async function getMicrophone () {
    const audio = await navigator.mediaDevices.getUserMedia({
      audio: true,
      video: false
    })
    SpeechRecognition.startListening({ continuous: false })
    setAudio(audio)
  }

  function stopMicrophone () {
    SpeechRecognition.stopListening()
    if(transcript !== null) {
      sendQuestion(transcript)
    }
    audio.getTracks().forEach(track => track.stop())
    setAudio(null)
    setQuestionAudio(null)
  }

  function toggleMicrophone () {
    resetTranscript()
    if (audio) {
      stopMicrophone()
    } else {
      getMicrophone()
    }
  }

  checkPermissions()

  return (
    <div className="App">
      <Notification isShowModal={access} askAccess={checkPermissions}/>
      <img src={logo} className="App-logo" alt="logo" />
      {!audio && <Waiting/>}
      {audio ? <AudioAnalyser audio={audio} /> : ''}
      <p id='transcript'>{transcript}</p>
      <div className="controls">
        <button onClick={toggleMicrophone}>
          {audio ? 'Stop' : 'Start Talking'}
        </button>
      </div>
      {questionAudio != null && <p id='transcript'>What I heard is: {questionAudio}</p>
      }
    </div>
  )

}

