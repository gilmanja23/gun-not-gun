<script lang="ts">
    let uploadedImage: string;
    let imageFile: File;

    function handleImageUpload(e: Event) {
        const image = (e.target as HTMLInputElement)?.files?.[0];
        if (!image) return;
        // URL.createObjectURL() creates a temporary URL for the image we can use as src for an img tag
        uploadedImage = URL.createObjectURL(image);
        imageFile = image;
    }

    async function handleClassify() {
        if (!imageFile) return;


        const formData = new FormData();
        formData.append('img', imageFile);

        console.log(formData)
    
        await fetch('http://127.0.0.1:8000/prediction', {
            method: 'POST',
            body: formData,
            mode: 'cors'
        })
        .then(response => response.json())
        .then(data => {
            response = data.prediction;
            console.log(response)
        })
        .catch(error => {
            console.error(error);
        });
    }
    

    let models: string[] = ["CNN One", "CNN Two", "CNN Three", "CNN Four"]

    let selectedModel: string = ""

    let loading: boolean = false

    let response: string = ""

    const classify = () => {
        // loading = true
        handleClassify()
        response = "Nope no gun here"
    }

</script>

<div class="grid gap-5">
    
    <div class="grid gap-5 bg-primary p-5 justify-center">
        <div class="pb-5">
            <h1 class="text-center font-bold text-2xl">Upload an Image</h1>
        </div>
        <div class=" flex justify-center">
            <input type="file" class="file-input w-full max-w-xs" name="albumImage" accept="image/*" on:change={handleImageUpload} />
        </div>
        <div class="">
            {#if uploadedImage}
                <div class="mt-4">
                    <img src={uploadedImage} style="max-width: 50ch;" alt="" />
                </div>
            {/if}
        </div>
    </div>
    <div class="grid gap-5 bg-primary p-5 justify-center">
        <div class="pb-5">
            <h1 class="text-center font-bold text-2xl">Choose a Model</h1>
        </div>
        
        {#each models as m}
            <label class="label cursor-pointer">
                <span class="label-text">{m}</span> 
                <input bind:group={selectedModel} type="radio" name="models" value={m} class="radio checked:bg-red-500" />
            </label>
        {/each}

        <h1>Selected Model: {selectedModel}</h1>

    </div>
</div>
<!-- <button class="btn btn-outline btn-success w-full mt-5">Classify</button> -->

<!-- The button to open modal -->
<label on:click={classify} for="my-modal-5" class="btn btn-outline btn-success w-full mt-5">Classify</label>

<!-- Put this part before </body> tag -->
<input type="checkbox" id="my-modal-5" class="modal-toggle" />
<div class="modal">
  <div class="modal-box w-11/12 max-w-5xl">
    <h3 class="font-bold text-2xl text-center">Results</h3>

    {#if loading}
        <p class="text-center">Classifying...</p>
        <progress class="progress w-full"></progress>
    {:else}
        <div class="grid justify-center gap-5">
            <div class="mt-4">
                <img src={uploadedImage} style="max-width: 50ch;" alt="" />
            </div>
            <div class="font-bold text-2xl text-center">
                {selectedModel}: {response}
            </div>
        </div>
    {/if}




    <div class="modal-action">
      <label for="my-modal-5" class="btn">Exit</label>
    </div>
  </div>
</div>
<!-- https://hartenfeller.dev/blog/sveltekit-image-upload-store -->
<!-- <form method="post" enctype="multipart/form-data">
    <input type="hidden" name="albumId" value={data.album.albumId} />
    
  
    
  
    <div class="mt-4 mb-6">
      <button
        class="button is-primary is-disabled"
        type="submit"
        formaction="?/updateAlbumImage"
        disabled={!uploadedImage ?? null}
        >Upload Image
      </button>
    </div>
  </form> -->