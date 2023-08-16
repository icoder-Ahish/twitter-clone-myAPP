import {defineStore } from 'pinia'

export const useUserTokenStore = defineStore ("userToken",{
    state: ()=>({
        user_token:'',
    }),
    actions: {
        setUserToken(user_token) {
          this.user_token = user_token
        },
      },
})


// import {defineStore } from 'pinia'

// export const useUserStore = defineStore ("user",{
//     state: ()=>({
//         user_id:'',
//     }),
//     actions: {
//         setUserId(user_id) {
//           this.user_id = user_id
//         },
//       },
// })