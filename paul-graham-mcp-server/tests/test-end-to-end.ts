import * as dotenv from "dotenv";
import { vectorizeQuery } from "./src/services/vectorization";
import { findSimilarParagraphs } from "./src/services/similarity";

// Load environment variables
dotenv.config();

async function testEndToEndFlow() {
    console.log("Testing Complete End-to-End Flow...");
    console.log("===================================");

    const testQueries = [
        "What makes a successful startup?",
        "How to build great products",
    ];

    for (let i = 0; i < testQueries.length; i++) {
        const query = testQueries[i];
        console.log(`\n${i + 1}. Testing query: "${query}"`);
        console.log("   ─".repeat(50));

        try {
            // Step 1: Vectorize the query
            console.log("   🔄 Step 1: Vectorizing query...");
            const startVectorize = Date.now();
            const vector = await vectorizeQuery(query);
            const vectorizeTime = Date.now() - startVectorize;
            console.log(
                `   ✅ Vectorized in ${vectorizeTime}ms (${vector.length} dimensions)`
            );

            // Step 2: Search for similar paragraphs
            console.log("   🔄 Step 2: Searching for similar paragraphs...");
            const startSearch = Date.now();
            const similarParagraphs = await findSimilarParagraphs(vector);
            const searchTime = Date.now() - startSearch;
            console.log(
                `   ✅ Found ${similarParagraphs.length} similar paragraphs in ${searchTime}ms`
            );

            // Step 3: Display results
            console.log("   📊 Results:");
            similarParagraphs.forEach((paragraph, index) => {
                console.log(
                    `\n   ${index + 1}. [${
                        paragraph.source
                    }] (similarity: ${paragraph.similarity.toFixed(3)})`
                );
                console.log(
                    `      "${paragraph.paragraph.substring(0, 150)}..."`
                );
            });

            // Step 4: Validate results
            if (similarParagraphs.length === 0) {
                console.log(
                    "   ⚠️  Warning: No results found - may need to adjust similarity threshold"
                );
            } else {
                const avgSimilarity =
                    similarParagraphs.reduce(
                        (sum, p) => sum + p.similarity,
                        0
                    ) / similarParagraphs.length;
                console.log(
                    `   📈 Average similarity: ${avgSimilarity.toFixed(3)}`
                );

                if (avgSimilarity < 0.3) {
                    console.log(
                        "   ⚠️  Warning: Low similarity scores - results may not be very relevant"
                    );
                }
            }

            console.log(`   ⏱️  Total time: ${vectorizeTime + searchTime}ms`);
        } catch (error) {
            console.log(
                `   ❌ Failed: ${
                    error instanceof Error ? error.message : "Unknown error"
                }`
            );

            // Don't continue if first test fails
            if (i === 0) {
                console.log(`\n🛑 Stopping tests due to failure`);
                return;
            }
        }
    }

    console.log(`\n🎯 End-to-end testing completed!`);
    console.log(`\n📝 Next step: Test the MCP server itself`);
}

testEndToEndFlow().catch(console.error);
