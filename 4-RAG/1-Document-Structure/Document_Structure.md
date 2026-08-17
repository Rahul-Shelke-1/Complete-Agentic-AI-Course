# Document Structure

![document-structuring](../flowcharts/4-document-structuring.svg)
*[figure 4.1]*

Whenever we work with an external knowledge base or data that needs to be fed into a vector DB, we definitely need to understand this document structure.

We might ask ourselves: **"Why?"**

## RAG Pipeline

![rag-pipeline](../flowcharts/3-rag-pipeline.svg)
*[figure 4.2]*

Because in this data ingestion pipeline [figure 4.2], the first step is data ingestion. Whenever we talk about data ingestion, we can have various kinds of source files like PDF files, HTML files, database files, and Excel files. Our main aim is to read all these file contents and convert them into a structure where we can additionally apply strategies like chunking, embedding, and storing into a vector DB-which is what this entire pipeline is all about.

So for that, we really need to understand "Document Structuring".

Referring to figure 4.2, in the data ingestion pipeline, the first step is data ingestion. This means we may have different kinds of files such as PDFs, HTML, Excel, database files, unstructured files, or any other format.

So in data ingestion, our main strategy revolves around: 
- *how do we proceed with reading this particular file?* 
- *how do we perform data parsing?* 
and then 
- *how do we convert this into a document structure?* 

These are the key reasons why we must understand "Document Structuring", along with:

* How to build this "Document Structure"?
* What is metadata?
* What does the structure of metadata look like?

**Data Parsing**: This step is really important. In the retrieval pipeline (i.e., query retrieval pipeline), proper parsing makes retrieval much more efficient and leads to much more accurate results.

After data parsing, we need to perform **chunking**.

In chunking, we convert the entire document into multiple smaller chunks. This strategy is all about breaking big documents into smaller parts or chunks.

Again, we might ask ourselves: **Why?** (Why break big documents into smaller parts?).

The reason we do this is that whenever we work with any LLM model or embedding model, we need to embed the document, and every model has a fixed context size.

For example:

If we take an entire 100-page PDF document and pass it directly to an embedding model to convert the text into vector embeddings, it will not be possible. The model will return an error stating that the input exceeds its context size limit.

Therefore, we must feed the data strictly within the model's context size limits. This applies to both embedding models and the LLM models used in later stages, as every model operates with a specific context window.

Different LLM models may have different context window sizes.

So dividing our data into smaller chunks is a solid strategy to ensure the processed data fits properly before storing it into vector databases.

After embedding, we store the data in the vector database, where the chunks are stored as vectors.

Finally, from the vector DB, we can apply similarity search techniques to retrieve the most relevant data chunks.