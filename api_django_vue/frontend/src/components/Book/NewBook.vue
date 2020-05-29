<template>
    <div class="container">
        <div class="row">
            <!-- Page title -->
            <div class="col text-left">
                <h2>New Book</h2>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <!-- Form to edit the book -->
                        <form @submit="onSubmit">
                            <div class="form-group row">
                                <label for="title" class="col-form-label">Title</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Title" name="title" class="form-control" v-model.trim="form.title">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="description" class="col-form-label">Description</label>
                                <div class="col-sm-6">
                                    <textarea name="description" class="form-control" placeholder="Description" v-model.trim="form.description" rows="3">
                                    </textarea>
                                </div>
                            </div>
                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="success">
                                        Create
                                    </b-button> 
                                    <b-button type="submit" class="btn-large-space" :to="{ name:'ListBook' }">
                                        Cancel
                                    </b-button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
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
            form: {
                title: '',
                description: ''
            }
        }
    },
    methods: {
        async onSubmit(evt){
            // Prevent the submit redirection form
            evt.preventDefault()

            // Send a request to the API
            const path = `http://localhost:8000/api/v1.0/books/`
            try {
                let response = await axios.post(path, this.form)
                // alert("Book updated successfully")
                swal("Created!", "The new book has been created successfully", "success")
            } catch (error) {
                console.log(error);
            }
        }
    }
}
</script>

<style>

</style>