
<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mx-auto h-10 w-auto">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5" />
        </svg>
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Create your UCHA account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form @submit.prevent="submitForm" class="space-y-6">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" v-model="email" type="email" autocomplete="email" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          </div>
        </div>

        <div>
          <label for="deposit_number" class="block text-sm font-medium leading-6 text-gray-900">Deposit Number</label>
          <div class="mt-2">
            <input id="deposit_number" name="deposit_number" type="number" v-model="deposit_number" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
          </div>
          <div class="mt-2">
            <input id="password" name="password" type="password" v-model="password" autocomplete="current-password" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="confirm_password" class="block text-sm font-medium leading-6 text-gray-900">Confirm Password</label>
          </div>
          <div class="mt-2">
            <input id="confirm_password" name="confirm_password" type="password" v-model="confirm_password" autocomplete="current-password" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-green-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Create Account</button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-500">
        Already have an account?
        {{ ' ' }}
        <router-link to="/login" class="font-semibold leading-6 text-green-600 hover:text-green-500">Log In</router-link>
      </p>

      <br>
      <br>
      <div v-if="errors.length" class="rounded-md bg-red-50 p-4">
        <div class="flex">
          <div class="flex-shrink-0">
            <XCircleIcon class="h-5 w-5 text-red-400" aria-hidden="true" />
          </div>
          <div class="ml-3">
            <h3 class="text-sm font-medium text-red-800">There were {{ errors.length }} errors with your submission</h3>
            <div class="mt-2 text-sm text-red-700">
              <ul role="list" class="list-disc space-y-1 pl-5">
                <li v-for="error in errors" :key="error">{{ error }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'SignUp',
  data() {
    return {
      email: '',
      deposit_number: '',
      password: '',
      confirm_password: '',
      errors: []
    }
  },
  methods: {
    submitForm(){
      this.errors = []

      if (this.email === '') {
          this.errors.push('The email is missing')
      }

      if (!(/^\d{5}$/.test(this.deposit_number))){
          this.errors.push('Please enter a five digit depost number')
      }

      if (this.password === '') {
          this.errors.push('The password is too short')
      }

      if (this.password !== this.confirm_password) {
          this.errors.push('The passwords do not match')
      }

      if (!this.errors.length) {
        const formData = {
          email: this.email,
          password: this.password,
          deposit_number: this.deposit_number
        }
        axios
          .post("http://localhost:8000/accounts/register/", formData)
          .then(response => {
            this.$router.push('/login')
            console.log(response.data)
          })
          .catch(error =>{
            if (error.response){
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again")
              console.log(JSON.stringify(error))
            }
          })

      }

    }
  }
}
</script>

<script setup>
import { XCircleIcon } from '@heroicons/vue/20/solid'
</script>