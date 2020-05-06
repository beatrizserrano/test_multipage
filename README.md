## Test the multi-page option to pass packed images from the IDR download tool to CellProfiler in Galaxy

__1.__ The output features of the ExampleHuman dataset is in the folder `results_separate_images`.

__2.__ Python script to create a multi-page tiff from numpy objects (by @davelopez).
  - Input: original ExampleHuman tiff files to use them as numpy objects
  - Output: multi-page tif
  - Dependencies: imageio
  
  Part of this code can be included in the IDR download tool to save multiple numpy objects (from `getTile`) into one file instead of saving separate tif files.
  
  *NOTE:* All the files within a multi-page file need to have the same dimensions. The batches of images should never combine images from different datasets (they are cropped differently).
  
__3.__ To run CellProfiler using the multi-page tif some adjustments are needed:
  - Module `Metadata` 
      - Metadata extraction method -> `Extract from image file headers`
  - Module `NamesAndTypes` (this config might not be needed)
      - Assign a name to -> `Images matching rules`
      - Match `All` of the following rules
      - Select the rule criteria: 
        - `Metadata` - `does` - `Have Frame matching` - `0`
        - `Image` - `Is` - `Stack frame`

The output features are in the folder `results_multipage_tiff`.
