<template>
    <v-container>
        <v-row>
            <v-col cols="4">
                <v-label>Username: </v-label>
                <v-text-field class="centered-input" solo disabled color="primary" :loading="isLoadingUserData" :value="getUserUsername"/>
            </v-col>
            <v-col cols="4">
                <v-label>Name: </v-label>
                <v-text-field class="centered-input" solo disabled color="primary" :loading="isLoadingUserData" :value="getUserName"/>
            </v-col>
            <v-col cols="4">
                <v-label>Surname: </v-label>
                <v-text-field class="centered-input" solo disabled color="primary" :loading="isLoadingUserData" :value="getUserSurname"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <home-page-table/>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import store from "../store/store";
    import HomePageTable from "./home-page-table"

    export default {
        name: "home-page",
        components: {
          HomePageTable
        },
        created() {
            this.$store.dispatch('userData')
        },
        computed: {
            isLoadingUserData(){
                return store.getters.userData === null;
            },
            getUserUsername(){
                return ((store.getters.userData !== null) ? store.getters.userData.username : null);
            },
            getUserName(){
                return ((store.getters.userData !== null) ? store.getters.userData.name : null);
            },
            getUserSurname(){
                return ((store.getters.userData !== null) ? store.getters.userData.surname : null);
            },
        }
    }
</script>

<style scoped>
    .centered-input >>> input {
        text-align: center
    }
</style>
