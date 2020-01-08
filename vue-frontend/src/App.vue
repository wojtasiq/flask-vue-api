<template>
    <div id="app">
        <v-app>
            <v-container class="v-container text-center" fluid>
                <v-row>
                    <v-col cols="3"/>
                    <v-col cols="6">
                        <h1>Vue Frontend</h1>
                    </v-col>
                    <v-col cols="3">
                        <v-btn v-if="authorized" v-on:click="logout" color="primary">
                            Logout
                        </v-btn>
                    </v-col>
                </v-row>
                <v-row align="center" justify="center" class="text-center">
                    <router-view/>
                </v-row>
            </v-container>
        </v-app>
    </div>
</template>

<script>
    import store from "./store/store";

    export default {
        name: 'app',
        created() {
            this.$vuetify.theme.dark = true
        },
        computed: {
            authorized () {
                return store.getters.isLoggedIn
            }
        },
        methods: {
            logout: function () {
                this.$store.dispatch('logout')
                    .then(() => this.$router.push('/login'))
                    .catch(err => window.console.log(err))
            }
        }
    }
</script>

<style scoped>
    .v-container {
        padding-top: 3rem;
        padding-left: 6rem;
        padding-right: 6rem;
    }
</style>
