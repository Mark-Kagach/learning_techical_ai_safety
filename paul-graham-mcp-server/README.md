# Paul Graham MCP Server

A Model Context Protocol (MCP) server that provides semantic search capabilities over Paul Graham's essays. This server integrates with VS Code and other MCP-compatible applications to help users find relevant quotes and insights from Paul Graham's writings.

## Features

-   🔍 **Semantic Search**: Uses OpenAI embeddings to find contextually relevant paragraphs
-   📚 **Paul Graham Essays**: Comprehensive database of Paul Graham's writings
-   🔌 **MCP Compatible**: Works with VS Code, Cursor, Claude Desktop, and other MCP clients
-   ⚡ **Fast Responses**: Optimized similarity search using Supabase vector operations
-   🎯 **Top 5 Results**: Returns the most relevant paragraphs with similarity scores

## Prerequisites

Before you begin, ensure you have:

-   Node.js (v16 or higher)
-   An OpenAI API key
-   A Supabase project with the Paul Graham essays data

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/paul-graham-mcp-server.git
    cd paul-graham-mcp-server
    ```

2. **Install dependencies**:

    ```bash
    npm install
    ```

3. **Set up environment variables**:

    ```bash
    cp .env.example .env
    ```

    Edit `.env` and add your credentials:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    SUPABASE_URL=your_supabase_project_url
    SUPABASE_ANON_KEY=your_supabase_anon_key
    ```

4. **Build the project**:
    ```bash
    npm run build
    ```

## Usage

### As an MCP Server

1. **Start the server**:

    ```bash
    npm start
    ```

2. **Configure your MCP client** (e.g., VS Code):

    Add to your MCP configuration file (e.g., `.cursor/mcp.json`):

    ```json
    {
        "mcpServers": {
            "paul-graham-mcp-server": {
                "type": "stdio",
                "command": "node",
                "args": ["path/to/your/paul-graham-mcp-server/dist/server.js"],
                "cwd": "path/to/your/paul-graham-mcp-server",
                "env": {
                    "OPENAI_API_KEY": "your_key_here",
                    "SUPABASE_URL": "your_url_here",
                    "SUPABASE_ANON_KEY": "your_key_here"
                }
            }
        }
    }
    ```

3. **Use in your MCP client**:

    The server provides a `search_paragraphs` tool that you can use in VS Code's chat or other MCP clients:

    ```
    What does Paul Graham say about startups?
    ```

### API

The server exposes one main tool:

-   **`search_paragraphs`**: Search for similar paragraphs from Paul Graham's essays
    -   Input: `query` (string) - Your search query
    -   Output: Top 5 most similar paragraphs with sources and similarity scores

## Project Structure

```
paul-graham-mcp-server/
├── src/
│   ├── server.ts               # Main MCP server implementation
│   ├── types/
│   │   └── index.ts            # TypeScript type definitions
│   ├── services/
│   │   ├── vectorization.ts    # OpenAI embedding service
│   │   ├── supabase.ts         # Supabase client configuration
│   │   └── similarity.ts       # Similarity search logic
│   ├── utils/
│   │   ├── embedding.ts        # Embedding utilities
│   │   └── validation.ts       # Input validation
│   └── config/
│       └── database.ts         # Database configuration
├── data/
│   └── sample-paragraphs.json  # Sample Paul Graham essay excerpts
├── dist/                       # Compiled JavaScript (generated)
├── package.json
├── tsconfig.json
├── .env.example               # Environment variables template
├── .gitignore
├── LICENSE
└── README.md
```

## Development

### Running Tests

```bash
# Run all tests
npm test

# Run specific test files
npx ts-node test-vectorization.ts
npx ts-node test-supabase-real.ts
npx ts-node test-end-to-end.ts
```

## Database Setup

This server requires a Supabase database with Paul Graham's essays. The database should have:

-   A `paul_graham` table with columns: `id`, `paragraph`, `source`, `embedding`
-   A custom RPC function `paul_graham_search` for vector similarity search
-   Proper vector extensions enabled (pgvector)

Contact the repository maintainer for database schema details.
