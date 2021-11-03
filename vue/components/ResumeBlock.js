app.component('resumeblock', {
    props: {
        show: {
            type: Boolean
        }
    },
    data() {
        return {
            name: 'Artem',
            lastName: 'Daniliants',
            description: 'web developer with no life',
            availableForWork: true,
            avatar: 'https://s.gravatar.com/avatar/9ea35b66e8191ba29adce17661bdecd3',
            avatarDesc: 'Artem Daniliants Photo',
            techStack: [{
                    id: 1,
                    tech: 'Python'
                },
                {
                    id: 2,
                    tech: 'Django'
                },
                {
                    id: 3,
                    tech: 'Tailwind CSS'
                },
                {
                    id: 4,
                    tech: 'Vue'
                }
            ]
        }
    },
    methods: {},
    computed: {
        generateDescription(){
            return this.avatarDesc.length > 0 ? this.avatarDesc: "Generated text"
        }
    },
    template: 
    /*html*/
    `
    <img v-if="show" style="border: 1px solid red;" :src="avatar" v-bind:alt="generateDescription" width="80" height="80">
        <br />
        My name is {{ name }} and I am a {{ description }}. Here is my tech stack:
        <ul>
            <li v-for="t in techStack" :key="t.id">{{t.tech}}</li>
        </ul>
        <p v-if="availableForWork">I am available for work! Send me an email!</p>
        <p v-else>I am not available for work!</p>

    `
})
