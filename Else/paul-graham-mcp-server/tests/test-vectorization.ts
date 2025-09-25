import * as dotenv from "dotenv";
import { vectorizeQuery } from "./src/services/vectorization";

// Load environment variables
dotenv.config();

async function testVectorization() {
    console.log("Testing OpenAI Vectorization Service...");
    console.log("======================================");

    const testQueries = [
        "What makes a successful startup?",
        "How to build great products",
        "Paul Graham entrepreneurship advice",
    ];

    for (let i = 0; i < testQueries.length; i++) {
        const query = testQueries[i];
        console.log(`\n${i + 1}. Testing query: "${query}"`);

        try {
            const startTime = Date.now();
            const vector = await vectorizeQuery(query);
            const endTime = Date.now();

            console.log(`   ✅ Success!`);
            console.log(`   📊 Vector dimensions: ${vector.length}`);
            console.log(
                `   📈 Sample values: [${vector
                    .slice(0, 5)
                    .map((v) => v.toFixed(4))
                    .join(", ")}...]`
            );
            console.log(`   ⏱️  Time taken: ${endTime - startTime}ms`);

            // Basic validation
            if (vector.length !== 1536) {
                console.log(
                    `   ⚠️  Warning: Expected 1536 dimensions, got ${vector.length}`
                );
            }

            if (vector.some((v) => isNaN(v))) {
                console.log(`   ❌ Error: Vector contains NaN values`);
            }
        } catch (error) {
            console.log(
                `   ❌ Failed: ${
                    error instanceof Error ? error.message : "Unknown error"
                }`
            );

            // Check if it's an API key issue
            if (error instanceof Error && error.message.includes("401")) {
                console.log(`   💡 Hint: Check if OpenAI API key is valid`);
            }

            // Don't continue if first test fails
            if (i === 0) {
                console.log(`\n🛑 Stopping tests due to API failure`);
                return;
            }
        }
    }

    console.log(`\n🎯 Vectorization testing completed!`);
}

testVectorization().catch(console.error);
