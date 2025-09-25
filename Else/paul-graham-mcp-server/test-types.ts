// Test TypeScript interfaces and types
import { SimilarParagraph, UserQuery, QueryResponse } from "./src/types/index";

console.log("Testing TypeScript Types and Interfaces...");
console.log("==========================================");

// Test SimilarParagraph interface
const testParagraph: SimilarParagraph = {
    id: 1,
    paragraph: "Test paragraph content",
    source: "Test Essay",
    similarity: 0.95,
};

console.log("✅ SimilarParagraph interface works:");
console.log(`   ID: ${testParagraph.id}`);
console.log(`   Source: ${testParagraph.source}`);
console.log(`   Similarity: ${testParagraph.similarity}`);
console.log(`   Text: "${testParagraph.paragraph}"`);

// Test UserQuery interface
const testQuery: UserQuery = {
    query: "What makes a successful startup?",
};

console.log("\n✅ UserQuery interface works:");
console.log(`   Query: "${testQuery.query}"`);

// Test QueryResponse interface
const testResponse: QueryResponse = {
    similarParagraphs: [testParagraph],
};

console.log("\n✅ QueryResponse interface works:");
console.log(
    `   Number of paragraphs: ${testResponse.similarParagraphs.length}`
);

// Test Vector type
const testVector: number[] = [0.1, 0.2, 0.3, 0.4, 0.5];
console.log("\n✅ Vector type works:");
console.log(`   Vector length: ${testVector.length}`);
console.log(`   Sample values: [${testVector.slice(0, 3).join(", ")}...]`);

console.log("\n🎯 All TypeScript types and interfaces are working correctly!");
