<script>
    import { archive } from '$lib/app';
    import { parseYear, validYear } from '$lib/utils';
    import stringSimilarity from "string-similarity";
    import YearPicker from '$lib/components/YearPicker.svelte';

    export let result = $archive;

    let allTags = [];
    let filters = {
        minYear : 1950,
        maxYear : new Date().getFullYear(),
        tags : [],
        categories : [],
    }
    let searchTerm = ''

    // Get all the possible tags out
    $archive.forEach(d => d.tags.forEach(tag => {
        if (!allTags.includes(tag))
            allTags.push(tag);
    }));

    // Tag Toggles
    function toggleTag(tag) {
        if (filters.tags.includes(tag)) {
            filters.tags.splice(filters.tags.indexOf(tag), 1)
        } else {
            filters.tags.push(tag)
        }
        filters.tags = filters.tags; // hint to svelte
    }

    // Calculate distances on fuzzy-text search and update
    // Sorts the results by their distance
    function updateTextSearch() {
        result.forEach(d => {
            const comparator = d.title.replace(/[^a-zA-Z]+/g, '').toLowerCase();
            d['dist'] = stringSimilarity.compareTwoStrings(searchTerm.toLowerCase(), comparator)
        })

        result.sort((a, b) => a.dist - b.dist);
        result = result.reverse();
    }

    // Filters Handling
    $: filters, result = $archive.filter(p => {
        let [tags, categories, minYear, maxYear] = [true, true, true, true];
        const year = parseYear(p.date)
         
        if (validYear(filters.minYear)) {
            minYear = year >= filters.minYear;
        }

        if (validYear(filters.maxYear)) {
            maxYear = year <= filters.maxYear;
        }

        if (filters.tags.length !== 0) {
            tags = filters.tags.some(tag => p.tags.includes(tag));
        }

        if (filters.categories.length !== 0) {
            categories = filters.tags.some(cat => p.categories.includes(cat))
        }
        
        return tags && categories && minYear && maxYear; 
    })
</script>

<div class='search'>
    <div class='left'>
        <div class='text-search'>
            <input 
            placeholder='enter search term here'
            type=text
            id='search-bar' 
            bind:value={searchTerm} 
            on:input={updateTextSearch}
            />
        </div>
        <div class='year'>
            <span>From</span>
            <YearPicker 
            bind:year={ filters.minYear } 
            reset=1900
            />
            <span>To</span>
            <YearPicker 
            bind:year={ filters.maxYear }
            reset={ new Date().getFullYear() } 
            />
        </div>
        <div class="sort">
            sort by....
        </div>
    </div>

    <div class='right'>
        <div class="tag-selector">
            {#each allTags as tag}
            <div
            class:tag-select={filters.tags.includes(tag)}
            on:click={() => toggleTag(tag)} 
            class='tag'
            >
            {tag}
            </div>
            {/each}
        </div>
    </div>
</div>

<style>
    .search {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        gap: 20px;
    }

    #search-bar {
        width: 100%
    }

    .left {
        grid-area: filters;
    }

    .right {
        grid-area: tags;
    }

    .tag-selector {
        display: flex;
        flex-direction: column;
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
        font-style: italic;
    }

    .tag:hover {
        background: rgb(228, 228, 228);
    }

    .tag:active {
        background: rgb(196, 196, 196);
    }
</style>
