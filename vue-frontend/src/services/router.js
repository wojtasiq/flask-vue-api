import Vue from 'vue';
import Router from 'vue-router';
import HomePage from "../components/HomePage";
import LoginPage from "../components/LoginPage";

Vue.use(Router);

export const router = new Router({
    mode: 'history',
    routes: [
        { path: '/', name: 'home', component: HomePage },
        { path: '/login', component: LoginPage },
        { path: '/*', redirect: '/' }
    ]
});

// router.beforeEach((to,from, next) => {
//     const loginPage = '/login'
//     const loggedIn = localStorage.getItem('user')
//
//     if(to.path !== loginPage && !loggedIn){
//         return next(loginPage)
//     }
// });

export default router
