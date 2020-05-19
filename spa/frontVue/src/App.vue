<template>
    <div id="app">
        <header>
            <h1>Vue.js SPA</h1>
            My email <input v-model="email">
            <button @click="persist">Сохранить</button>
        </header>
        <main>
            <aside class="sidebar">
                Search <input v-model="searchParam"><br/>
                Date filter
                <select v-model="dateFilterParam">
                    <option value="">select option</option>
                    <option value="ld">Last day</option>
                    <option value="lw">Last week</option>
                    <option value="lm">Last month</option>
                </select>
                <ul>
                    <li><router-link
                                active-class="is-active"
                                class="link"
                                :to="{ name: 'event', params:{id:'create'}}">
                            new Event
                        </router-link></li>
                    <li v-for="event in events" class="line">
                        <router-link
                                active-class="is-active"
                                class="link"
                                :to="{ name: 'event', params:{id:event.url}}">
                            {{event.title}}
                        </router-link>
                        <button v-on:click="remove(event.url)">remove</button>
                    </li>
                </ul>
            </aside>
            <div class="content">
                <router-view></router-view>
            </div>
        </main>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                events: [],
                email: '',
                searchParam: '',
                dateFilterParam: '',
                endpoint: '/api/v1/events/',
            }
        },
        watch: {
            searchParam: function (val) {
                this.getAllevents();
            },
            dateFilterParam: function (val) {
                this.getAllevents();
            },
        },
        created() {
            document.addEventListener('eventsUpdated', this.getAllevents);
            if (localStorage.email) {
                this.email = localStorage.email;
                this.$cookie.set("email", this.email)
            }
            this.getAllevents();
        },
        methods: {
            persist() {
                localStorage.email = this.email;
                console.log(localStorage.email);
            },
            remove(id) {
                axios.delete(this.endpoint + id)
                    .then(response => {
                        this.getAllevents();
                        this.$router.push('home')
                    })
                    .catch(error => {
                        console.log('-----error-------');
                        console.log(error);
                    })
            },
            getAllevents() {
                console.log(this.dateFilterParam);
                axios.get(this.endpoint + `?search=${this.searchParam}&dateFilter=${this.dateFilterParam}`)
                    .then(response => {
                        console.log(response);
                        this.events = response.data;
                    })
                    .catch(error => {
                        console.log('-----error-------');
                        console.log(error);
                    })
            }
        }
    }
</script>

<style lang="scss">

    body {
        margin: 0;
        padding: 0;
    }

    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
    }

    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    li.line {
        display: flex;
    }

    header {
        position: fixed;
        top: 0;
        width: 100%;
        min-height: 90px;
        border-bottom: 1px solid #42b983;
        text-align: center;
        background: #ffffff;
    }

    main {
        display: flex;
        height: calc(100vh - 90px);
        max-width: 1200px;
        margin-top: 90px;
        margin-left: auto;
        margin-right: auto;
        overflow: hidden;
    }

    aside {
        flex: 1 0 30%;
        height: 100%;
        overflow-y: auto;
        width: 30%;
        padding: 50px 30px;
        box-sizing: border-box;
        border-right: 1px solid #42b983;
    }

    .content {
        flex: 1 1 70%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .link {
        display: block;
        text-decoration: none;
        margin-bottom: 10px;
        color: #2c3e50;

        &--home {
            text-transform: uppercase;
            margin-bottom: 30px;
        }

        &.is-active {
            color: #42b983;
        }
    }
</style>
