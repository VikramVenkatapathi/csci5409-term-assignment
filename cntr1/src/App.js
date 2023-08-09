import './App.css';
import { Routes, Route } from 'react-router-dom';
import LoginPage from './Login/LoginForm';
import RegistrationForm from './Registration/RegistrationForm';
import SessionData from './SessionData/SessionData';
import ImageProcessing from './ImageProcessing/ImageProcessing';
import PrivateRoute from './PrivateRoute';

const App = () => {
  return (
    <div>
      {/* <Router> */}
      <Routes>
        <Route path="/" element={<RegistrationForm />} />
        <Route path="/RegistrationForm" element={<RegistrationForm />} />
        <Route path="/login" element={<LoginPage />} />
        {/* <Route path="/sessionData/:email" element={<SessionData />} /> */}
        <Route path="/imageProcessing" element={<ImageProcessing />} />
        {/* <Route
          path="/sessionData"
          element={
            <PrivateRoute component={SessionData} />
          }
        /> */}
      </Routes>
      {/* </Router> */}
    </div>
  );
};

export default App;