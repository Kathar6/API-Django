<template>
    <div class="container">
        <div class="row">
            <!-- Page title -->
            <div class="col text-left">
                <h2>Edit Book</h2>
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
                                    <b-button type="submit" variant="primary">
                                        Edit
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
            evt.preventDefault()
            const path = `http://localhost:8000/api/v1.0/books/${this.bookId}/`
            try {
                let response = await axios.put(path, this.form)
                // alert("Book updated successfully")
                swal("Updated!", "The book has been update successfully", "success")
            } catch (error) {
                console.log(error);
            }
        },
        async getBook (){
            const path = `http://localhost:8000/api/v1.0/books/${this.bookId}/`
            try {
                let response = await axios.get(path)
                this.form.title = response.data.title
                this.form.description = response.data.description
            } catch (error) {
                console.log(error);
            }
        }
    },
    created(){
        this.getBook()
    }
};
</script>

<style>
</style>