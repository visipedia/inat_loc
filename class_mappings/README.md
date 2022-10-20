# Class Mappings

## Mapping Between CUB and iNaturalist

CUB contains 200 bird categories, but they are mostly identified by "common names" (not scientific names). To map the CUB classes to iNaturalist classes, we need to know the *iNaturalist Taxon ID* (i.e. the integer code that iNaturalist uses to denote a particular type of organism) corresponding to each CUB class. 

We therefore carry out the following *highly* scientific procedure:
1. Paste the common name into a search engine.
2. If the common name seems to unambiguously correspond to a particular scientific name in the search results (i.e. agreement by Wikipedia, All About Birds, etc.), proceed. 
3. Search for that scientific name on the iNaturalist website. If there is a perfect match, write down the *iNaturalist Taxon ID* for that species, which is found in the URL of the iNaturalist page for that species.
We obtain matches for 188/200 CUB categories. 

The result is `cub_inat_mapping.txt`, which has the following headings:
* `cub_category`: The name of a CUB category. 
* `scientific_name`: The scientific name corresponding to a CUB category if we could find one - otherwise, `Unknown`. 
* `inat_taxon_id`: The iNaturalist Taxon ID corresponding to a CUB category if we could find one - otherwise, `-1`. 

Because taxonomies evolve over time, we note that this process was carried out between January 2022 and March 2022. If you spot any errors or changes, please open an issue!
