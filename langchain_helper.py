from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain #to put the individual components of the llm together
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.6)# temperature parameter is for checking whether its safe but less creative(0) or more creative but prone to errors(1)
    prompt_template_name=PromptTemplate(
        input_variables=["animal_type","pet_color"],
        template="I have a {animal_type} pet. It is {pet_color} in color. Suggest 5 cool names I could name my dog."
    )
    name_chain= LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response=name_chain({'animal_type':animal_type, 'pet_color':pet_color})

    return response

if __name__=="__main__":
    print(generate_pet_name("cow", "black"))