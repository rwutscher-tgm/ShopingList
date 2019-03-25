<template>
  <div class="home">
    <div>
      <h2>CREATE</h2>
      <input type="text" placeholder="Task" v-model="newTask">
      <input type="button" v-on:click="createTodo" value="send" name="" id="">
    </div>
    <div>
      <h2>DELETE</h2>
      <input type="text" placeholder="TaskId" v-model="delTask">
      <input type="button" v-on:click="deleteTodo" value="send" name="" id="">
    </div>
    <div>
      <h2>UPDATE</h2>
      <input type="text" placeholder="TaskId" v-model="updTaskId">
      <input type="text" placeholder="Task name" v-model="updTaskName">

      <input type="button" v-on:click="updateTodo" value="send" name="" id="">
    </div>
    <ul>
      <li v-for="(element, index) in data" v-bind:key="index">
          {{ index }}: {{ element.task }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'home',
  data(){
    return {
      data: null,
      newTask: null,
      delTask: null,
      updTaskId: null,
      updTaskName: null
    }
  },
  methods:{
    listTodos(){
      axios.get('http://127.0.0.1:5000/todos').then(res=>{
        this.data = res.data
      })
    },
    createTodo(){
      axios.post('http://127.0.0.1:5000/todos',{
        task: this.newTask
      })
      .then(res=>{
        this.listTodos()
      })
    },
    deleteTodo(){
      axios.delete('http://127.0.0.1:5000/todos/'+this.delTask)
      .then(res=>{
        this.listTodos()
      })
    },
    updateTodo(){
      axios.put('http://127.0.0.1:5000/todos/'+this.updTaskId,{
        task: this.updTaskName
      })
      .then(res=>{
        this.listTodos()
      })
    }
  },
  created(){
    this.listTodos()
  }
}
</script>
