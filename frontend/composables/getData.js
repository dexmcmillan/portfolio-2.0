export const getProjects = async () => {

    const config = useRuntimeConfig()

    let baseUrl

    // If we're in dev mode, use testing/dev database.
    if (config.mode != 'production') {
        baseUrl = "http://localhost:8000"
    }

    // Otherwise, use the real one.
    else {
        baseUrl = "https://data.dextermcmillan.com"
    }

    return await useFetch(`${baseUrl}/api/projects`)
}

export const getTags = async () => {

    const config = useRuntimeConfig()

    let baseUrl

    // If we're in dev mode, use testing/dev database.
    if (config.mode != 'production') {
        baseUrl = "http://localhost:8000"
    }

    // Otherwise, use the real one.
    else {
        baseUrl = "https://data.dextermcmillan.com"
    }

    return await useFetch(`${baseUrl}/api/tags`)
}

export const getJobs = async () => {

    const config = useRuntimeConfig()

    let baseUrl

    // If we're in dev mode, use testing/dev database.
    if (config.mode != 'production') {
        baseUrl = "http://localhost:8000"
    }

    // Otherwise, use the real one.
    else {
        baseUrl = "https://data.dextermcmillan.com"
    }
    return await useFetch(`${baseUrl}/api/jobs`)
}