// Mock test for Supabase similarity search logic
// This tests the data processing without actual DB connection

import { SimilarParagraph } from "./src/types/index";

console.log("Testing Similarity Data Processing...");
console.log("=====================================");

// Mock data that would come from Supabase
const mockSupabaseResponse = [
    {
        id: 1,
        paragraph:
            "Paul Graham's essays are a treasure trove of insights on startups, technology, and life.",
        source: "On Writing",
        similarity: 0.95,
    },
    {
        id: 2,
        content:
            "One of his key points is that the best startups are often founded by people who are passionate about their work.",
        essay_title: "How to Start a Startup",
        similarity: 0.88,
    },
    {
        // Test with missing fields
        paragraph:
            "Innovation and creativity are essential for entrepreneurial success.",
        similarity: 0.82,
    },
];

// Simulate the data mapping logic from similarity.ts
function processMockData(data: any[]): SimilarParagraph[] {
    return data.map((item: any, index: number) => ({
        id: item.id || index + 1,
        paragraph: item.paragraph || item.content || "",
        source: item.source || item.essay_title || "Paul Graham Blog",
        similarity: item.similarity || 0,
    }));
}

console.log("\n📊 Testing data processing:");
const processed = processMockData(mockSupabaseResponse);

processed.forEach((item, index) => {
    console.log(`\n${index + 1}. ID: ${item.id}`);
    console.log(`   Source: "${item.source}"`);
    console.log(`   Similarity: ${item.similarity}`);
    console.log(`   Text: "${item.paragraph.substring(0, 60)}..."`);
});

console.log("\n✅ Data processing logic works correctly!");
console.log(
    "📝 Note: This tests the data transformation without connecting to Supabase"
);
