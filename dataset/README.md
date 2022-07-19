# Images
The images in iNatLoc500 are drawn from [iNat21](https://github.com/visipedia/inat_comp/tree/master/2021) (for `train-weaksup`) and [iNat17](https://github.com/visipedia/inat_comp/tree/master/2017) (for `train-fullsup` and `test`). Each image in iNatLoc500 has the same path as it does in its source dataset. The image paths are therefore structured as follows: 
```
- train/species_folder/image.jpg # for train-weaksup, drawn from iNat21
- val/supercategory_folder/species_folder/image.jpg # for train-fullsup, drawn from iNat17
- test/supercategory_folder/species_folder/image.jpg # for test, drawn from iNat17
```

# Metadata

## Choe et al. Format
This is the format used by the [code](https://github.com/clovaai/wsolevaluation) from ["Evaluating Weakly Supervised Object Localization Methods Right"](https://arxiv.org/abs/2001.07437) (Choe et al. CVPR 2020). The metadata files are as follows:
```
- train
  - class_labels.txt
  - class_labels_genus.txt
  - class_labels_family.txt
  - class_labels_order.txt
  - class_labels_class.txt
  - class_labels_phylum.txt
  - class_labels_kingdom.txt
  - image_ids.txt
- val
  - class_labels.txt
  - class_labels_genus.txt
  - class_labels_family.txt
  - class_labels_order.txt
  - class_labels_class.txt
  - class_labels_phylum.txt
  - class_labels_kingdom.txt
  - image_ids.txt
  - image_sizes.txt
  - localization.txt
- test
  - class_labels.txt
  - class_labels_genus.txt
  - class_labels_family.txt
  - class_labels_order.txt
  - class_labels_class.txt
  - class_labels_phylum.txt
  - class_labels_kingdom.txt
  - image_ids.txt
  - image_sizes.txt
  - localization.txt
- class_names.txt
- class_names_genus.txt
- class_names_family.txt
- class_names_order.txt
- class_names_class.txt
- class_names_phylum.txt
- class_names_kingdom.txt
```
We now describe the content of each file.

### `class_labels.txt`
Each row corresponds to one image and has two entries:
```
path/to/image,category_label
```
The category label corresponds to a species. The species name corresponding to each label is given in `class_names.txt`. 

### `class_labels_X.txt`
The files 
* `class_labels_genus.txt`
* `class_labels_family.txt`
* `class_labels_order.txt`
* `class_labels_class.txt`
* `class_labels_phylum.txt`
* `class_labels_kingdom.txt` 
are similar to `class_labels.txt`, except that each image is labeled at the `genus`/`family`/.../`phylum` level instead of the species level. That is, `class_labels_X.txt` is a re-labeling of the images in `class_labels.txt` at a coarser level of granularity. The `genus`/`family`/.../`phylum` name corresponding to each label in `class_labels_genus.txt`/`class_labels_family.txt`/.../`class_labels_phylum.txt` is given in `class_names_genus.txt`/`class_names_family.txt`/.../`class_names_phylum.txt`. 

### `image_ids.txt`
Each row corresponds to one image and has a single entry:
```
path/to/image
```

### `image_sizes.txt`
Each row corresponds to one image and has three entries:
```
path/to/image,image_height,image_width
```

### `localization.txt`
Each row corresponds to one image and has five entries:
```
path/to/image,x_min,x_max,y_min,y_max
```

# Download Links
* Amazon S3
  * [Images](https://ml-inat-competition-datasets.s3.amazonaws.com/inatloc/iNatLoc.tar.gz) (18.9 GB, `md5sum f9394137ddbff3919fe805c6dd8f22cb`)
  * [Metadata](https://ml-inat-competition-datasets.s3.amazonaws.com/inatloc/metadata_choe.zip) (32.4 MB, `md5sum 5ae02339a005574b3c6757309e9872ed`)
* [Caltech Research Data Repository](https://data.caltech.edu/records/20229)
  * [Images](https://data.caltech.edu/tindfiles/serve/a3a9d489-01a2-4727-8496-a8a5b411ff0b/) (18.9 GB)
  * [Metadata](https://data.caltech.edu/tindfiles/serve/59e7b6ba-37f1-49a2-85da-ece1593b1e44/) (32.4 MB)
