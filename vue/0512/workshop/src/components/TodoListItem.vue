<template>
  <div>
    <span @click="updateTodo(todo)"
    :class="{'is-completed': todo.isCompleted}"
    >{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  props: {
    todo: Object,
  },
  methods: {
    ...mapActions(['deleteTodo', 'updateTodo']),
  }
}
</script>

<style scoped>
.is-completed {
  text-decoration: line-through;
}

div {
  border: 2px solid black;
  margin: 2px;
  padding: 2px;
}

span {
  cursor: pointer;
}
</style>