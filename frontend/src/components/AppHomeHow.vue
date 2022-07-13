<script setup>
/* eslint-disable */
import questionStory from '../assets/svgs/Questions.svg'

</script>

<template>
  <main class="w-full h-full bg-white">

    <div class="w-11/12 py-10 mx-auto flex flex-col gap-5 md:w-10/12 lg:py-24 lg:w-9/12">

        <div class="w-full h-full flex flex-col gap-y-10 items-center  lg:flex-row">

            <div class="flex-1 flex flex-col gap-4 lg:px-10">
                <p class="self-start bg-yellow-500 px-4 py-1 text-white text-xs font-medium rounded-full md:text-sm">How CGIMS</p>
                <h3 class="text-slate-900 text-2xl font-black md:text-3xl">How Career Guidance Information and Management System Works?</h3>
                <p class="text-xs text-slate-600 md:text-sm">
                    In secondary schools, the number of students required to undergo counselling are very enormous and the number of staffs in
                    counselling cannot handle the job effectively. It is very easy to forget Information about students.<br><br>
                    
                    Another major problem of counselling is the way and manner information is being stored. The mode of storing information about
                    students observed by the counsellor is not reliable and this makes the counsellor to apply guess work in trying to direct
                    students in their future career path. <br><br>

                    Delay is decision making is a very big problem in todays fast paced world. Referencing to students information for decisions
                    concerning students future career takes a very long time. Decision should be precise and accurate based on the data available.
                </p>
            </div>

            <!-- start of story svg -->
            <div class="relative flex-1 w-full">
                <img :src="questionStory" alt="Question Story" class="w-full h-full">
                <a href="https://storyset.com/people" target="_blank" class="absolute bottom-24 right-16 text-xs italic hover:text-blue-600">People illustrations by Storyset</a>
            </div>
            <!-- end of story svg -->

        </div>

    </div>

  </main>
</template>