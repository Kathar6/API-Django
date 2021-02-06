import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// Components
import ListBook from '@/views/Books/ListBook'
import EditBook from '@/views/Books/EditBook'
import DeleteBook from '@/views/Books/DeleteBook'
import NewBook from '@/views/Books/NewBook'

const routes = [
  {
    path: "/books",
    name: "ListBook",
    component: ListBook
  },
  {
    path: "/books/:bookId/edit/",
    name: "EditBook",
    component: EditBook
  },
  {
    path: "/books/:bookId/delete",
    name: "DeleteBook",
    component: DeleteBook
  },
  {
    path: "/books/create",
    name: "NewBook",
    component: NewBook
  }
];


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
