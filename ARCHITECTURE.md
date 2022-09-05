# Architecture

The s3-metadata-tagger can be conceptually seperated into two elements:

## The object_tagger.py
The object tagger is the execution driver, and the main point of access for library users.
It receives the location of the object to tag and a metadata extractor to apply (along with some further information), and then executes the flow logic of the tagging operation (Checking the files tags, downloading it, applying the extractor, adding the metadata to the s3 object).
See [object_tagger.py](src/metadata_tagger/object_tagger.py).

## The metadata extractors
The metadata extractors (like the one for [pdfs](src/metadata_tagger/pdf_metadata_extractor/pdf_metadata_extractor.py) or [pictures](src/metadata_tagger/picture_metadata_extractor/picture_metadata_extractor.py))
are responsible for retrieving the metadata from the object of interest. They receive a local file path, and return a dictionary containing the tags to apply.