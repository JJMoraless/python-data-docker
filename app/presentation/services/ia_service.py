from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_huggingface.llms import HuggingFacePipeline
from transformers import pipeline

# if True:
#     model = pipeline(model="google/flan-t5-large")
#     model.save_pretrained("~/flan-t5-large")
# from langchain_openai import ChatOpenAI


class IaService:
    # def prompt_template(self, phrase_str: str):
    #     prompt_template = PromptTemplate.from_template(
    #         "describe un objeto que le resulta {abjetivo} y por que tiene ese efecto en ti"
    #     )

    #     result = prompt_template.format(abjetivo=phrase_str)
    #     return result

    # def prompt_template_chains(self, prompt_str: str):
    #     template = "Eres un axistente util que traduce el {idioma_entrada} al {idioma_salida} el texto: {texto}"
    #     prompt_template = PromptTemplate(
    #         input_variables=["idioma_entrada", "idioma_salida", "texto"],
    #         template=template,
    #     )

    #     translator_llm = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
    #     chain = LLMChain(llm=translator_llm, prompt=prompt_template)

    #     res_chain = chain.invoke(
    #         input={
    #             "idioma_entrada": "español",
    #             "idioma_salida": "ingles",
    #             "texto": prompt_str,
    #         }
    #     )
    #     return res_chain

    def save_model(self):
        return "ok"

    def llm_promt(self):
        llm = HuggingFacePipeline.from_model_id(
            model_id="~/flan-t5-large",
            task="text2text-generation",
            model_kwargs={"temperature": 1e-10},
        )

        template = PromptTemplate(input_variables=["input"], template="{input}")
        chain = LLMChain(llm=llm, verbose=True, prompt=template)
        chain("What is the meaning of life?")


    def mistral_ia(self):
        pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")
        return True
         
        
