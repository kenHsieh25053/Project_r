<template>
<b-container>
  <b-row align-h="center" align-v="center">
    <b-col cols="8">
      <b-card header-tag="header" bg-variant="light">
        <h2 slot='header' class="text-center">Sign up</h2>
      <b-form  @reset="onReset" v-if="show">
        <b-form-group 
            label="Email*"
            label-for="nestedEmail">
          <b-form-input 
            id="nestedEmail" 
            type='email'
            v-model="form.essential.email"
            required
            placeholder="Enter email">
          </b-form-input>
        </b-form-group>
        <b-form-group 
            label="Username*"
            label-for="nestedUsername">
          <b-form-input 
          id="nestedUsername" 
          type='text'
          required
          v-model="form.essential.username"
          placeholder="Enter username">
          </b-form-input>
        </b-form-group>
        <b-form-group 
            label="Password*"
            label-for="nestedPassword">
          <b-form-input 
          id="nestedPassword" 
          type='password'
          required
          v-model="form.essential.password"
          placeholder="Enter password">
          </b-form-input>
        </b-form-group>
        <b-form-group 
            label="Birthday"
            label-for="nestedBirthday">
          <b-form-input 
          id="nestedBirthday" 
          type='date'
          v-model="form.birthday">
          </b-form-input>
        </b-form-group>
        <b-form-group 
            label="Location"
            label-for="nestedLocation">
          <b-form-input 
          id="nestedLocation" 
          type='text'
          v-model="form.location"
          placeholder="Where you are?">
          </b-form-input>
        </b-form-group>
        <b-form-group 
            label="Gender"
            class="mb-0">
          <b-form-radio-group
          @change="result()"
          :options="form.gender.options" 
          v-model="form.gender.result"/>
        </b-form-group>
          <b-form-group 
            class="pt-2"
            label="About"
            label-for="nestedtextarea">
          <b-form-textarea 
            id="textarea1"
            v-model="form.about"
            placeholder="Introduce yourself"
            :rows="4"
            :max-rows="6">
          </b-form-textarea>
        </b-form-group>
        <b-button 
        type="submit" 
        variant="success" 
        @click="submit()">
        Submit
        </b-button>
        <b-button 
        type="reset" 
        variant="danger">Reset</b-button>
      </b-form>
    </b-card>
    </b-col>
  </b-row>
</b-container>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      form: {
        essential: {
          email: "",
          username: "",
          password: ""
        },
        birthday: "",
        location: "",
        gender: {
          selected: "Male",
          options: [
            { text: "男", value: "Male" },
            { text: "女", value: "Female" }
          ],
          result: ""
        },
        about: ""
      },
      show: true
    };
  },
  methods: {
    result: function(arg) {
      return console.log(arg);
    },
    onReset(evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.form.essential.email = "";
      this.form.essential.username = "";
      this.form.essential.password = "";
      this.form.birthday = "";
      this.form.location = "";
      this.form.gender.selected = "Male";
      this.form.file = "";
      this.form.text = "";
      /* Trick to reset/clear native browser form validation state */
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    submit() {
      if (this.form.essential != null) {
        this.$http
          .post("/auth/user/create/", {
            email: this.form.essential.email,
            username: this.form.essential.username,
            password: this.form.essential.password,
            birthday: this.form.birthday,
            location: this.form.location,
            gender: this.form.gender.result,
            about: this.form.about
          })
          .then(this.$router.replace(this.$route.query.redirect || "/login"));
      } else {
        alert("Please Enter essential info!");
      }
    }
  }
};
</script>

<style>
</style>