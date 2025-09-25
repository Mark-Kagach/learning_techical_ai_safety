"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.vectorizeQuery = void 0;
const openai_1 = __importDefault(require("openai"));
function getOpenAIClient() {
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
        throw new Error("OPENAI_API_KEY environment variable is required");
    }
    return new openai_1.default({ apiKey });
}
async function vectorizeQuery(query) {
    try {
        const openai = getOpenAIClient();
        const response = await openai.embeddings.create({
            model: "text-embedding-ada-002",
            input: query,
        });
        return response.data[0].embedding;
    }
    catch (error) {
        console.error("Error vectorizing query:", error);
        throw new Error(`Failed to vectorize query: ${error instanceof Error ? error.message : "Unknown error"}`);
    }
}
exports.vectorizeQuery = vectorizeQuery;
