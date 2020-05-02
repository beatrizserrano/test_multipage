#!/usr/bin/env python

import os
import fnmatch
import numpy
import imageio


def main():
    input_directory = "./ExampleHuman_original_data/images"
    output_multipage_tiff = "merged.tiff"

    try:
        input_tiff_filenames = get_tiff_files_in_directory(input_directory)
        numpy_arrays = load_tiff_files_as_numpy_array_sequence(
            input_tiff_filenames)
        merge_pages_on_file(numpy_arrays, output_multipage_tiff)
        print(f"{output_multipage_tiff} generated successfully.")
    except Exception as err:
        print(f"ERROR: Can not generate the output tiff. Reason: {err}")


def get_tiff_files_in_directory(directory):
    """Searches the given directory for .tif or .tiff files and returns a list with all the filenames found."""
    result = []
    for filename in os.listdir(directory):
        if fnmatch.fnmatch(filename, '*.tif*'):
            tif_filename = os.path.join(directory, filename)
            result.append(tif_filename)
    return result


def load_tiff_files_as_numpy_array_sequence(tiff_filenames):
    """Reads all the tiff files, given their filenames, and returns them as a sequence of numpy arrays"""
    result = []
    number_of_files = len(tiff_filenames)
    for i in range(number_of_files):
        filename = tiff_filenames[i]
        img = imageio.imread(filename)
        result.append(img)
    return result


def merge_pages_on_file(pages, output):
    """Merges a sequence of numpy arrays containing image data into a multi-page tiff."""
    imageio.mimwrite(output, pages)


if __name__ == "__main__":
    main()
