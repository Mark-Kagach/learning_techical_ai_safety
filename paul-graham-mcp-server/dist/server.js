"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const index_js_1 = require("@modelcontextprotocol/sdk/server/index.js");
const stdio_js_1 = require("@modelcontextprotocol/sdk/server/stdio.js");
const types_js_1 = require("@modelcontextprotocol/sdk/types.js");
const vectorization_1 = require("./services/vectorization");
const similarity_1 = require("./services/similarity");
const dotenv = __importStar(require("dotenv"));
// Load environment variables
dotenv.config();
// Create server instance
const server = new index_js_1.Server({
    name: "paul-graham-mcp-server",
    version: "1.0.0",
}, {
    capabilities: {
        tools: {},
    },
});
// Add initialize handler
server.setRequestHandler(types_js_1.InitializeRequestSchema, async (request) => {
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
server.setRequestHandler(types_js_1.ListToolsRequestSchema, async () => {
    return {
        tools: [
            {
                name: "search_paragraphs",
                description: "Search for similar paragraphs from Paul Graham's essays based on a query",
                inputSchema: {
                    type: "object",
                    properties: {
                        query: {
                            type: "string",
                            description: "The search query to find similar paragraphs",
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
server.setRequestHandler(types_js_1.CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    if (name === "search_paragraphs") {
        const { query } = args;
        if (!query || typeof query !== "string") {
            throw new Error("Query parameter is required and must be a string");
        }
        try {
            console.error(`Processing query: ${query}`);
            // Step 1: Vectorize the user query
            const vector = await (0, vectorization_1.vectorizeQuery)(query);
            console.error(`Query vectorized successfully`);
            // Step 2: Find similar paragraphs in the database
            const similarParagraphs = await (0, similarity_1.findSimilarParagraphs)(vector);
            console.error(`Found ${similarParagraphs.length} similar paragraphs`);
            // Format results for better readability
            const formattedResults = similarParagraphs
                .map((p, index) => `${index + 1}. [${p.source}] ${p.paragraph} (similarity: ${p.similarity?.toFixed(3) || "N/A"})`)
                .join("\n\n");
            return {
                content: [
                    {
                        type: "text",
                        text: `Found ${similarParagraphs.length} similar paragraphs for query: "${query}"\n\n${formattedResults}`,
                    },
                ],
            };
        }
        catch (error) {
            console.error(`Error processing query: ${error}`);
            throw new Error(`Failed to process query: ${error instanceof Error ? error.message : "Unknown error"}`);
        }
    }
    throw new Error(`Unknown tool: ${name}`);
});
// Main function
async function main() {
    const transport = new stdio_js_1.StdioServerTransport();
    await server.connect(transport);
    console.error("Paul Graham MCP server running on stdio");
}
// Handle errors
main().catch((error) => {
    console.error("Server failed to start:", error);
    process.exit(1);
});
