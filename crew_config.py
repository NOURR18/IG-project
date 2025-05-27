from crewai import Agent

retriever = Agent(name="Retriever", description="Retrieves relevant travel chunks")
summarizer = Agent(name="Summarizer", description="Summarizes retrieved content")
composer = Agent(name="Composer", description="Composes the final user response")

agents = [retriever, summarizer, composer]