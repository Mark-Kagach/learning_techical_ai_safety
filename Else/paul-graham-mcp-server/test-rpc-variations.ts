import * as dotenv from "dotenv";
import { createClient } from "@supabase/supabase-js";

// Load environment variables
dotenv.config();

async function testRPCVariations() {
    console.log("Testing RPC Function Parameter Variations...");
    console.log("============================================");

    const supabase = createClient(
        process.env.SUPABASE_URL as string,
        process.env.SUPABASE_ANON_KEY as string
    );

    const testVector = Array(1536).fill(0.1);

    // Try different parameter combinations
    const variations = [
        {
            name: "Original order",
            params: {
                query_embedding: testVector,
                similarity_threshold: 0.5,
                match_count: 2,
            },
        },
        {
            name: "Different order 1",
            params: {
                match_count: 2,
                query_embedding: testVector,
                similarity_threshold: 0.5,
            },
        },
        {
            name: "Different order 2",
            params: {
                similarity_threshold: 0.5,
                match_count: 2,
                query_embedding: testVector,
            },
        },
        {
            name: "Just embedding and count",
            params: {
                query_embedding: testVector,
                match_count: 2,
            },
        },
        {
            name: "Just embedding",
            params: {
                query_embedding: testVector,
            },
        },
    ];

    for (const variation of variations) {
        console.log(`\nTrying: ${variation.name}`);

        try {
            const { data, error } = await supabase.rpc(
                "find_similar_paragraphs",
                variation.params
            );

            if (error) {
                console.log(`   ❌ ${error.message}`);
            } else {
                console.log(`   ✅ Success! Got ${data?.length || 0} results`);
                if (data && data.length > 0) {
                    console.log(
                        `   📋 First result keys: ${Object.keys(data[0]).join(
                            ", "
                        )}`
                    );
                }
                break; // Found working combination
            }
        } catch (e) {
            console.log(
                `   ❌ Exception: ${e instanceof Error ? e.message : "Unknown"}`
            );
        }
    }

    console.log("\n🎯 RPC variation testing completed!");
}

testRPCVariations().catch(console.error);
