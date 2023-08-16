import {defineStore } from 'pinia'

export const useUserStore = defineStore ("user",{
    state: ()=>({
        user_id:'',
    }),
    actions: {
        setUserId(user_id) {
          this.user_id = user_id
        },
      },
})