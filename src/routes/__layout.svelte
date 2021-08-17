<script>
	import '../app.css';
</script>

<main class='container'>
    <div class='left'></div>
    <div class='center'><slot/></div>
    <div class='right'></div>
</main>

<style>
	.container {
		display: grid;
		justify-content: center;
		gap: 90px;
	}

    .left {
        grid-area: left;
    }

    .center {
        grid-area: center;
    }

    .right {
        grid-area: right
    }

    	/* Media Queries */
	@media (min-width: 1200px) {
        .container {
			grid-template-columns: auto min(80ch, 100%) auto;
            grid-template-areas:
            "left center right"
        }
    }
    @media (max-width: 1200px) {
        .container {
			justify-content:start;
			gap: 0px;
			grid-template-rows: auto auto;
            grid-template-areas:
            "left"
            "center"
        }

		.right {
			display: none;
		}
    }
</style>

