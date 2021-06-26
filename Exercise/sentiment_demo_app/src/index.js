import React from 'react'
import ReactDOM from 'react-dom'

import { Form, Input, Button } from 'antd';

import 'antd/dist/antd.css';
import './index.less'

class App extends React.Component {
  onFinish = () => {

  }

  onFinishFailed = () => {

  }


  render() {
    const layout = {
      labelCol: { span: 4 },
      wrapperCol: { span: 8 },
    }
    const offset_layout = {
      wrapperCol: {
        offset: 4,
        span: 4,
      }
    }

    return (
      <div className='main'>
          <Form {...layout} onFinish={this.onFinish} onFinishFailed={this.onFinishFailed}>
            <Form.Item name="review" label="Review" rules={[{required: true,}]}>
              <Input placeholder='This was an excellent experince!' />
            </Form.Item>

            <Form.Item {...offset_layout}>
              <Button type="primary" htmlType="submit">Submit</Button>
            </Form.Item>
          </Form>
      </div>
      )
  }
}

ReactDOM.render(<App />, document.getElementById('root'))
