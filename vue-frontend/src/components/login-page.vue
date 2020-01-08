<template>
    <v-col cols="5">
        <v-card class="elevation-12">
            <v-toolbar
                    color="primary"
                    flat
            >
                <v-toolbar-title>Login</v-toolbar-title>
                <v-spacer/>
            </v-toolbar>
            <v-card-text>
                <v-form @submit.prevent="login">
                    <v-text-field
                            label="Login"
                            v-model="username"
                            name="login"
                            prepend-icon="mdi-account-circle"
                            type="text"
                    />

                    <v-text-field
                            id="password"
                            v-model="password"
                            label="Password"
                            name="password"
                            prepend-icon="mdi-lock"
                            type="password"
                    />
                    <v-card-actions>
                        <v-spacer/>
                        <v-btn type="submit" color="primary" :loading="isAuthStatusLoading">Login</v-btn>
                    </v-card-actions>
                </v-form>
            </v-card-text>
        </v-card>
    </v-col>
</template>

<script>
    import store from "../store/store";

    export default {
        name: "login-page",
        data(){
            return {
                username : "",
                password : ""
            }
        },
        computed: {
          isAuthStatusLoading () {
              return store.getters.authStatus === 'loading';
          }
        },
        methods: {
            login: function () {
                let username = this.username
                let password = this.password
                this.$store.dispatch('login', { username, password })
                    .then(() => this.$router.push('/'))
                    .catch(err => window.console.log(err))
            }
        }
    }
</script>

