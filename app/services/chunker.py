from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text: str):
    """
    Split text into smaller chunks for AI processing
    """

    # Create text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    # Split text into chunks
    chunks = text_splitter.split_text(text)

    return chunks