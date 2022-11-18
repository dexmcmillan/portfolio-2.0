// Comment out for dev or production database.

// const baseUrl = "http://localhost:8000"
const baseUrl = "https://data.dextermcmillan.com"

export const getProjects = async () => { return await useFetch(`${baseUrl}/api/projects`) }

export const getTags = async () => { return await useFetch(`${baseUrl}/api/tags`) }

export const getJobs = async () => { return await useFetch(`${baseUrl}/api/jobs`) }