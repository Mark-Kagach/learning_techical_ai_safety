import * as dotenv from "dotenv";
import { createClient } from "@supabase/supabase-js";

// Load environment variables
dotenv.config();

async function testSupabaseConnection() {
    console.log("Testing Supabase Connection...");
    console.log("==============================");

    const supabaseUrl = process.env.SUPABASE_URL as string;
    const supabaseKey = process.env.SUPABASE_ANON_KEY as string;

    console.log(`📡 Connecting to: ${supabaseUrl}`);

    try {
        const supabase = createClient(supabaseUrl, supabaseKey);

        // Test 1: Basic connection health check
        console.log("\n1. Testing basic connection...");
        const { data, error } = await supabase
            .from("health_check")
            .select("*")
            .limit(1);

        if (error && error.code !== "PGRST116") {
            // PGRST116 = table not found (expected)
            console.log(`   ❌ Connection failed: ${error.message}`);
            return;
        }

        console.log("   ✅ Basic connection successful!");

        // Test 2: List available tables/functions
        console.log("\n2. Checking available functions...");
        const { data: functions, error: funcError } = await supabase.rpc(
            "help"
        );

        if (funcError) {
            console.log(`   ⚠️  Cannot list functions: ${funcError.message}`);
        } else {
            console.log("   ✅ Function listing works");
        }

        // Test 3: Test the find_similar_paragraphs function exists
        console.log("\n3. Testing find_similar_paragraphs function...");

        // Create a dummy vector to test with
        const testVector = Array(1536).fill(0.1); // OpenAI embedding size

        const { data: similarData, error: similarError } = await supabase.rpc(
            "find_similar_paragraphs",
            {
                input_vector: testVector,
                limit_count: 2,
            }
        );

        if (similarError) {
            console.log(`   ❌ RPC function failed: ${similarError.message}`);
            console.log(
                `   💡 Hint: Make sure 'find_similar_paragraphs' function exists in your database`
            );

            // Let's try to list actual tables
            console.log("\n4. Checking available tables...");
            const { data: tables, error: tableError } = await supabase
                .from("information_schema.tables")
                .select("table_name")
                .eq("table_schema", "public");

            if (!tableError && tables) {
                console.log(
                    `   📊 Available tables: ${tables
                        .map((t) => t.table_name)
                        .join(", ")}`
                );
            }
        } else {
            console.log("   ✅ RPC function exists and works!");
            console.log(`   📊 Returned ${similarData?.length || 0} results`);

            if (similarData && similarData.length > 0) {
                console.log("   📋 Sample result structure:");
                const sample = similarData[0];
                Object.keys(sample).forEach((key) => {
                    console.log(`      ${key}: ${typeof sample[key]}`);
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

    console.log("\n🎯 Supabase connection testing completed!");
}

testSupabaseConnection().catch(console.error);
