import { createClient } from "@supabase/supabase-js";
import { SimilarParagraph } from "../types/index.js";

function getSupabaseClient() {
    const supabaseUrl = process.env.SUPABASE_URL as string;
    const supabaseKey = process.env.SUPABASE_ANON_KEY as string;

    if (!supabaseUrl || !supabaseKey) {
        throw new Error("Missing Supabase environment variables");
    }

    return createClient(supabaseUrl, supabaseKey);
}

export async function findSimilarParagraphs(
    vector: number[]
): Promise<SimilarParagraph[]> {
    try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase.rpc("paul_graham_search", {
            query_embedding: vector,
            similarity_threshold: 0.7, // Adjust threshold as needed
            match_count: 5,
        });

        if (error) {
            throw new Error(`Supabase RPC error: ${error.message}`);
        }

        if (!data || !Array.isArray(data)) {
            throw new Error("Invalid response from Supabase");
        }

        return data.map((item: any) => ({
            id: item.id,
            paragraph: item.content, // Using 'content' field from your database
            source: item.essay_title || "Paul Graham Blog",
            similarity: item.similarity || 0,
        }));
    } catch (error) {
        console.error("Error fetching similar paragraphs:", error);
        throw new Error(
            `Failed to find similar paragraphs: ${
                error instanceof Error ? error.message : "Unknown error"
            }`
        );
    }
}
