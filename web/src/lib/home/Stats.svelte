<script lang="ts">
    import Graph from "./Graph.svelte";

    let data = [
        {
            "model": "CNN",
            "actual": [1, 2, 3, 3, 4, 1, 3],
            "predicted": [1, 2, 3, 3, 4, 2, 3],
            "stats": {
                "network": {
                    "hiddenLayers": 2,
                    "inputLayers": 10,
                    "totalNeurons": 1000
                },
                "hyperParams": {
                    "padding": 2,
                    "matrix": "idk different kinds",
                    "step": 3
                }
            }
        },
        {
            "model": "Joe is gay",
            "actual": [1, 2, 3, 3, 10, 1, 3],
            "predicted": [1, 2, 3, 3, 4, 2, 3],
            "stats": {
                "network": {
                    "hiddenLayers": 2,
                    "inputLayers": 10,
                    "totalNeurons": 1000
                },
                "hyperParams": {
                    "padding": 2,
                    "matrix": "idk different kinds",
                    "step": 3
                }
            }
        }
    ]
</script>


<div class="grid gap-5">
    {#each data as d}
        <div class="bg-primary p-5">
            <div class="bg-black p-5">
                <Graph actual={d.actual} predicted={d.predicted} title={d.model}/>
            </div>

            <h1 class="font-bold text-2xl p-5 pb-0">Stats</h1>
            <h1 class="font-bold text-xl px-10 py-5">Hyper Parameters</h1>

            <div class="w-full stats stats-vertical lg:stats-horizontal shadow p-5">
  
                <div class="stat">
                  <div class="stat-title">Padding</div>
                  <div class="stat-value">{d.stats.hyperParams.padding}</div>
                </div>
                
                <div class="stat">
                  <div class="stat-title">Matrix</div>
                  <div class="stat-value">{d.stats.hyperParams.matrix}</div>
                </div>
                
                <div class="stat">
                  <div class="stat-title">Step</div>
                  <div class="stat-value">{d.stats.hyperParams.step}</div>
                </div>
                
            </div>

            <h1 class="font-bold text-xl px-10 py-5">Network</h1>

            <div class="w-full stats stats-vertical lg:stats-horizontal shadow p-5">
  
                <div class="stat">
                  <div class="stat-title">Hidden Layers</div>
                  <div class="stat-value">{d.stats.network.hiddenLayers}</div>
                </div>
                
                <div class="stat">
                  <div class="stat-title">Input Layers</div>
                  <div class="stat-value">{d.stats.network.inputLayers}</div>
                </div>
                
                <div class="stat">
                  <div class="stat-title">Total Neurons</div>
                  <div class="stat-value">{d.stats.network.totalNeurons}</div>
                </div>
                
            </div>

        </div>
    {/each}
</div>