import React from 'react';
import { Button, Checkbox, Form, Input } from 'antd';
import { useState } from 'react';
import axios from 'axios';












const AuthForm = () => {


  const [email, setEmail] = useState('none')
  const [password, setPassword] = useState('none')



  
  const onFinish = (values) => {
    setEmail(values['email'])
    setPassword(values['password'])
    CheckUserAuth()
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };


  const [authstatus, setAuthstatus] = useState('Вы не авторизованы')
  const [AuthRequest, setAuthRequest] = useState(0)
  
  function CheckUserAuth() {
    const params = new URLSearchParams();
    params.append('username', email);
    params.append('password', password);
    console.log(email)
    console.log(password)
    axios.post(
      'http://127.0.0.1:8000/auth/jwt/login', 
      params
      ).then(
        r =>  {
          setAuthRequest(r.status)
        }
    )
    if (AuthRequest == 204){
      setAuthstatus('Вы успешно авторизовались')
    }
    
  
  }

  return(
    <div>
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
          value = {password}
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

  )
};
export default AuthForm;