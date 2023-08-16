<template>
  <!-- wrapup Container  -->
  <div class="leftsidebar flex mt-5">
    <!-- left side bar -->
    <leftsideBar />

    <!-- Middle bar -->
    <div
      class="middlebar ml-10 w-[600px] bg-white rounded-lg overflow-y-scroll border-red-300 border-4 hover:border-red-700 "
    >
      <!-- Tweet Section -->
      <div class=" ">
        <div class="px-5 py-3 border-b border-lighter flex items-center justify-between">
          <h1 class="text-xl font-bold">Home</h1>
          <i class="far fa-star text-xl text-blue" @click="pageRefresh"></i>
        </div>
      </div>
      <div class="px-5 py-3 border-b-8 border-lighter flex">
        <div class="flex-none">
          <img
            src="../../public/userAvtar2.png"
            class="flex-none mt-2 w-12 h-12 rounded-full border border-lighter"
          />
        </div>
        <div class="ml-2">
          <form action="">
            <input
              type="text"
              v-model="body"
              placeholder="What's up?"
              class="mt-3 pb-3 w-full border-black border-2 hover:bg-slate-600 hover:text-white focus:outline-none"
            />
            <div class="flex items-center">
              <a href=""> <i class="text-lg text-blue mr-4 far fa-image"></i></a>
              <a href=""> <i class="text-lg text-blue mr-4 fas fa-film"></i></a>
              <a href=""> <i class="text-lg text-blue mr-4 far fa-chart-bar"></i></a>
              <a href=""> <i class="text-lg text-blue mr-4 far fa-smile"></i></a>
              <button
                type="button"
                @click="addTweet"
                class="bg-blue-950 hover:bg-blue-600 rounded-lg px-5 hover:text-stone-100  text-white"
              >
                Tweet
              </button>
            </div>
          </form>
        </div>
      </div>
      <div class="flex flex-col-reverse">
        <div
          v-for="(tweet, index) in tweetList"
          :key="index"
          class="w-full p-4 border-b hover:bg-lighter flex"
        >
          <div class="flex-none mr-4">
            <img src="../../public/userAvtar2.png" class="h-12 w-12 rounded-full flex-none" />
          </div>
          <div class="w-full">
            <div class="flex items-center w-full">
              <p class="font-semibold">{{ username }}</p>
              <p class="text-sm text-dark ml-2">@{{ username }}</p>
              <p class="text-sm text-dark ml-2">{{ formatTimeAgo(tweet.created) }}</p>
              <i class="fas fa-angle-down text-dark ml-auto"></i>
            </div>
            <a href=""></a>
            <p class="py-2">
              {{ tweet.body }}
            </p>
            <div class="flex items-center justify-between w-full">
              <div class="flex items-center text-sm text-dark">
                <button href=""><i class="far fa-comment mr-3"></i></button>
                <p>1</p>
              </div>
              <div class="flex items-center text-sm text-dark">
                <button href=""><i class="fas fa-retweet mr-3"></i></button>
                <p>0</p>
              </div>
              <div class="flex items-center text-sm text-dark">
                <button href=""><i class="fas fa-heart mr-3"></i></button>
                <p>2</p>
              </div>
              <div class="flex items-center  text-dark">
                <button href="" @click.prevent="deleteTweet(tweet.id)"> <i class="fa-solid fa-trash mr-3"></i> </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div
        v-for="(follow, index) in following"
        :key="index"
        class="w-full p-4 border-b hover:bg-lighter flex"
      >
        <div class="flex-none mr-4">
          <img :src="`${follow.src}`" class="h-12 w-12 rounded-full flex-none" />
        </div>
        <div class="w-full">
          <div class="flex items-center w-full">
            <p class="font-semibold">{{ follow.name }}</p>
            <p class="text-sm text-dark ml-2">{{ follow.handle }}</p>
            <p class="text-sm text-dark ml-2">{{ follow.time }}</p>
            <i class="fas fa-angle-down text-dark ml-auto"></i>
          </div>
          <p class="py-2">
            {{ follow.tweet }}
          </p>
          <div class="flex items-center justify-between w-full">
            <div class="flex items-center text-sm text-dark">
              <i class="far fa-comment mr-3"></i>
              <p>{{ follow.comments }}</p>
            </div>
            <div class="flex items-center text-sm text-dark">
              <i class="fas fa-retweet mr-3"></i>
              <p>{{ follow.retweets }}</p>
            </div>
            <div class="flex items-center text-sm text-dark">
              <i class="fas fa-heart mr-3"></i>
              <p>{{ follow.like }}</p>
            </div>
            <div class="flex items-center text-sm text-dark">
              <i class="fas fa-share-square mr-3"></i>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- right side bar -->
    <div
      class="flex-shrink rounded-lg w-[400px] ml-10 bg-white overflow-y-scroll border-red-300 border-4 hover:border-red-700"
    >
      <input
        class="pl-12 bg-slate-500 mt-3 rounded-full w-full p-2 bg-lighter text-sm mb-4 hover:bg-slate-700 hover:text-white"
        placeholder="Search Twitter"
      />
      <i class="fas fa-search absolute top-[42px] right-[520px]"></i>
      <div class="w-full rounded-lg bg-lightest">
        <div class="flex items-center justify-between p-3">
          <p class="text-lg font-bold">Trends for You</p>
          <i class="fas fa-cog text-lg text-blue"></i>
        </div>
        <button
          v-for="(trend, index) in trending"
          :key="index"
          class="w-full flex justify-between hover:bg-lighter p-3 border-t border-lighter"
        >
          <div>
            <p class="text-xs text-left leading-tight text-dark">{{ trend.top }}</p>
            <p class="font-semibold text-sm text-left leading-tight">{{ trend.title }}</p>
            <p class="text-left text-sm leading-tight text-dark">{{ trend.bottom }}</p>
          </div>
          <i class="fas fa-angle-down text-lg text-dark"></i>
        </button>
        <button class="p-3 w-full hover:bg-lighter text-left text-blue border-t border-lighter">
          Show More
        </button>
      </div>
      <div class="w-full rounded-lg bg-lightest my-4">
        <div class="p-3">
          <p class="text-lg font-bold">Who to Follow</p>
        </div>

        <!-- Follow User Display -->
        <div>
    <!-- Fetch and display the top 3 users -->
                  <div v-for="user in follow" :key="user.id" class="w-full flex hover:bg-lighter p-3 border-t border-lighter">
                    <img :src="`/public/anonymous-avtar.jpeg`" class="w-12 h-12 rounded-full border border-lighter" />
                    <div class="hidden lg:block ml-4">
                      <p class="text-sm font-bold leading-tight">{{ user.username }}</p>
                      <p class="text-sm leading-tight">{{ user.username }}</p>
                    </div>
                    <button
                      @click="viewUser(user.id, user.username)"
                      class="ml-auto text-sm text-white py-1 px-4 rounded-full border-2 border-blue bg-blue-950 hover:bg-blue-600"
                    >
                      View
                    </button>
                  </div>
                </div>

        <button class="p-3 w-full hover:bg-lighter text-left text-blue border-t border-lighter" type="button" @click.prevent="followbtn">
          Show More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import leftsideBar from '@/components/leftsideBar.vue'
