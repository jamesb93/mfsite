<script context="module">
    export function load({ error, status }) {
        return {
            props: {
                title: `${status}: ${error.message}`
            }
        };
    }
</script>

<script>
    export let title;
</script>

<h1>{title}</h1>
<p>If you think this page should exist please contact James Bradbury</p>