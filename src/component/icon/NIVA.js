// /*
// Auto-generated by: https://github.com/pmndrs/gltfjsx
// */

// import React, { useRef, useState } from 'react'
// import { useGLTF } from '@react-three/drei'
// import { useFrame } from '@react-three/fiber'
// import './Status'
// import { NIVA_IDLE, NIVA_LISTENING, NIVA_PROCESSING, NIVA_SPEAKING } from './Status'

// export function Model (props) {

//   const group = useRef()

//   // const mesh = useRef()
//   const [status, setStatus] = useState(NIVA_IDLE)

//   let multiplier = 0.34
//   useFrame((state, delta) => {
//     if(status === NIVA_IDLE) {
//       multiplier = 0.34
//       group.current.rotation.x += multiplier * delta
//     } else if(status === NIVA_LISTENING) {
//       multiplier = 4
//       group.current.rotation.x += multiplier * delta
//     }
//   })

//   // const [active, setActive] = useState(false)
//   // const [colour, setColour] = useState('#ED91AD')

//   function ClickModel () {
//     props.toggleMicrophone()
//     changeState()
//   }

//   function changeState () {
//     if(status === NIVA_IDLE) {
//       setStatus(NIVA_LISTENING)
//     } else if(status === NIVA_LISTENING) {
//       setStatus(NIVA_PROCESSING)
//     } else if(status === NIVA_PROCESSING) {
//       setStatus(NIVA_SPEAKING)
//     } else {
//       setStatus(NIVA_IDLE)
//     }
//   }

//   return (
//     <group ref = {group} {...props} dispose={null}>
//       <mesh geometry={nodes.Icosphere.geometry} material={materials['Oil Slick']} onClick={ClickModel}/>
//       <mesh geometry={nodes.Plane.geometry} material={materials.Material} position={[-4.43, 0, 0]} rotation={[0, 0, -1.57]} scale={8.43} />
//     </group>
//   )
// }

// useGLTF.preload('/NIVA.gltf')
