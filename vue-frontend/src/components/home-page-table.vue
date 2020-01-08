<template>
    <v-simple-table height="36rem" fixed-header>
        <thead>
        <tr>
            <th class="text-center">Number</th>
            <th class="text-center">Date and time</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(item, index) in tableData" :key="item.date">
            <td>{{ index+1 }}</td>
            <td>{{ item.date.slice(0,16) }}</td>
        </tr>
        </tbody>
    </v-simple-table>
</template>

<script>
    export default {
        name: "home-page-table",
        data() {
            return {
                tableData: null
            }
        },
        created() {
            this.getTableData()
        },
        methods: {
            getTableData: function () {
                return new Promise((resolve, reject) => {
                    this.$http.get('http://127.0.0.1:5000/auth/user/login_history',
                        {headers: {'content-type': 'application/json'}},
                    )
                        .then(resp => {
                            window.console.log(resp)
                            this.tableData = resp.data.loginDates.reverse()
                            resolve(resp)
                        })
                        .catch(err => {
                            reject(err)
                        })
                })
            }
        }
    }

</script>

