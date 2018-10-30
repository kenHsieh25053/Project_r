<template>
    <div id='bg'>
        <navbar></navbar>
        <br>
        <b-container >
            <b-row align-h="between">
                <b-col cols='4' align-self="center">
                    <h1>
                        Start to explore book's world today!
                    </h1>    
                </b-col>
                <b-col cols='4' align-self="center">
                    <b-card>
                        <registerForm></registerForm>
                    </b-card>                    
                </b-col>
            </b-row>
        </b-container>
        <br>
        <bottom></bottom>
    </div>
</template>

<script>
import navbar from "@/components/header/Navbar";
import registerForm from "@/components/general/RegisterForm";
import bottom from "@/components/footer/Bottom";

export default {
  name: "register",
  components: {
    navbar,
    registerForm,
    bottom
  }
};
</script>

<style>
#bg {
  background-color: whitesmoke;
  background-size: 100%;
}
</style>