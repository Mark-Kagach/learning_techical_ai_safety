"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.findSimilarParagraphs = void 0;
const supabase_js_1 = require("@supabase/supabase-js");
function getSupabaseClient() {
    const supabaseUrl = process.env.SUPABASE_URL;
    const supabaseKey = process.env.SUPABASE_ANON_KEY;
    if (!supabaseUrl || !supabaseKey) {
        throw new Error("Missing Supabase environment variables");
    }
    return (0, supabase_js_1.createClient)(supabaseUrl, supabaseKey);
}
async function findSimilarParagraphs(vector) {
    try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase.rpc("paul_graham_search", {
            query_embedding: vector,
            similarity_threshold: 0.7,
            match_count: 5,
        });
        if (error) {
            throw new Error(`Supabase RPC error: ${error.message}`);
        }
        if (!data || !Array.isArray(data)) {
            throw new Error("Invalid response from Supabase");
        }
        return data.map((item) => ({
            id: item.id,
            paragraph: item.content,
            source: item.essay_title || "Paul Graham Blog",
            similarity: item.similarity || 0,
        }));
    }
    catch (error) {
        console.error("Error fetching similar paragraphs:", error);
        throw new Error(`Failed to find similar paragraphs: ${error instanceof Error ? error.message : "Unknown error"}`);
    }
}
exports.findSimilarParagraphs = findSimilarParagraphs;
