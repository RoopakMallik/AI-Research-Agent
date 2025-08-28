# AI Research Agent

An intelligent research assistant powered by LangChain that can search the web, query Wikipedia, and generate structured research reports on any topic.

## Features

- **Multi-source Research**: Combines web search and Wikipedia queries for comprehensive information gathering
- **Structured Output**: Generates well-formatted research reports with topics, summaries, sources, and references
- **Automatic Saving**: Saves research outputs to text files with timestamps
- **Tool Integration**: Uses multiple AI tools working together through LangChain's agent framework
- **Flexible LLM Support**: Compatible with both OpenAI and Anthropic models

## Installation

1. **Clone the repository**
```bash
git clone <https://github.com/RoopakMallik/AI-Research-Agent.git>
cd research-agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file in the project root and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Usage

Run the research agent:
```bash
python main.py
```

The agent will prompt you with: "What can I help you Research today?"

Simply enter your research topic, and the agent will:
1. Search the web for relevant information
2. Query Wikipedia for additional context
3. Generate a structured research report
4. Save the results to `research_output.txt`

### Example Topics
- "Quartz Watches" 
- "Rolex Watch Company"
- "Artificial Intelligence in Healthcare"
- "Climate Change Solutions"

## Project Structure

```
research-agent/
│
├── main.py              # Main application entry point
├── tools.py             # Custom tools for web search, Wikipedia, and file saving
├── requirements.txt     # Project dependencies
├── research_output.txt  # Generated research reports (created automatically)
└── .env                # Environment variables (create this file)
```

## Output Format

The agent generates structured research reports containing:

- **Topic**: The research subject
- **Summary**: Comprehensive overview with key concepts and findings
- **Sources**: List of referenced websites and documents
- **Tools Used**: Which research tools were utilized
- **References**: Properly formatted citations
- **Timestamp**: When the research was conducted

## Configuration

### Adjusting Wikipedia Search
In `tools.py`, you can modify the Wikipedia tool settings:
```python
api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,           # Number of Wikipedia results
    doc_content_chars_max=100  # Character limit per result
)
```

### Changing the LLM Model
In `main.py`, update the model configuration:
```python
llm = ChatOpenAI(model_name="gpt-4")  # or "gpt-3.5-turbo"
# or use Anthropic:
# llm = ChatAnthropic(model="claude-3-sonnet-20240229")
```

## Dependencies

- **langchain**: Core framework for building AI agents
- **langchain-openai**: OpenAI integration
- **langchain-anthropic**: Anthropic Claude integration  
- **langchain-community**: Community tools and utilities
- **wikipedia**: Wikipedia API wrapper
- **duckduckgo-search**: Web search functionality
- **pydantic**: Data validation and parsing
- **python-dotenv**: Environment variable management

## Sample Output

```
Research Output for You: 
Timestamp: 2025-08-28 18:49:11

Topic: Quartz Watches

Summary: Quartz watches use a quartz crystal oscillator regulated by an electronic circuit to keep time. When voltage is applied to the crystal, it vibrates at a precise frequency (commonly 32,768 Hz)...

Sources: 
- Wikipedia: Quartz clock
- Wikipedia: Astron (wristwatch)
- Various web sources

Tools Used: 
- search
- wiki_tool
- save_text_to_file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

**Common Issues:**

- **API Key Errors**: Ensure your API keys are correctly set in the `.env` file
- **Parsing Errors**: Check that your LLM model supports the required output format
- **Search Failures**: Verify internet connection and that DuckDuckGo search is accessible

**Error Handling**: The application includes error handling for parsing issues and will display both error messages and raw responses for debugging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [LangChain](https://python.langchain.com/)
- Uses [DuckDuckGo](https://duckduckgo.com/) for web search
- Wikipedia integration via [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)
