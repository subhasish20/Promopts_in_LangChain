from langchain_core.prompts import  PromptTemplate


# used to convert the prompt into other file format by which we can access it in the other promgrams

template = PromptTemplate(
    template="""
        Your are a helpful assistant !!
        Act as an expert in summarizer and summarize the given text {text},
        Where the summarization style will be {style}
        and the length will be {length}
        """,
    input_variables=["text", "style", "length"],
    validate_template=True
)

template.save("template.json")