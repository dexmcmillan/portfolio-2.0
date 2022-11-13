export default async function () {
    const { data: tags } = await useFetch(`https://d45esux869ize.cloudfront.net/api/tags/`);
    return useState('shown', () => tags.value.map(x => x.name))
}