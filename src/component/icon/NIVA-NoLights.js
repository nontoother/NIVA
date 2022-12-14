/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
*/

import React from 'react'
import { useGLTF } from '@react-three/drei'

export function Model (props) {

  const { nodes, materials } = useGLTF('/NIVA-NoLights.gltf')

  return (
    <group {...props} dispose={null}>
      <mesh geometry={nodes.Icosphere.geometry} material={materials['Oil Slick']} />
    </group>
  )
}

useGLTF.preload('/NIVA-NoLights.gltf')
