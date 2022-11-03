import React, { useState } from 'react'
import ReactModal from 'react-modal'
import './Notification.css'

export default function Notification (props) {
  const [showModal, setShowModal] = useState({...props.status})

  function closeModal () {
    setShowModal(false)
    props.askAccess()
  }

  return (
    <div>
      <ReactModal
        isOpen={showModal}
        className="Modal"
        overlayClassName="Overlay"
      >
        <p>Please allow the microphone access</p>
        <button onClick={closeModal}>Okay</button>
      </ReactModal>
    </div>
  )
}

