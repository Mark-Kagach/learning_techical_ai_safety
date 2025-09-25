import * as dotenv from "dotenv";
import { createClient } from "@supabase/supabase-js";

// Load environment variables
dotenv.config();

async function testSupabaseReal() {
    console.log("Testing Real Supabase Database...");
    console.log("=================================");

    const supabaseUrl = process.env.SUPABASE_URL as string;
    const supabaseKey = process.env.SUPABASE_ANON_KEY as string;

    try {
        const supabase = createClient(supabaseUrl, supabaseKey);

        // Test 1: Check paul_graham table structure
        console.log("1. Testing paul_graham table access...");
        const { data: sampleData, error: sampleError } = await supabase
            .from("paul_graham")
            .select("id, essay_title, content")
            .limit(1);

        if (sampleError) {
            console.log(`   ❌ Table access failed: ${sampleError.message}`);
            return;
        }

        console.log("   ✅ Table access successful!");
        if (sampleData && sampleData.length > 0) {
            const sample = sampleData[0];
            console.log(`   📊 Sample record:`);
            console.log(`      ID: ${sample.id}`);
            console.log(`      Essay: ${sample.essay_title}`);
            console.log(
                `      Content: "${sample.content?.substring(0, 100)}..."`
            );
        }

        // Test 2: Check total count
        console.log("\n2. Checking total record count...");
        const { count, error: countError } = await supabase
            .from("paul_graham")
            .select("*", { count: "exact", head: true });

        if (!countError) {
            console.log(`   ✅ Total records: ${count}`);
        }

        // Test 3: Test RPC function with a dummy vector
        console.log("\n3. Testing find_similar_paragraphs RPC function...");

        const testVector = Array(1536).fill(0.1); // Dummy vector for testing structure

        const { data: rpcData, error: rpcError } = await supabase.rpc(
            "find_similar_paragraphs",
            {
                query_embedding: testVector,
                similarity_threshold: 0.5,
                match_count: 2,
            }
        );

        if (rpcError) {
            console.log(`   ❌ RPC function failed: ${rpcError.message}`);
            console.log(
                `   🔧 Error details: ${JSON.stringify(rpcError, null, 2)}`
            );
        } else {
            console.log(`   ✅ RPC function works!`);
            console.log(`   📊 Returned ${rpcData?.length || 0} results`);

            if (rpcData && rpcData.length > 0) {
                const sample = rpcData[0];
                console.log(`   📋 Sample result structure:`);
                Object.keys(sample).forEach((key) => {
                    const value = sample[key];
                    if (typeof value === "string" && value.length > 50) {
                        console.log(
                            `      ${key}: "${value.substring(0, 50)}..."`
                        );
                    } else {
                        console.log(`      ${key}: ${value}`);
                    }
                });
            }
        }
    } catch (error) {
        console.log(
            `❌ Unexpected error: ${
                error instanceof Error ? error.message : "Unknown error"
            }`
        );
    }

    console.log("\n🎯 Supabase database testing completed!");
}

testSupabaseReal().catch(console.error);
