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
                <v-form>
                    <v-text-field
                            label="Login"
                            name="login"
                            prepend-icon="mdi-account-circle"
                            type="text"
                    />

                    <v-text-field
                            id="password"
                            label="Password"
                            name="password"
                            prepend-icon="mdi-lock"
                            type="password"
                    />
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-spacer/>
                <v-btn color="primary">Login</v-btn>
            </v-card-actions>
        </v-card>
    </v-col>
</template>

<script>
    export default {}
</script>

