<template>
<div id='bottom-bg'>
    <b-container>
        <b-row class="pt-5 d-flex align-items-center">    
            <b-col md="8" lg="8">    
                <p class="text-center text-md-left grey-text">&copy; 2018 Copyright: <a href="https://www.Readland.com">www.Readland.com</a></p>    
            </b-col>    
            <b-col md="4" lg="4" class="ml-lg-0">    
                <div class="text-center text-md-right">    
                    <ul class="list-unstyled list-inline">    
                        <li class="list-inline-item">    
                            <a class="btn-floating btn-sm rgba-white-slight mx-1">    
                                <v-icon name="fas-twitter" scale="2" />    
                            </a>    
                        </li>    
                        <li class="list-inline-item">    
                            <a class="btn-floating btn-sm rgba-white-slight mx-1">    
                                <v-icon name="info-circle" scale="2" />    
                            </a>    
                        </li>    
                        <li class="list-inline-item">    
                            <a class="btn-floating btn-sm rgba-white-slight mx-1">    
                                <v-icon name="info-circle" scale="2" />    
                            </a>    
                        </li>    
                        <li class="list-inline-item">    
                            <a class="btn-floating btn-sm rgba-white-slight mx-1">    
                                <v-icon name="info-circle" scale="2" />    
                            </a>    
                        </li>    
                    </ul>    
                </div>    
            </b-col>    
        </b-row>    
    </b-container>
</div>
</template>

<script>
export default {
  name: "bottom",
  components: {}
};
</script>

<style scoped>
#bottom-bg {
  background-color: #929fba;
}
</style>