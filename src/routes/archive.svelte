<script>
    import data from '../../static/archive.json'
    console.log(data)
</script>

{#each data.archive as p}

    <h1>{p.title}</h1>
    <h2>{p.date}</h2>
    <div>
    {#each p.text as para}
    <p>{para}</p>
    {/each}
    </div>

    {#each p.assets as asset}
        <img src={asset} width=400px height=100%/>
    {/each}
{/each}