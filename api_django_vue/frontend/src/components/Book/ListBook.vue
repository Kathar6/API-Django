<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>List of books</h2>
                <div class="col-md-12">
                    <!-- Data table from bootstrap -->
                    <b-button variant="success" :to="{ name:'NewBook' }" class="mb-3">Create</b-button>
                    <b-table striped hover :items="books" :fields="fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" :to="{ name:'EditBook', params:{bookId: data.item.id} }">
                                Edit
                            </b-button>
                            <b-button size="sm" variant="danger" :to="{ name:'DeleteBook', params:{bookId: data.item.id} }">
                                Delete
                            </b-button>
                        </template>
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            // Sets the fields of the table
            fields: [
                { key: 'title', label: 'Title'},
                { key: 'description', label: 'Description'},
                { key: 'action', label: ''}
            ],
            // This array is going to fill up when we access to our API in django
            books: []
        }
    },
    methods: {
        // Method for call books from the API with the axios module
        getBooks(){
            const path = 'http://localhost:8000/api/v1.0/books/'
            axios.get(path)
            .then(response=>{
                this.books = response.data
            })
            .catch(err => {
                console.log(err);
            })
        }
    },
    // Execute a function after that the instance has been created
    created(){
        this.getBooks()
    }
}
</script>

<style>

</style>