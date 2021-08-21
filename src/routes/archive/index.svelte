<script>
    import { archive } from '$lib/app';
    import { fade } from 'svelte/transition';
    import ArchiveSearch from '$lib/components/ArchiveSearch.svelte';

    let projects = $archive;
</script>

<ArchiveSearch bind:result={projects} />

<div class="project-area">
    {#each projects as project}
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
    .project-area {
        height: 100vh;
    }
</style>
