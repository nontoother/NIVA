import React, { useState } from 'react';
import ReactModal from 'react-modal';

const customStyles = {
  content: {
    top: '50%',
    left: '50%',
    right: 'auto',
    bottom: 'auto',
    marginRight: '-50%',
    transform: 'translate(-50%, -50%)',
  },
};


export default function Notification(props) {
    const [showModal, setShowModal] = useState(props.status)
    function openModal() {
        setShowModal(true)
    }
    function closeModal() {
        setShowModal(false)
    }
    return (
        <div>
            {/* <button onClick={openModal}>Trigger Modal</button> */}
            <ReactModal 
            isOpen={showModal}
            contentLabel="Minimal Modal Example"
            >
            <button onClick={closeModal}>Close Modal</button>
            </ReactModal>
        </div>
    );
}

