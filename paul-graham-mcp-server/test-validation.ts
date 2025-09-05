import { validateQuery } from "./src/utils/validation";

console.log("Testing Query Validation...");
console.log("==========================");

// Test valid queries
const validQueries = [
    "What are startups?",
    "How to build a great product",
    "Paul Graham's advice on entrepreneurship",
];

console.log("\n✅ Testing valid queries:");
validQueries.forEach((query) => {
    try {
        const result = validateQuery(query);
        console.log(`  ✓ "${query}" -> "${result}"`);
    } catch (error) {
        console.log(
            `  ✗ "${query}" -> Error: ${
                error instanceof Error ? error.message : "Unknown error"
            }`
        );
    }
});

// Test invalid queries
const invalidQueries = [
    "", // empty string
    "   ", // only whitespace
    123, // not a string
    null, // null
    undefined, // undefined
    "a".repeat(1001), // too long
];

console.log("\n❌ Testing invalid queries:");
invalidQueries.forEach((query) => {
    try {
        const result = validateQuery(query);
        console.log(`  ✗ Unexpected success for: ${JSON.stringify(query)}`);
    } catch (error) {
        console.log(
            `  ✓ Correctly rejected: ${JSON.stringify(query)} -> ${
                error instanceof Error ? error.message : "Unknown error"
            }`
        );
    }
});

console.log("\n✅ Query validation tests completed!");
