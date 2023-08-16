import './assets/style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')


const pinia = createPinia()
app.use(pinia)



// main.js

// import './assets/style.css'
// import { createApp } from 'vue'
// import { createPinia } from 'pinia'
// import App from './App.vue'
// import router from './router'

// const app = createApp(App)

//  Add an event listener for the beforeunload event
// window.addEventListener('beforeunload', handleBeforeUnload);

// function handleBeforeUnload(event) {
//   // Remove the user_id from localStorage when the window is about to unload (i.e., user closes the tab/window)
//   localStorage.removeItem('user_id');
//   // The following line is necessary to prevent the default "Are you sure you want to leave this page?" message in some browsers.
//   event.preventDefault();
//   // Remove the beforeunload event listener to avoid triggering it on page reload
//   window.removeEventListener('beforeunload', handleBeforeUnload);
// }

//  Add an event listener for the unload event
// window.addEventListener('unload', handleUnload);

// function handleUnload() {
//   This event will only be triggered when the page is being unloaded (not reloaded)
//   You can perform additional cleanup tasks here if needed.
// }

// app.use(router)

// app.mount('#app')

// const pinia = createPinia()
// app.use(pinia)
