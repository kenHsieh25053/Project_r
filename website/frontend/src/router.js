import Vue from 'vue'
import Router from 'vue-router'
import register from './views/accounts/Login.vue'
import logout from './views/accounts/Logout.vue'
import bookinfo from './views/bookshelf/Bookinfo.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/register',
            name: 'register',
            component: register,
            meta: {
                requireAuth: false
            }
        },
        {
            path: '/logout',
            name: 'logout',
            component: logout,
            meta: {
                requireAuth: false
            }
        },
        {
            path: '/bookinfo',
            name: 'bookinfo',
            components: bookinfo,
            meta: {
                requireAuth: true
            }
        }
    ]
})