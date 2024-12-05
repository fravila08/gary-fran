import { useState } from "react";
import { createATask } from "../utilities";

const TaskForm = ({setTasks, tasks}) => {
  const [title, setTitle] = useState('')

  const handleSubmit = async(e)=>{
    let newTask = await createATask(e, title)
    setTasks([...tasks, newTask])
    setTitle('')
  }
  return(
    <form onSubmit={(e)=>handleSubmit(e)} >
      <input
        value={title}
        onChange={(e)=> setTitle(e.target.value)} 
        type="text" 
        placeholder="task title" 
      />
      <button type="submit">+</button>
    </form>
  )

}

export default TaskForm;