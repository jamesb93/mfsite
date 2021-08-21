<script>
    const minYear = 1900;
    const maxYear = new Date().getFullYear();
    export let year = null;
</script>

<input 
class='picker'
type=number
bind:value={year}
/>

<style>
    input[type=number] {
        -moz-appearance: textfield;
    }

    input::-webkit-outer-spin-button,
    input::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
</style>