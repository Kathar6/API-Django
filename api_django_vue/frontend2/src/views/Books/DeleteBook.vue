<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h3>Are you sure you want to delete this book?</h3>
                <p>Title : {{ this.element.title }}</p>
                <p>Description : {{ this.element.description }}</p>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <b-button @click="deleteBook" variant="danger">Delete</b-button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
    data(){
        return{
            bookId: this.$route.params.bookId,
            element: {
                title: '',
                description: ''
            }
        }
    },
    methods: {
        async deleteBook(){
            const path = `http://localhost:8081/api/v1.0/books/${this.bookId}/`
            try {
                let response = await axios.delete(path)
                console.log(response);
                location.href = '/books'
            } catch (error) {
                swal("Error!", "An error has been ocurred.", "error")
                console.log(error);
            }
        },
        async getBook (){
            const path = `http://localhost:8081/api/v1.0/books/${this.bookId}/`
            try {
                let response = await axios.get(path)
                this.element.title = response.data.title
                this.element.description = response.data.description
            } catch (error) {
                console.log(error);
            }
        }
    },
    created(){
        this.getBook()
    }
}
</script>

<style>

</style>