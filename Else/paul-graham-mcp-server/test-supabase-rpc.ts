import * as dotenv from "dotenv";
import { createClient } from "@supabase/supabase-js";

// Load environment variables
dotenv.config();

async function testSupabaseConnection() {
    console.log("Testing Supabase Connection with paul_graham_search...");
    console.log("=====================================================");

    const supabaseUrl = process.env.SUPABASE_URL as string;
    const supabaseKey = process.env.SUPABASE_ANON_KEY as string;

    console.log(`📡 Connected to: ${supabaseUrl}`);

    try {
        const supabase = createClient(supabaseUrl, supabaseKey);

        // Test 1: Check table structure
        console.log("\n1. Testing direct table access...");
        const { data: tableData, error: tableError } = await supabase
            .from("paul_graham")
            .select("id, essay_title, content")
            .limit(2);

        if (tableError) {
            console.log(`   ❌ Table access failed: ${tableError.message}`);
            return;
        }

        console.log(
            `   ✅ Table access works! Found ${tableData.length} sample records`
        );
        if (tableData.length > 0) {
            const sample = tableData[0];
            console.log(`   📊 Sample record:`);
            console.log(`      ID: ${sample.id}`);
            console.log(`      Essay: "${sample.essay_title}"`);
            console.log(
                `      Content: "${sample.content.substring(0, 100)}..."`
            );
        }

        // Test 2: Test paul_graham_search function with a dummy vector
        console.log("\n2. Testing paul_graham_search function...");

        const testVector = Array(1536).fill(0.1);

        const { data: searchData, error: searchError } = await supabase.rpc(
            "paul_graham_search",
            {
                query_embedding: testVector,
                similarity_threshold: 0.5,
                match_count: 3,
            }
        );

        if (searchError) {
            console.log(`   ❌ RPC function failed: ${searchError.message}`);
            console.log(`   🔧 Error code: ${searchError.code}`);

            // Try different parameter combinations to debug
            console.log("\n   Trying alternative parameter names...");

            const alternatives = [
                { query_embedding: testVector, match_count: 3 },
                { embedding: testVector, limit_count: 3 },
                {
                    vector: testVector,
                    similarity_threshold: 0.5,
                    match_count: 3,
                },
            ];

            for (let i = 0; i < alternatives.length; i++) {
                try {
                    const { data: altData, error: altError } =
                        await supabase.rpc(
                            "paul_graham_search",
                            alternatives[i]
                        );
                    if (!altError) {
                        console.log(`   ✅ Alternative ${i + 1} works!`);
                        console.log(
                            `   📊 Parameters: ${JSON.stringify(
                                alternatives[i],
                                null,
                                2
                            )}`
                        );
                        break;
                    }
                } catch (e) {
                    // Continue to next alternative
                }
            }
        } else {
            console.log(`   ✅ RPC function works!`);
            console.log(`   📊 Returned ${searchData?.length || 0} results`);

            if (searchData && searchData.length > 0) {
                console.log(`   📋 Sample result structure:`);
                const sample = searchData[0];
                Object.keys(sample).forEach((key) => {
                    const value = sample[key];
                    const preview =
                        typeof value === "string" && value.length > 50
                            ? value.substring(0, 50) + "..."
                            : value;
                    console.log(`      ${key}: ${typeof value} = ${preview}`);
                });
            }
        }
    } catch (error) {
        console.log(
            `❌ Connection error: ${
                error instanceof Error ? error.message : "Unknown error"
            }`
        );
    }

    console.log("\n🎯 Supabase connection testing completed!");
}

testSupabaseConnection().catch(console.error);
