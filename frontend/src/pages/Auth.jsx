import React from 'react';
import { Button, Checkbox, Form, Input } from 'antd';
import { useState } from 'react';
import axios from 'axios';
import '../index.css'
import { redirect } from "react-router-dom"
import { useNavigate } from 'react-router-dom';




const Auth = () => {


  
  const onFinish = (values) => {
    CheckUserAuth(values['email'],values['password'])
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };


  const navigate = useNavigate();

  const redirect_home = () => {
    navigate('/')
  }

  

  const [authstatus, setAuthstatus] = useState(false)
  const [AuthRequest, setAuthRequest] = useState(0)
  
  function CheckUserAuth(email_user,password_user) {
    const params = new URLSearchParams();
    params.append('username', email_user);
    params.append('password', password_user);
    
    axios.post(
      'http://127.0.0.1:8000/auth/jwt/login', 
      params,
      { withCredentials: true }
      ).then(
        r =>  {
          if (r.status == 204){
            return(redirect_home())
          }
        }
      ).catch((error) => {
          alert('Неправильное имя пользователя или пароль')
        }
      )
    
    
  
  }

  return(
    <div className="container">
      <div className='auth-form'>
        <Form
          name="basic"
          labelCol={{
            span: 8,
          }}
          wrapperCol={{
            span: 16,
          }}
          style={{
            maxWidth: 600,
          }}
          initialValues={{
            remember: true,
          }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          autoComplete="off"
        >
          <Form.Item
            label="email"
            name="email"
            id='email'
            
            rules={[
              {
                required: true,
                message: 'Please input your email!',
              },
            
            ]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Password"
            name="password"
            id='password'
            rules={[
              {
                required: true,
                message: 'Please input your password!',
              },
            ]}
            
          >
            <Input.Password />
          </Form.Item>

          <Form.Item
            name="remember"
            valuePropName="checked"
            wrapperCol={{
              offset: 8,
              span: 16,
            }}
          >
            <Checkbox>Remember me</Checkbox>
          </Form.Item>

          <Form.Item
            wrapperCol={{
              offset: 8,
              span: 16,
            }}
          >
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
        <p>{authstatus}</p>
      </div>
    </div>

  )
};
export default Auth;