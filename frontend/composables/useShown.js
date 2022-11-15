// This function controls the state of which tags are shown on the site.
export default async function () {

    const { data: tags } = await getTags()

    return useState('shown', () => tags.value.map(x => x.name))

}