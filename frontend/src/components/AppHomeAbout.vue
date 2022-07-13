<script setup>
/* eslint-disable */
import thinkingStory from '../assets/svgs/Thinking.svg'
import IconExternalLink from './icons/IconExternalLink.vue';
import IconHelpQuestionMark from './icons/IconHelpQuestionMark.vue';

const questions = [
    {
        id: 1,
        title: 'What Is Career Guidance',
        detail: `
            The word “guidance” originated back in the 1530s, and is defined as the process of directing conduct.
            Career guidance can be defined as a comprehensive, developmental program designed to assist individuals
            in making and implementing informed educational and occupational choices.
        `,
        source: 'https://www.mindler.com/career-guidance-meaning-benefits-importance'
    },
    {
        id: 2,
        title: 'What Is Career Counselling',
        detail: `
            Career counselling is a systematic process that helps an individual understand one’s self, as well as
            the world of work, to choose the right career. It is the process of helping students and professionals
            to analyze their strengths, interests, abilities and skills.
        `,
        source: 'https://www.careers360.com/articles/what-is-a-career-counselling-counar'
    },
    {
        id: 3,
        title: 'What Are Career Assessments',
        detail: `
            A career assessment is a system used to identify and monitor an individual's work-related skills and interests.
            Sometimes beginning in childhood, career assessments may include a number of different types of assessments that
            evaluate the individual's psychological strengths, functional capacity, and work-specific skills.
        `,
        source: 'https://www.workplacetesting.com/definition/2405/career-assessment'
    },
    
]
</script>

<template>
  <main class="w-full h-full bg-white">

    <div class="w-11/12 py-24 mx-auto flex flex-col gap-10 md:w-10/12 lg:w-9/12">

        <div class="w-full h-full flex flex-col gap-y-10 items-center  lg:flex-row">

            <div class="flex-1 flex flex-col gap-4">
                <p class="self-start bg-red-600 px-4 py-1 text-white text-xs font-medium rounded-full md:text-sm">About CGIMS</p>
                <h3 class="text-slate-900 text-2xl font-black md:text-3xl">What is Career Guidance Information and Management System?</h3>
                <p class="text-xs text-slate-600 md:text-sm">
                    The presence of counsellors in school is not just for the sake of it, they are there to direct student
                    on areas they psychologically find them fit. The job of counselling towards a future career is not an easy
                    one, the student has to be followed regularly within attitude and academic performance so that he/she will
                    be directed towards his/her gift career. This project work researched into the procedure involved in guiding
                    and counselling student in secondary schools with a view to come up with the modernized system that would
                    help in carrying out these activities effectively.<br><br>
                    
                    The problems associated with the existing system were detected and possible solutions to the problem were
                    provided in the new system. The new system is a web-based one, which works automatically; it is very easy
                    to use, it is also interactive, and cost effective. The new system is comprehensive enough, timely and accurate
                    in report generation.                    
                </p>
            </div>

            <!-- start of story svg -->
            <div class="relative flex-1 w-full">
                <img :src="thinkingStory" alt="Question Story" class="w-full h-full">
                <a href="https://storyset.com/people" target="_blank" class="absolute bottom-7 right-16 text-xs italic hover:text-blue-600 md:bottom-12">People illustrations by Storyset</a>
            </div>
            <!-- end of story svg -->

        </div>

        <!-- start of other questions -->
        <div class="grid gap-10 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">

            <div v-for="question in questions" :key="question.id" class="flex flex-col gap-5">
                <div class="flex gap-4 items-center">
                    <div class="w-10 h-10 rounded-full shadow-inner shadow-slate-400 bg-slate-200 flex items-center justify-center">
                        <IconHelpQuestionMark class="w-5 h-5 fill-slate-900" />
                    </div>
                    <p class="text-sm text-slate-900 font-semibold">{{question.title}}</p>
                </div>
                <div class="flex flex-col text-xs">
                    <p class="text-slate-600 font-normal">{{question.detail}}</p>
                    <a :href="question.source" target="_blank" rel="noopener noreferrer" class="self-start flex gap-1 items-center">
                        <IconExternalLink class="w-5 h-5 fill-blue-600" />
                        <p class="text-blue-600">Source</p>
                    </a>
                </div>
            </div>
            
        </div>
        <!-- end of other questions -->

    </div>

  </main>
</template>