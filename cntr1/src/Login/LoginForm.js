import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './LoginForm.css';

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  
  // const apiUrl = `http://localhost:5000/login`;
  const ec2_ip = process.env.REACT_APP_API_URL;
  const apiUrl = `http://${ec2_ip}:5000/login`;
  
  console.log("apiUrl: ",apiUrl);
  const handleLogin = (event) => {
    event.preventDefault();
    (async () => {
    const loginData = {
      "Email" : email,
      "Password" : password
    };

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginData),
      });
  
      if (response.ok) {
        const responseData = await response.json();
        if (responseData.sns_topic_arn && responseData.subscription_arn) {
          // SNS topic and subscription created, prompt the user to check their email
          alert('Login successful! Please check your email and confirm the subscription.');
        } else {
          // Login successful without SNS topic and subscription
          alert('Login successful!');
        }
        navigate(`/imageProcessing?email=${email}`);

      } else {
        // Login failed, handle the error response
        console.error('Login failed. Invalid credentials');
        alert('Login failed. Invalid credentials!');
      }
    } catch (error) {
      console.error('Error occurred during login:', error);
    }
  
    // Clear the form fields after login
    setEmail('');
    setPassword('');
  })();
};

  return (
    <div className="login-form">
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <div className="form-field">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
          />
        </div>
        <div className="form-field">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
          />
        </div>
        <div className="form-field">
          <button type="submit">Login</button>
        </div>
        <div className="form-field">
          <Link to="/RegistrationForm">Haven't registered yet? Register</Link>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
