# Source Image Mappings

iNatLoc500 is drawn from iNat17 and iNat21. The files in this directory map the each image in iNatLoc500 to its source dataset. There are three files, one for each split:
* `inatloc500_image_mapping_train.txt`
* `inatloc500_image_mapping_val.txt`
* `inatloc500_image_mapping_test.txt`
Each row corresponds to an image in iNatLoc500. The headings are as follows:
* `file_name`: The name of the file in iNatLoc500. 
* `source_dataset`: The dataset from which the image was sourced. Either `inat17` or `inat21`.
* `source_dataset_split`: The split to which the image belonged in the source dataset.
* `source_dataset_image_id`: The image ID in the source dataset. 
Note that the rows follow the same order as the CSV metadata files in `dataset/metadata_choe`.
