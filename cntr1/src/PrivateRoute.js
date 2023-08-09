import React, { useContext } from 'react';
import { Route, useNavigate } from 'react-router-dom';
import { AuthContext } from './AuthContext';

const PrivateRoute = ({ component: Component, ...rest }) => {
  const { isAuthenticated } = useContext(AuthContext);
  const navigate = useNavigate();

  if (!isAuthenticated) {
    navigate('/login');
    return null;
  }

  return <Route {...rest} element={<Component />} />;
};

export default PrivateRoute;
