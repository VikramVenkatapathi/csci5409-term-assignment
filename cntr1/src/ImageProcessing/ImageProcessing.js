import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { FiUpload } from 'react-icons/fi';
import './ImageProcessing.css';
import analysisIcon from '../assets/analysis_icon.png'; // Update the file path accordingly

const ImageProcessing = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const email = queryParams.get('email');

  const ec2_ip = process.env.REACT_APP_API_URL;
  // const apiUrl = `http://44.202.61.56:5000`;
  const apiUrl = `http://${ec2_ip}:5000`;

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    setSelectedImage(file);
  };

  const handleImageProcessing = async () => {
    const formData = new FormData();
    formData.append('image', selectedImage);
    formData.append('email', email);

    try {
      const response = await fetch(`${apiUrl}/s3_upload`, {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        console.log('Image uploaded successfully');
        alert('Image analysis in progress... Check your email inbox for the results');
        // Handle success response here
      } else {
        console.error('Error uploading image');
        alert('Error uploading image');
        // Handle error response here
      }
    } catch (error) {
      console.error('Error uploading image:', error);
      alert('Error uploading image:', error);
      // Handle error here
    }
  };

  const handleLogout = () => {
    // Redirect to the logout page
    navigate('/login');
  };

  return (
    <div className="image-processing-page">
      <div className="logout-button" onClick={handleLogout}>
        Logout
      </div>
      <h2>Welcome, {email}</h2>
      <p>Select an image for processing:</p>
      <div className="upload-container">
        <input
          type="file"
          accept="image/*"
          onChange={handleImageUpload}
          className="upload-input"
          id="image-upload"
        />
        <label htmlFor="image-upload" className="upload-label">
          <FiUpload className="upload-icon" />
          Choose an Image
        </label>
      </div>
      {selectedImage && (
        <div className="selected-image-preview">
          <img src={URL.createObjectURL(selectedImage)} alt="Selected" />
        </div>
      )}
      {selectedImage && (
        <button className="analyze-button" onClick={handleImageProcessing}>
          <img src={analysisIcon} alt="Analysis Icon" className="analyze-icon" />
          <br />
          Analyze
        </button>
      )}
    </div>
  );
};

export default ImageProcessing;
