import axios from 'axios'

export const api = axios.create({
  baseURL:"http://127.0.0.1:8000/api/v1/"
})

export const createATask = async(e, taskTitle)=>{
  e.preventDefault()
  let response = await api.post("tasks/", {
    'title':taskTitle
  })
  if (response.status === 201){
    return response.data
  }
  else{
    alert(response.data)
  }
}