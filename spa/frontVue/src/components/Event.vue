<template lang="html">
    <div class="event" v-if="event">
        <button v-on:click="changeState">{{state}}</button>
        <h1 class="event__title"><input v-if="state === 'save'" v-model="event.title"><span v-if="state === 'edit'">{{ event.title }}</span>
        </h1>
        <p class="event__date"><input v-if="state === 'save'" type="datetime-local" v-model="event.date"><span
                v-if="state === 'edit'">{{ event.date }}</span></p>
        <p class="event__body"><textarea v-if="state === 'save'" v-model="event.description"></textarea><span
                v-if="state === 'edit'">{{ event.description }}</span></p>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        props: ['id'],

        metaInfo() {
            return {
                title: this.event && this.event.title,
            };
        },

        data() {
            return {
                event: null,
                state: 'edit',
                endpoint: '/api/v1/events/',
            }
        },

        methods: {
            changeState() {
                if (this.state === 'edit') {
                    this.state = 'save';
                } else {
                    this.state = 'edit';
                    if (this.id === 'create') {
                        this.event.email = localStorage.getItem('email')
                        axios(
                            {
                                method: 'POST',
                                url: this.endpoint,
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                data: this.event
                            })
                            .then(response => {
                                this.event = response.data
                                this.$router.push({ name: 'event', params: { id: this.event.url } })
                                document.dispatchEvent(new Event('eventsUpdated'));

                            })
                            .catch(error => {
                                console.log('-----error-------');
                                console.log(error)
                            })
                    } else {
                        axios(
                            {
                                method: 'PATCH',
                                url: this.endpoint + this.event.url + '/',
                                headers: {
                                    "Content-Type": "application/json"
                                },
                                data: this.event
                            })
                            .then(response => {
                                this.event = response.data

                                document.dispatchEvent(new Event('eventsUpdated'));

                            })
                            .catch(error => {
                                console.log('-----error-------');
                                console.log(error)
                            })
                    }
                }
            },
            getevent(url) {
                axios(this.endpoint + url)
                    .then(response => {
                        console.log(response);
                        this.event = response.data
                    })
                    .catch(error => {
                        console.log('-----error-------');
                        console.log(error)
                    })
            }
        },

        created() {
            if (this.id === 'create') {
                this.state = 'save'
                this.event = {
                    title: '',
                    date: '',
                    description: '',
                }
            } else {
                this.getevent(this.id);
            }
        },

        watch: {
            '$route'() {
                if (this.id === 'create') {
                    this.state = 'save'
                    this.event = {
                        title: '',
                        date: '',
                        description: '',
                    }
                } else {
                    this.getevent(this.id);
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    .event {
        position: relative;
        max-width: 500px;
        margin: 0 auto;
        padding: 50px 20px 70px;

        &__title {
            position: relative;
            text-transform: uppercase;
            z-index: 1;
        }

        &__body {
            position: relative;
            z-index: 1;
        }

        &__id {
            position: absolute;
            font-size: 280px;
            bottom: -50px;
            margin: 0;
            color: #eeeeee;
            right: -20px;
            line-height: 1;
            font-weight: 900;
            z-index: 0;
        }
    }
</style>
