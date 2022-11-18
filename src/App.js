import React from 'react'
import './App.css'
// import Page from './component/index'
// // import { useLoader } from '@react-three/fiber'
// // import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader'
// // import { Canvas } from '@react-three/fiber'
// // import { Environment, OrbitControls } from '@react-three/drei'

// // const Scene = () => {
// //   const fbx = useLoader(FBXLoader, 'NIVA.fbx')
// //   return <primitive object={fbx} />
// // }

// class App extends React.Component {
//   render () {
//     return(
//       <Page />
//     )
//   }
// }

// export default App

// import ''./styles.css'
import { Canvas } from '@react-three/fiber'
import { useLoader } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader'
import { Suspense } from 'react'
import { Environment } from '@react-three/drei'
// import axios from 'axios'
// import AudioAnalyser from '../voice/AudioAnalyser'
// import Notification from '../modal/Notification'
// import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
// import './component/homepage/Home.css'
// import Notification from './component/modal/Notification'
// import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
// import axios from 'axios'
// import AudioAnalyser from './component/voice/AudioAnalyser'

const Scene = () => {
  const fbx = useLoader(FBXLoader, 'NIVA.fbx')

  return <primitive object={fbx} scale={0.05} />
}

// const [audio, setAudio] = useState(null)
// const [access, setAccess] = useState(false)
// const [questionAudio, setQuestionAudio] = useState(null)

// const {
//   transcript,
//   resetTranscript
// } = useSpeechRecognition()

// function sendQuestion (question) {
//   axios.post('http://127.0.0.1:5000/profile', null, {
//     params: {
//       questionText: question
//     }
//   })
//     .then((response) => {
//       const res = response.data
//       console.log(res)
//       setQuestionAudio(res.questionText)
//     }).catch((error) => {
//       if (error.response) {
//         console.log(error.response)
//         console.log(error.response.status)
//         console.log(error.response.headers)
//       }
//     })
// }

// function checkPermissions () {
//   const permissions = navigator.mediaDevices.getUserMedia({audio: true, video: false})
//   permissions.then((stream) => {
//     setAccess(!access)
//   })
//     .catch((err) => {
//       setAccess(false)
//       console.log(`${err.name} : ${err.message}`)
//     })
// }

// async function getMicrophone () {
//   const audio = await navigator.mediaDevices.getUserMedia({
//     audio: true,
//     video: false
//   })
//   SpeechRecognition.startListening({ continuous: false })
//   setAudio(audio)
// }

// function stopMicrophone () {
//   SpeechRecognition.stopListening()
//   if(transcript !== null) {
//     sendQuestion(transcript)
//   }
//   audio.getTracks().forEach(track => track.stop())
//   setAudio(null)
//   setQuestionAudio(null)
// }

// function toggleMicrophone () {
//   resetTranscript()
//   if (audio) {
//     stopMicrophone()
//   } else {
//     getMicrophone()
//   }
// }

// checkPermissions()

export default function App () {
  return (
    <div>
      {/* <Notification isShowModal={access} askAccess={checkPermissions} />
      {!audio}
      {audio ? <AudioAnalyser audio={audio} /> : ''}
      <p id='transcript'>{transcript}</p>
      {questionAudio != null && <p id='transcript'>What I heard is: {questionAudio}</p>
      } */}
      <Canvas className="app-canvas">
        <Suspense fallback={null}>
          <Scene id='image' />
          <OrbitControls />
          <Environment background={true} preset={'apartment'} />
        </Suspense>
      </Canvas>
    </div>
  )
};
