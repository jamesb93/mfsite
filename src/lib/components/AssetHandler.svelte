<script>
    export let assets;
    const images = ['jpg', 'png']
    const videos = ['mov', 'webm', 'mp4']
</script>

<div class="asset-box">
    {#each assets as asset}
    <!-- IF IMAGE -->
    {#if images.includes(asset.split('.').pop())}
    <img loading='lazy' src={asset} />
    {/if}
    
    {#if videos.includes(asset.split('.').pop())}
    {/if}
    {/each}
</div>

<style>
    .asset-box {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 10px;
    }
    img {
        max-width: 100%
    }
</style>