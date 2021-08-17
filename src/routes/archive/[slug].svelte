<script context="module">
	export async function load({ page }) {
        return { 
            props: {slug: page.params.slug}
        };
	}
</script>

<script>
    import AssetHandler from '$lib/components/AssetHandler.svelte';
    import { archive } from '$lib/app';
    import marked from 'marked';
    export let slug;
    
    let project = $archive.filter(p => p.title === slug)[0]
</script>

<div>
    <h1>{project.title}</h1>
    <h2>{project.date}</h2>
    <hr>
    {@html marked(project.text)}

    <AssetHandler assets={project.assets}/>
</div>