// import {useUserStore} from '@/stores/user.js'
// import {useuserTokenStore} from '@/stores/userToken.js'

export default {
  // setup() {
  //       const userTokenStore = useuserTokenStore()
  //       const user_token = userTokenStore.user_tokeen
  //       return {
  //         user_token
  //   }
  // },
  components: {
    leftsideBar
  },
  data() {
    return {
      username: '',
      userId: '',
      status: 'Follow',
      dropdown: false,
      body: '',
      trending: [
        { top: 'Techies all around', title: 'Tech', bottom: '#The technology' }
        // {top: 'Apps', title: 'Flutter', bottom: '100K Tweets'},
        // {top: 'Animals', title: 'Shark larger than Great white', bottom: '115k tweets'},
        // {top: 'The techies nation', title: '2m servers', bottom: '30k tweets'},
      ],
      follow: [],
      // following: [
      //   {src: 'https://randomuser.me/api/portraits/women/52.jpg', name: 'Giza Lamo', handle: '@giza', time: '1.2 hr', tweet: 'The very essence of TailWindCSS??', comments: '500', retweets: '250', like: '52,003'},
      //   {src: 'https://randomuser.me/api/portraits/women/62.jpg', name: 'Doug mama', handle: '@mama', time: '25 min', tweet: 'Should I use Flutter now?', comments: '1000', retweets: '500', like: '70,003'},
      //   {src: 'https://randomuser.me/api/portraits/men/63.jpg', name: 'Ezy Pzy', handle: '@ezypzy', time: '2.7 hr', tweet: 'Get Ready for the tech revolution', comments: '10,000', retweets: '100,002', like: '200,003'},
      // ],
      tweetList: [],
      
    }
  },
  created() {
    this.username = localStorage.getItem('username')
    this.fetchTweets();
    this.fetchUsers();
  },
  methods: {
    pageRefresh(){
      window.location.reload();
    },
    async addTweet() {
      const userId = localStorage.getItem('user_id')
      const tweetContent = this.body
      axios
        .post('http://localhost:8000/api/v2/tweet/', {
          author: userId,
          content: tweetContent
        })
        .then((response) => {
          this.body = '',
          console.log('Tweet created successfully:', response.data)
          this.fetchTweets();
        })
        .catch((error) => {
          console.error('Error creating tweet:', error.response.data)
        })
    },
    fetchTweets() {
      const  userId = localStorage.getItem('user_id');
      // console.log(userId);
      axios
        .get(`http://localhost:8000/api/v2/tweet/?author_id=${userId}`)
        .then((response) => {
          this.tweetList = response.data.reverse()
        })
        .catch((error) => {
          console.error('Error fetching tweets:', error.response.data)
        })
    },
    formatTimeAgo(createdAt) {
      const createdTime = new Date(createdAt)
      const currentTime = new Date()
      const timeDifferenceInSeconds = Math.floor((currentTime - createdTime) / 1000)

      if (timeDifferenceInSeconds < 60) {
        return `${timeDifferenceInSeconds} sec ago`
      } else if (timeDifferenceInSeconds < 3600) {
        const minutes = Math.floor(timeDifferenceInSeconds / 60)
        return `${minutes} min ago`
      } else if (timeDifferenceInSeconds < 86400) {
        const hours = Math.floor(timeDifferenceInSeconds / 3600)
        return `${hours} hour ago`
      } else {
        const days = Math.floor(timeDifferenceInSeconds / 86400)
        return `${days} days ago`
      }
    },
    fetchUsers(){
      axios
        .get('http://localhost:8000/api/v1/users/') 
        .then((response) => {
          const sortedUsers = response.data.sort((a, b) => b.followers_count - a.followers_count);
          
          // console.log(sortedUsers)
          // Get the top 3 users from the sorted array
        // const username = localstorage.getItem('username')
        const filteredUsers = sortedUsers.filter((user) => user.username !== this.username);
        // console.log(filteredUsers)
        this.follow = filteredUsers.slice(0, 3);
          
        })
        .catch((error) => {
          console.error('Error fetching users:', error.response.data);
        });
    },
    deleteTweet(tweetid){
      axios.delete(`http://localhost:8000/api/v2/tweet/${tweetid}`)
        .then(()=>{
          console.log("Tweet deleted successfully")
          this.fetchTweets()
        })
        .catch((error) => {
          console.error('Error fetching tweets:', error.response.data)
        })
     },
     viewUser(userId, username){
        this.$router.push({
          name: 'userview',
          params:{
            userId,
            username
          }
        })
     }
  }
}
</script>
