<template>
    <v-col cols="8">
        <v-simple-table>
            <template v-slot:default>
                <thead>
                <tr>
                    <th class="text-center">Number</th>
                    <th class="text-center">Date</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(item, index) in desserts" :key="item.name">
                    <td>{{ index+1 }}</td>
                    <td>{{ item.name }}</td>
                </tr>
                </tbody>
            </template>
        </v-simple-table>
    </v-col>
</template>

<script>
    export default {
        data() {
            return {
                desserts: [
                    {
                        name: 'date 1',
                    },
                    {
                        name: 'date 2',
                    },
                    {
                        name: 'date 3',
                    },
                ],
            }
        },
    }
</script>
