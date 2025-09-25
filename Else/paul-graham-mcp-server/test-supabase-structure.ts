import * as dotenv from "dotenv";
import { createClient } from "@supabase/supabase-js";

// Load environment variables
dotenv.config();

async function testSupabaseStructure() {
    console.log("Testing Supabase Database Structure...");
    console.log("=====================================");

    const supabaseUrl = process.env.SUPABASE_URL as string;
    const supabaseKey = process.env.SUPABASE_ANON_KEY as string;

    console.log(`📡 Connected to: ${supabaseUrl}`);

    try {
        const supabase = createClient(supabaseUrl, supabaseKey);

        // Test 1: Try to find paragraph-related tables
        console.log("\n1. Looking for paragraph-related data...");

        const possibleTableNames = [
            "paragraphs",
            "paul_graham_paragraphs",
            "essays",
            "blog_paragraphs",
            "documents",
            "content",
        ];

        for (const tableName of possibleTableNames) {
            try {
                const { data, error } = await supabase
                    .from(tableName)
                    .select("*")
                    .limit(1);

                if (!error) {
                    console.log(`   ✅ Found table: ${tableName}`);
                    if (data && data.length > 0) {
                        console.log(`   📊 Sample record structure:`);
                        const sample = data[0];
                        Object.keys(sample).forEach((key) => {
                            const value = sample[key];
                            const type = typeof value;
                            const preview =
                                type === "string" && value.length > 50
                                    ? value.substring(0, 50) + "..."
                                    : value;
                            console.log(`      ${key}: ${type} = ${preview}`);
                        });

                        // Check if this looks like our paragraph table
                        const hasText = Object.keys(sample).some(
                            (key) =>
                                key.includes("paragraph") ||
                                key.includes("content") ||
                                key.includes("text")
                        );
                        const hasEmbedding = Object.keys(sample).some(
                            (key) =>
                                key.includes("embedding") ||
                                key.includes("vector")
                        );

                        if (hasText || hasEmbedding) {
                            console.log(
                                `   🎯 This looks like our target table!`
                            );
                        }
                    }
                    break; // Found a working table
                }
            } catch (e) {
                // Continue to next table
            }
        }

        // Test 2: Try the RPC function with a small test vector
        console.log("\n2. Testing find_similar_paragraphs function...");

        const testVector = Array(1536).fill(0.1);

        try {
            const { data: rpcData, error: rpcError } = await supabase.rpc(
                "find_similar_paragraphs",
                {
                    input_vector: testVector,
                    limit_count: 2,
                }
            );

            if (rpcError) {
                console.log(`   ❌ RPC function error: ${rpcError.message}`);
                console.log(`   🔧 Error code: ${rpcError.code}`);

                // Try without limit_count parameter
                console.log("\n   Trying without limit_count parameter...");
                const { data: rpcData2, error: rpcError2 } = await supabase.rpc(
                    "find_similar_paragraphs",
                    {
                        input_vector: testVector,
                    }
                );

                if (rpcError2) {
                    console.log(`   ❌ Still failed: ${rpcError2.message}`);
                } else {
                    console.log(`   ✅ Works without limit_count!`);
                    console.log(
                        `   📊 Returned ${rpcData2?.length || 0} results`
                    );
                }
            } else {
                console.log(`   ✅ RPC function works!`);
                console.log(`   📊 Returned ${rpcData?.length || 0} results`);

                if (rpcData && rpcData.length > 0) {
                    console.log(`   📋 Sample result:`);
                    const sample = rpcData[0];
                    Object.keys(sample).forEach((key) => {
                        console.log(`      ${key}: ${typeof sample[key]}`);
                    });
                }
            }
        } catch (e) {
            console.log(`   ❌ RPC function doesn't exist or has issues`);
        }
    } catch (error) {
        console.log(
            `❌ Connection error: ${
                error instanceof Error ? error.message : "Unknown error"
            }`
        );
    }

    console.log("\n🎯 Database structure testing completed!");
}

testSupabaseStructure().catch(console.error);
