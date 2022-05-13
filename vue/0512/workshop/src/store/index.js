import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import createPersistedState from 'vuex-persistedstate'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: [],
  },
  getters: {
    completedTodosCount({ todos }) {
      return todos.filter(todo => {
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodosCount({ todos }) {
      return todos.filter(todo => {
        return todo.isCompleted === false
      }).length
    }
  },
  mutations: {
    CREATE_TODO({ todos }, todoItem) {
      todos.push(todoItem)
    },
    DELETE_TODO({ todos }, todoItem) {
      const idx = todos.indexOf(todoItem)
      todos.splice(idx, 1)
    },
    UPDATE_TODO(state, todoItem) {
      state.todos = state.todos.map(todo => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
          }
          return todo
      })
    }
  },
  actions: {
    createTodo({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodo({ commit }, todoItem) {
      commit('UPDATE_TODO', todoItem)
    }
  }
})
