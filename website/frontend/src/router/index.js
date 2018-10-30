import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/pages/Login'
import Bookinfo from '@/pages/Bookinfo'
import Register from '@/pages/Register'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [{
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/bookinfo',
            name: 'Bookinfo',
            component: Bookinfo,
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/register',
            name: 'Register',
            component: Register
        },
    ]
})

// router.beforeEach((to, from, next) => {
//     if (to.matched.some(record => record.meta.requiresAuth)) {
//         if (store.state.token) {
//             next();
//         } else {
//             next({
//                 path: '/login',
//             });
//         }
//     } else {
//         next();
//     }
// })

export default router