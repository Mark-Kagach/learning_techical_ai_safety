import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
    CallToolRequestSchema,
    ListToolsRequestSchema,
    InitializeRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { vectorizeQuery } from "./services/vectorization";
import { findSimilarParagraphs } from "./services/similarity";
import * as dotenv from "dotenv";

// Load environment variables
dotenv.config();

// Create server instance
const server = new Server(
    {
        name: "paul-graham-mcp-server",
        version: "1.0.0",
    },
    {
        capabilities: {
            tools: {},
        },
    }
);

// Add initialize handler
server.setRequestHandler(InitializeRequestSchema, async (request) => {
    const { params } = request;
    return {
        protocolVersion: "2024-11-05",
        capabilities: {
            tools: {},
        },
        serverInfo: {
            name: "paul-graham-mcp-server",
            version: "1.0.0",
        },
    };
});

// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
    return {
        tools: [
            {
                name: "search_paragraphs",
                description:
                    "Search for similar paragraphs from Paul Graham's essays based on a query",
                inputSchema: {
                    type: "object",
                    properties: {
                        query: {
                            type: "string",
                            description:
                                "The search query to find similar paragraphs",
                        },
                    },
                    required: ["query"],
                    additionalProperties: false,
                },
            },
        ],
    };
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    if (name === "search_paragraphs") {
        const { query } = args as { query: string };

        if (!query || typeof query !== "string") {
            throw new Error("Query parameter is required and must be a string");
        }

        try {
            console.error(`Processing query: ${query}`);

            // Step 1: Vectorize the user query
            const vector = await vectorizeQuery(query);
            console.error(`Query vectorized successfully`);

            // Step 2: Find similar paragraphs in the database
            const similarParagraphs = await findSimilarParagraphs(vector);
            console.error(
                `Found ${similarParagraphs.length} similar paragraphs`
            );

            // Format results for better readability
            const formattedResults = similarParagraphs
                .map(
                    (p, index) =>
                        `${index + 1}. [${p.source}] ${
                            p.paragraph
                        } (similarity: ${p.similarity?.toFixed(3) || "N/A"})`
                )
                .join("\n\n");

            return {
                content: [
                    {
                        type: "text",
                        text: `Found ${similarParagraphs.length} similar paragraphs for query: "${query}"\n\n${formattedResults}`,
                    },
                ],
            };
        } catch (error) {
            console.error(`Error processing query: ${error}`);
            throw new Error(
                `Failed to process query: ${
                    error instanceof Error ? error.message : "Unknown error"
                }`
            );
        }
    }

    throw new Error(`Unknown tool: ${name}`);
});

// Main function
async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);

    console.error("Paul Graham MCP server running on stdio");
}

// Handle errors
main().catch((error) => {
    console.error("Server failed to start:", error);
    process.exit(1);
});
