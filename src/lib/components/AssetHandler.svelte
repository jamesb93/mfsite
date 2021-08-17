<script>
    export let assets;
    const images = ['jpg', 'png']
    const videos = ['mov', 'webm', 'mp4']
</script>

<div class="asset-box">
    {#each assets as asset}
    <!-- IF IMAGE -->
    {#if images.includes(asset.split('.').pop())}
    <img src={asset} />
    {/if}
    
    {#if videos.includes(asset.split('.').pop())}
    {/if}
    {/each}
</div>

<style>
    .asset-box {
        display: flex;
        flex-direction: row;
        max-width: 60%;
        flex-wrap: wrap;
        gap: 10px;
    }
    img {
        max-width: 45%;
    }
</style>