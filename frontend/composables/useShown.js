export default async function () {
    const { data: tags } = await useFetch(`https://data.dextermcmillan.com/api/tags/`);
    return useState('shown', () => tags.value.map(x => x.name))
}