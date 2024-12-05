import { useEffect, useState } from 'react'
import { api } from './utilities'
import './App.css'
import TaskForm from './components/TaskForm'

function App() {
  const [tasks, setTasks] = useState([])

  useEffect(()=>{
    const getTasks = async() => {
      let response = await api.get("tasks/")
      console.log(response.data)
      setTasks(response.data)
    }
    getTasks()
  }, [])

  return (
    <>
      <h1>Task Master</h1>
      <TaskForm tasks={tasks} setTasks={setTasks}/>
      <ul>
        {tasks.map((atask)=>(
          <li>{atask.title}</li>
        ))}
      </ul>
    </>
  )
}

export default App
