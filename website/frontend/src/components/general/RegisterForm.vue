<template>
<div>
    <b-button 
        class="my-2 my-sm-0" 
        type="submit"
        variant='primary'
        @click="FbLogin()">
        Sign up with Facebook Account
    </b-button>
    <h2 id='or'>or</h2>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="exampleInputGroup1"
                    label="Email address:"
                    label-for="exampleInput1">
        <b-form-input id="exampleInput1"
                      type="email"
                      v-model="register.email"
                      required
                      placeholder="Enter email">
        </b-form-input>
      </b-form-group>
      <b-form-group id="exampleInputGroup2"
                    label="Your Name:"
                    label-for="exampleInput2">
        <b-form-input id="exampleInput2"
                      type="text"
                      v-model="register.name"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      <b-form-group id="exampleInputGroup3"
                    label="Password:"
                    label-for="exampleInput3">
        <b-form-input id="exampleInput3"
                      type="text"
                      v-model="register.password"
                      required
                      placeholder="Enter Password">
        </b-form-input>
      </b-form-group>
    <b-form-group label="Gender">
      <b-form-radio-group v-model="register.selected"
                          :options="options"
                          name="radioInline">
      </b-form-radio-group>
    </b-form-group>
      <b-button type="submit" variant="success" @click="registerIt">Sign up now!</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "registerForm",
  data() {
    return {
      register: {
        email: "",
        name: "",
        password: "",
        checked: []
      },
      show: true,
      selected: "first",
      options: [
        { text: "Male", value: "male" },
        { text: "Female", value: "female" }
      ]
    };
  },
  methods: {
    registerIt() {
      axios
        .post("http://127.0.0.1:8000/auth/user/create/", this.register)
        .then(response => {
          let token = response.data.user.api_token;
          localStorage.setItem("token", token);
        });
    }
  }
};
</script>

<style>
#or {
  text-align: center;
}
</style>