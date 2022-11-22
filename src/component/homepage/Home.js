import React, { useState } from 'react'
import axios from 'axios'
import AudioAnalyser from '../voice/AudioAnalyser'
import responding from '../../resources/responding.svg'
import logo2 from '../../resources/NIVAlogo.svg'
import Notification from '../modal/Notification'
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
import './Home.css'
import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { Suspense } from 'react'
import { Environment } from '@react-three/drei'
import { Model } from '../../resources/NIVA'

export default function Home () {

  const [audio, setAudio] = useState(null)
  const [access, setAccess] = useState(false)
  const [questionAudio, setQuestionAudio] = useState(null)

  // function Model () {
  //   const { scene } = useGLTF('NIVA.gltf')
  //   return <primitive object={scene} />
  // }

  const {
    transcript,
    resetTranscript
  } = useSpeechRecognition()

  const img0 = logo2
  const img1 = responding

  function sendQuestion (question) {
    axios.post('http://127.0.0.1:5000/profile', null, {
      params: {
        questionText: question
      }
    })
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
    const permissions = navigator.mediaDevices.getUserMedia({ audio: true, video: false })
    permissions.then((stream) => {
      setAccess(!access)
    })
      .catch((err) => {
        setAccess(false)
        console.log(`${err.name} : ${err.message}`)
      })
  }

  async function getMicrophone () {
    var img = document.getElementById('image')
    const audio = await navigator.mediaDevices.getUserMedia({
      audio: true,
      video: false
    })
    SpeechRecognition.startListening({ continuous: false })
    setAudio(audio)
    img.classList.add('App-logo-light')
  }

  function resetLogo () {
    var img = document.getElementById('image')
    img.src = img0
    img.classList.remove('App-logo-resp-gen')
    setTimeout(img.classList.add('App-logo-light'), 2000)
    setTimeout(img.classList.remove('App-logo-light'), 4000)
  }

  function stopMicrophone () {
    SpeechRecognition.stopListening()
    var img = document.getElementById('image')
    if (transcript !== null) {
      sendQuestion(transcript)
    }
    audio.getTracks().forEach(track => track.stop())
    setAudio(null)
    setQuestionAudio(null)
    img.classList.remove('App-logo-light')
    img.src = img1
    img.classList.add('App-logo-resp-gen')
    setTimeout(resetLogo, 3000)
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

  // model.then(object=>{
  //   App.add(object)
  //   let s = 0.5
  //   object.scale.set(s, s, s)
  // })

  return (
    <div className="App">
      <Canvas className="app-canvas" camera={{position: [0, -23, 30], fov: 5 }}>
        <Suspense fallback={null}>
          {/* <Scene id='image' onClick={toggleMicrophone}/> */}
          <pointLight position={[10, 10, 10]} intensity={1.3} />
          <OrbitControls />
          <Environment
            files="https://cdn.jsdelivr.net/gh/Sean-Bradley/React-Three-Fiber-Boilerplate@environment/public/img/venice_sunset_1k.hdr"
            background
            blur={0.5}
          />
          <directionalLight position={[3.3, 1.0, 4.4]} />
          <Model onClick={toggleMicrophone}/>
        </Suspense>
      </Canvas>
      <Notification isShowModal={access} askAccess={checkPermissions} />
      {!audio}
      {audio ? <AudioAnalyser audio={audio} /> : ''}
      <p id='transcript'>{transcript}</p>
      {/* <div className="controls">
      <button id = "imageButton" className="App-logo"> <img id = "image" src ={img0} onClick={toggleMicrophone}/>
      </button>
    </div> */}
      {questionAudio != null && <p id='transcript'>What I heard is: {questionAudio}</p>
      }
    </div>

  )

}

