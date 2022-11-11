// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    app: {
        head: {
            charset: 'utf-16',
            viewport: 'width=500, initial-scale=1',
            title: 'Dexter McMillan / Portfolio',
            link: [
              { rel: "stylesheet", href: "https://use.typekit.net/azo6pea.css" }
            ]
          },
    },

    plugins: ['~/plugins/dates.js'],

    modules: [
        '@nuxtjs/tailwindcss',

    ],

    css: ['vuetify/lib/styles/main.sass'],

    build: {

        transpile: ['vuetify'],
        
    },

    vite: {

        define: {
            'process.env.DEBUG': false,
        },
        
    },
    

    
})
