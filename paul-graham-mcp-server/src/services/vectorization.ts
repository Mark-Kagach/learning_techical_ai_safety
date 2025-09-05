import OpenAI from "openai";

function getOpenAIClient() {
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
        throw new Error("OPENAI_API_KEY environment variable is required");
    }
    return new OpenAI({ apiKey });
}

export async function vectorizeQuery(query: string): Promise<number[]> {
    try {
        const openai = getOpenAIClient();
        const response = await openai.embeddings.create({
            model: "text-embedding-ada-002",
            input: query,
        });

        return response.data[0].embedding;
    } catch (error) {
        console.error("Error vectorizing query:", error);
        throw new Error(
            `Failed to vectorize query: ${
                error instanceof Error ? error.message : "Unknown error"
            }`
        );
    }
}
