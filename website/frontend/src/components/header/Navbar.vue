<template>
<b-navbar toggleable="md" type="dark" variant="info" fixed>
  <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
  <b-navbar-brand href="#">ReadLand</b-navbar-brand>
  <b-collapse is-nav id="nav_collapse">
    <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">      
      <b-nav-form>
        <b-form-input 
        size="sm" 
        class="mr-sm-2"
        name='email' 
        type="text"
        v-model="credentials.email" 
        placeholder="email"
        required />
        <b-form-input 
        size="sm" 
        class="mr-sm-2" 
        name='password'
        type="text"
        v-model="credentials.password" 
        placeholder="password"
        required autofocus/>
        <b-button 
        size="sm" 
        class="my-2 my-sm-0" 
        type="submit"
        @click="login()">
        login
        </b-button>
      </b-nav-form>      
    </b-navbar-nav>    
    <b-dropdown variant="link" size="md" id="ddown-right" right no-caret>
    <template slot="button-content">
      <v-icon id='info' name="info-circle" scale="2"/>
    </template>
    <b-dropdown-item href="#">Forget Password?</b-dropdown-item>
    <b-dropdown-item href="#">more</b-dropdown-item>
  </b-dropdown>
  </b-collapse>
</b-navbar>
</template>

<script>
export default {
  name: "navbar",
  data() {
    return {
      email: "",
      password: ""
    };
  },
  methods: {
    login() {
      this.$http.plain.post("/register", {
        email: this.email,
        password: this.password
      });
      // .then(response => this.signinSuccessful(response))
      // .catch(error => this.signinFailed(error));
    }
  }
};
</script>

<style>
#info {
  color: rgb(255, 253, 253);
}
</style>