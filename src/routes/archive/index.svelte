<script>
    import { archive } from '$lib/app';
    import { fade } from 'svelte/transition';
    import stringSimilarity from "string-similarity";

    let allTags = [];
    let selectedTags = [];
    let filteredProjects = [];
    let searchTerm = ''
    $archive.forEach(d => d.tags.forEach(tag => allTags.push(tag)))

    $: if (selectedTags.length === 0) {
        filteredProjects = $archive
    } else {
        // Do filtering here
        filteredProjects = $archive.filter(p => {
            return selectedTags.some(r => p.tags.includes(r))
        })
    }

    function toggleTag(tag) {
        if (selectedTags.includes(tag)) {
                selectedTags.splice(selectedTags.indexOf(tag), 1)
        } else {
            selectedTags.push(tag)
        }
        selectedTags = selectedTags; // Svelte Reactivity???
    }

    function updateSearch() {
        filteredProjects.forEach(d => {
            const comparator = d.title.replace(/[^a-zA-Z]+/g, '').toLowerCase();
            d['dist'] = stringSimilarity.compareTwoStrings(searchTerm.toLowerCase(), comparator)
        })

        filteredProjects.sort((a, b) => a.dist - b.dist);
        filteredProjects = filteredProjects.reverse();
    }


</script>

<!-- https://svelte-tags-input.vercel.app/#installation -->
<!-- https://svelte.dev/repl/129f603083664aab9e5d10fe867745e2?version=3.42.1 -->
<div class='search'>
    <input 
    placeholder='enter search term here'
    type='text' 
    id='search-bar' 
    bind:value={searchTerm} 
    on:input={updateSearch}
    />
    <div class="tag-selector">
        {#each allTags as tag}
        <button
        class:tag-select={selectedTags.includes(tag)}
        on:click={() => toggleTag(tag)} 
        class='tag'>
        {tag}
        </button> 
        {/each}
    </div>
</div>

<div class="project-area">
    {#each filteredProjects as project}
    <div class="project" transition:fade={{duration: 80}}>
        <h1><a href='archive/{project.title}'>{project.title}</a></h1>
        <h2>{project.date}</h2>
        <div class='project-tags'>
        tags: {project.tags}
        </div>
    </div>
    {/each}
</div>

<style>
    .search {
        max-width: 100%;
    }
    .project-area {
    }
    .project {
    }

    .tag-selector {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 3px;
    }

    .tag {
        border: 1px solid grey;
        width: max-content;
        padding-left: 4px;
        padding-right: 4px;
        cursor: pointer;
    }
    .tag-select {
        /* border: 4px solid red; */
        font-style: italic;
    }

    .tag:hover {
        background: rgb(228, 228, 228);
    }

    .tag:active {
        background: rgb(196, 196, 196);
    }
</style>
