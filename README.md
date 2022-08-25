# AWS S3 Metadata Tagger
The AWS S3 Metadata Tagger adds information to S3 objects.
More specifically, it contains multiple scripts to determine file properties, which are then added as s3 metadata. (For the difference between `tags` and `metadata` see https://stackoverflow.com/a/42146207/4786733)

The currently included scripts retrieve:
* image dimensions
* number of pages of a pdf
* encoding of a csv or xlsx file

They are invoked either via triggers configured on bucket, operation, and file suffix (see serverless.yml for the details) or via http endpoints.

Since metadata tags can only be added on object creation (copies with `MetadataDirective="REPLACE"` in this case), there exists the danger of
trigger loops, where each tagging operation causes a new invocation of the service.
To avoid this, each object is additionally tagged with a `docu-tools-tags` tag.
On each invocation, the service checks if the object has the above tag.
If it does, the function invocation returns, and no further creation operation is done.
If a tagging operation fails, it is retried three times before returning an exception.

## Structure

### `controller` 
contains the higher-level orchestration:
* `endpoints.py` specifies the incoming endpoints, and transforms each request into a client-agnostic object, passing it to ->
* `object_tagger.py`, which contains all the logic for checking whether the file has already been tagged, downloading it, invoking the metadata script, creating the tag object, and adding it to the s3 resource. 

The metadata scripts are stored in their respective folders

### `dataset_tagger`
The dataset tagger checks whether a file is `.xlsx` or `.csv` (with `magic`/[python-magic](https://github.com/ahupp/python-magic)) and consequently determines the encoding
* For `csv` files, [chardet](https://github.com/chardet/chardet) is used
* For `xlsx` files, the `coreProps/core.xml` file is extracted, and there the `encoding` field is read

### `pdf_tagger`
The pdf tagger uses [PyPDF2](https://pypdf2.readthedocs.io/en/latest/) to determine the amount of pages in a pdf

### `picture_tagger`
Using [Pillow](https://python-pillow.org/), the script gets the `width` and `height` of the passed image