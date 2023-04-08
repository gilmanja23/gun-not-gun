<script lang='ts'>
    import Hyper from "./Hyper.svelte";
    import Stats from "./Stats.svelte";
    import Classify from "./Classify.svelte";

    export let tabID:number;

</script>


{#if tabID == 1}
    <Hyper/>
{/if}


{#if tabID == 2}
    <Classify/>
{/if}


{#if tabID == 3}
    <Stats/>
{/if}