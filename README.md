## Functionality
- Read contents of local .pdf file
- Answer questions about the file  

(both questions and file name are hardcoded, to be fixed soon)

## Integrations
- HuggingFace [pipeline](https://huggingface.co/docs/transformers/v4.35.2/en/main_classes/pipelines#transformers.QuestionAnsweringPipeline) for questions answering
- LangChain .pdf [loader](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#using-pypdf)

## Model
- [distilbert-base-cased-distilled-squad](https://huggingface.co/distilbert-base-cased-distilled-squad)
