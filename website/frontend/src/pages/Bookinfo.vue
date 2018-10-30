<template>
<div>
  <Navbar></Navbar>
  <p>login success!</p>
</div>
</template>

<script>
import Navbar from "@/components/Navbar";
import { mapGetters } from "vuex";
export default {
  name: "Bookinfo",
  components: {
    Navbar
  },
  watch: {
    $router: " checkCurrentLogin"
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
    checkCurrentLogin() {
      if (!this.currentUser && this.$route.path !== "/login") {
        this.$router.push("/?redirect=" + this.$route.path);
      }
    }
  }
};
</script>

<style>
</style>