<template>
  <div>
      <input type="text"
      v-model.trim="todoTitle"
      @keyup.enter="createTodo"
      placeholder="할 일을 입력해주세요"
      >
  </div>
</template>

<script>
export default {
    data() {
        return {
            todoTitle: '',
        }
    },
    methods: {
        createTodo() {
            const todoItem = {
                title: this.todoTitle,
                isCompleted: false,
                date: new Date().getTime(),
            }
            if (todoItem.title) {
                this.$store.dispatch('createTodo', todoItem)
            }
            this.todoTitle = ''
        }
    }
}
</script>

<style>

</style>