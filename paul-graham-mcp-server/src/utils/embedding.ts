import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
});

export async function getEmbedding(input: string): Promise<number[]> {
    try {
        const response = await openai.embeddings.create({
            model: "text-embedding-ada-002",
            input: input,
        });

        return response.data[0].embedding;
    } catch (error) {
        console.error("Error getting embedding:", error);
        throw new Error(
            `Failed to get embedding: ${
                error instanceof Error ? error.message : "Unknown error"
            }`
        );
    }
}
