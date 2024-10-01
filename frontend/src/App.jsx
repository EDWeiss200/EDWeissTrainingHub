
import './index.css'
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import MostLikedWorkout from './pages/MostLikedWorkout'
import Auth from './pages/Auth'

function App() {


  return (
    <BrowserRouter>
      <Routes>
        <Route path='/mostlikedworkout' element={<MostLikedWorkout/>}/>
        <Route path='/' element={<MostLikedWorkout/>}/>
        <Route path='/auth' element={<Auth/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
