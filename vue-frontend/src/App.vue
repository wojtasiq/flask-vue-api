<template>
    <div id="app">
        <v-app>
            <v-container
                    class="v-container text-center"
                    fluid
            >
                <v-row>
                    <v-col>
                        <h1>Vue Frontend</h1>
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
    export default {
        name: 'app',
        created() {
            this.$vuetify.theme.dark = true
        },
    }
</script>

<style scoped>
    h1 {
        padding-top: 3rem;
    }
    .v-container {
        padding-left: 6rem;
        padding-right: 6rem;
    }
</style>
