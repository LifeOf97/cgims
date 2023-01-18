# CGIMS - Career Guidance Information and Management System

This web based system was developed as a result of my undergraduate project.

## What is CGIMS/Web-Based CGIMS

[CGIMS](https://cgims.vercel.app/) is a web based system to facilitate counselling exercises in secondary schools here in Nigeria.
Web-based career guidance information and management system, creates an awareness to the use of computers in counselling. Currently the job of counselling towards a future career is not an easy one, the student has to be followed regularly within aptitude and academic performance so that he/she will be directed towards his/her gift career.


### Version 1

Version 1 of this new system will provide questionnaires carefully crafted by the counselling staff of the school in question, in respect to the counselling guidelines by relevant educational, social and cultural authorities in the country. This will then be used to engage with the students so as to collect answers from them.


# Please Note

As of January 2023, the backend server will no longer be available due to the fact that i was using the heroku free service which is no longer available for free. When/if i find a suitable replacement, this documentation will be updated to notify readers. Thank you for your understanding.

## Tech Stack

**Frontend**
* HTML
* JavaScript
* Vuejs 3 (with composition API)
    * Vite (Build tool)
    * Vue router (for SPA)
    * Pinia (Store)
    * Vitest (Pending...)
* TailwindCSS
* GSAP

**backend**
* Python
* Django
    * djangorestframework (REST API)

**Database**
* Postgresql

**Deployment**
* Docker
* Vercel (frontend)
* Heroku (Backend)

#
Please note, because of the free tier i use with the platform hosting the CGIMS backend api. _[Heroku](https://heroku.com)_ in my case, media files such as images are not provided, so the first letter of the signed in staff or student is used in place of the users avatar.
