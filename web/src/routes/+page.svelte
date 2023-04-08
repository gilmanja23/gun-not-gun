<script lang="ts">
    import TabSwitch from "../lib/home/TabSwitch.svelte";

    let tabID:number = 2

</script>

<h1 class="text-4xl font-bold text-center p-10 pb-0">Gun, not Gun</h1>

<div class="grid justify-center p-10">
    <div class="tabs justify-around w-full">
        <button on:click={() => tabID = 1} class="tab w-96 tab-bordered {tabID === 1 ? 'tab-active' : ''}">Adjust Hyper Parameters</button> 
        <button on:click={() => tabID = 2} class="tab w-96 tab-bordered {tabID === 2 ? 'tab-active' : ''}">Classify</button> 
        <button on:click={() => tabID = 3} class="tab w-96 tab-bordered {tabID === 3 ? 'tab-active' : ''}">Model Statistics</button>
    </div>
    
    <div class="p-10 w-full">
        <TabSwitch tabID={tabID}/>
    </div>
</div>