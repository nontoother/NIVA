import React from 'react'
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

const Scene = () => {
  const fbx = useLoader(FBXLoader, 'NIVA.fbx')

  return <primitive object={fbx} scale={0.005} />
}

export default function App () {
  return (
    <div className="App">
      <Canvas>
        <Suspense fallback={null}>
          <Scene />
          <OrbitControls />
          {/* <Environment preset="sunset" background /> */}
        </Suspense>
      </Canvas>
    </div>
  )
};
