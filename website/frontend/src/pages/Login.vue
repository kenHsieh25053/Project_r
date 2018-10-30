<template>
    <b-container fluid>   
        <b-row  align-h="center" align-v="center" id='loginPage'>
            <b-col cols="4">   
                <b-card header-tag="header" bg-variant="light">
                  <h2 slot='header' class="text-center">ReadLand</h2>
                    <b-alert show variant="warning" v-if='error'>{{ error }}</b-alert>  
                    <b-form v-if="show">
                        <b-form-group 
                        id="exampleInputGroup1" 
                        label="Email address:" 
                        label-for="exampleInput1" 
                        >
                            <b-form-input 
                            id="exampleInput1" 
                            type="email" 
                            v-model="form.email" 
                            required placeholder="Enter email">   
                            </b-form-input> 
                        </b-form-group>
                        <b-form-group 
                        id="ex" 
                        label="Username:" 
                        label-for="exa" 
                        >
                            <b-form-input 
                            id="e" 
                            type="text" 
                            v-model="form.username" 
                            required placeholder="Enter username">   
                            </b-form-input> 
                        </b-form-group>
                        <b-form-group 
                        id="exampleInputGroup2" 
                        label="Password:" 
                        label-for="exampleInput2">
                            <b-form-input 
                            id="exampleInput2" 
                            type="password" 
                            v-model="form.password" 
                            required placeholder="Enter password">
                            </b-form-input>
                        </b-form-group>
                        <b-button type="text" variant="primary" @click="logIn()">Login</b-button> 
                        <b-button type="text" variant="danger" @click="register()">Register</b-button>
                    </b-form>
                </b-card>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Login",

  data() {
    return {
      form: {
        email: "",
        username: "",
        password: ""
      },
      show: true,
      error: false
    };
  },
  computed: {
    ...mapGetters({ currentUser: "currentUser" })
  },
  created() {
    this.checkCurrentLogin();
  },
  updated() {
    this.checkCurrentLogin();
  },
  methods: {
    logIn() {
      this.$http
        .post("/auth/user/login/", {
          email: this.form.email,
          username: this.form.username,
          password: this.form.password
        })
        .then(request => this.loginSuccessful(request))
        .catch(() => this.loginFailed());
    },
    loginSuccessful(req) {
      if (!req.data.token) {
        this.loginFailed();
      }
      this.error = false;
      localStorage.token = req.data.token;
      this.$store.dispatch("login");
      this.$router.replace(this.$route.query.redirect || "/bookinfo");
    },
    loginFailed() {
      this.error = "Login Failed!";
      this.$store.dispatch("logout");
      delete localStorage.token;
    },
    checkCurrentLogin() {
      if (this.currentUser) {
        this.$router.replace(this.$route.query.redirect || "/bookinfo");
      }
    },
    register() {
      this.$router.push(this.$route.query.redirect || "/register");
    }
  }
};
</script>

<style>
#loginPage {
  z-index: 9999;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
}
</style>