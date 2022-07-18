<script setup>
/* eslint-disable */
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire';
import { ref, reactive } from 'vue';
import IconCloseBig from './icons/IconCloseBig.vue';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';
import IconPlus from './icons/IconPlus.vue';

// stores
const questionnaireStore = useStaffQuestionnaireStore()

// refs
const selectQuestion = ref(false)
const title = ref("")
const question = ref("")
const category = reactive([])
const filters = reactive([
    {
        id: 1,
        title: 'Gender',
        options: [
            {id: 1, name: 'Male', selected: false},
            {id: 2, name: 'Female', selected: false},
        ]
    },
    {
        id: 1,
        title: 'Class',
        options: [
            {id: 1, name: 'JSS1', selected: false},
            {id: 2, name: 'JSS2', selected: false},
            {id: 3, name: 'JSS3', selected: false},
            {id: 4, name: 'SSS1', selected: false},
            {id: 5, name: 'SSS2', selected: false},
            {id: 6, name: 'SSS3', selected: false},
        ]
    },
    {
        id: 1,
        title: 'Department',
        options: [
            {id: 1, name: 'Art', selected: false},
            {id: 2, name: 'Commercial', selected: false},
            {id: 3, name: 'Science', selected: false},
            {id: 4, name: 'Social Science', selected: false},
        ]
    },
])

// methods
const updateCategory = (state, value) => {
    // for some reasons the checkbox state is passed as false when active and
    // true when inactive soo....
    if (!state) category.push(value);
    else category.splice(category.indexOf(value), 1);
}
</script>

<template>
  <main class="w-full h-full mx-auto py-10 flex items-center justify-center bg-slate-400/50 backdrop-blur">

    <div class="w-11/12 mx-auto h-auto bg-white py-5 px-5  z-50 flex flex-col gap-16 rounded-lg shadow-lg md:py-10 md:px-20 lg:w-10/12 xl:w-9/12">

        <div class="grid grid-cols-3 gap-5">
            <div class="col-span-3 flex items-center justify-between border-b border-slate-200 pb-2 lg:col-span-2">
                <div class="flex flex-col">
                    <h3 class="text-xl text-slate-800 font-bold md:text-2xl">Questionnaire</h3>
                    <p class="text-xs text-slate-400 font-medium">Create a new questionnaire</p>
                </div>
    
                <button @click="questionnaireStore.create.open = false" type="button" class="p-2 transition-all duration-200 rounded-md group hover:bg-slate-100">
                    <IconCloseBig class="w-7 h-7 fill-slate-600 transition-all duration-200 group-hover:fill-rose-500" />
                </button>
            </div>
        </div>

        <form @submit.prevent class="grid grid-cols-1 gap-5 lg:grid-cols-3">

            <div class="col-span-3 grid gap-10 grid-cols-3">

                <!-- form fields -->
                <div class="col-span-3 flex flex-col gap-7 lg:col-span-2">
                    <div class="relative">
                        <AppInputField label="Title" v-model="title" placeholder="Enter questionnaire title..." />
                        <button @click="selectQuestion = !selectQuestion" type="button" class="absolute top-0 right-0 text-xs font-bold text-blue-500 transition-all duration-200 hover:text-blue-600 md:text-sm">Select Questions</button>
                        
                        <transition
                            name="slide-down"
                            enter-from-class="-translate-y-20 opacity-0"
                            enter-active-class="transition-all duration-500"
                            leave-to-class="-translate-y-20 opacity-0"
                            leave-active-class="transition-all duration-500">
                            <div v-if="selectQuestion" class="absolute top-16 w-full h-60 bg-white shadow-lg flex flex-col z-10">
                                <div class="w-full p-3 bg-slate-100 shadow-inner shadow-slate-400/50">
                                    <p class="text-xs font-medium text-center text-slate-400 md:text-sm">Select a predefined questionnaire</p>
                                </div>
                            </div>
                        </transition>
                    </div>

                    <div class="w-full h-full flex flex-col gap-2">
                        <label for="question" class="text-slate-700 text-xs font-medium md:text-sm">Question(s)</label>
                        <textarea
                            name="question"
                            id="question"
                            cols="30"
                            rows="10"
                            required
                            placeholder="Enter questions..."
                            class="w-full resize-none p-2 bg-slate-100 font-normal text-xs text-slate-900 rounded-sm ring-rose-500 ring-offset-2
                            ring-offset-rose-100 shadow transition-all duration-200 hover:ring-2 focus:ring-2 focus:outline-none md:text-sm">
                        </textarea>
                    </div>
                </div>
                <!-- end form fields -->

                <!-- start of students category -->
                <div class="col-span-3 flex flex-col gap-7 lg:col-span-1">
                    <div clas>
                        <h3 class="text-slate-800 text-md font-medium md:text-xl">Students</h3>
                        <p class="text-xs text-slate-400 font-normal">
                            Select the category of students this questionnaire is ment for.
                        </p>
                    </div>

                    <div class="flex flex-col gap-7">
                        <div class="flex flex-col gap-3" v-for="filter in filters" :key="filter.id">
                            <p class="capitalize text-slate-500 text-xs font-semibold md:text-sm">By {{filter.title}}</p>

                            <div class="flex flex-wrap items-center gap-3">
                                <label
                                    v-for="opt in filter.options"
                                    :key="opt.id" :for="opt.name"
                                    :class="opt.selected ? 'bg-slate-400 text-white':'bg-slate-100 text-slate-500'"
                                    class="group flex items-center gap-1 text-xs font-medium px-3 py-2 cursor-pointer rounded-md
                                    transition-all duration-200 ring-slate-400 hover:ring-1">
                                    <IconPlus :class="opt.selected ? 'fill-white':'fill-slate-500'" class="w-4 h-4 transition-all duration-200" />
                                    {{opt.name}}
                                    <input @click="updateCategory(opt.selected, opt.name)" type="checkbox" v-model="opt.selected" :name="opt.name" :id="opt.name" class="hidden">
                                </label>
                            </div>
                        </div>
                    </div>

                </div>
                <!-- end of students category -->

            </div>

            <div class="col-span-3 w-full flex items-center justify-end border-t border-slate-200 pt-5 lg:col-span-2">
                <div class="flex gap-2">
                    <AppButton @click.prevent="questionnaireStore.create.open = false" type="1" label="Cancle" />
                    <AppButton type="2" label="Save" :loading="questionnaireStore.create.loading || questionnaireStore.edit.loading" />
                </div>
            </div>

        </form>
    
    </div>

  </main>
</template>