"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getEmbedding = void 0;
const openai_1 = __importDefault(require("openai"));
const openai = new openai_1.default({
    apiKey: process.env.OPENAI_API_KEY,
});
async function getEmbedding(input) {
    try {
        const response = await openai.embeddings.create({
            model: "text-embedding-ada-002",
            input: input,
        });
        return response.data[0].embedding;
    }
    catch (error) {
        console.error("Error getting embedding:", error);
        throw new Error(`Failed to get embedding: ${error instanceof Error ? error.message : "Unknown error"}`);
    }
}
exports.getEmbedding = getEmbedding;
